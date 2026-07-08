#!/usr/bin/env python3
"""
Deploy the HookDev static site (Astro build) to the VPS behind nginx.

Secure by design: authenticates with an SSH *key* (path below or $HOOKDEV_SSH_KEY),
never a password. Creates an isolated web root and nginx server block for the
domain and does not touch any other site, container, or port on the host.

Usage:
    python deploy.py            # build + upload + nginx (+ certbot if DNS points here)
    python deploy.py --ssl-only # just (re)issue/renew the TLS cert via certbot
    python deploy.py --no-ssl   # deploy files only, skip certbot

Requires: paramiko (pip install paramiko), and `npm` locally to build.
"""
import argparse
import os
import subprocess
import sys
import tarfile
import tempfile

import paramiko

# ---- config (override via env) ---------------------------------------------
HOST = os.environ.get("HOOKDEV_SSH_HOST", "15.204.8.186")
USER = os.environ.get("HOOKDEV_SSH_USER", "ubuntu")
KEY = os.path.expanduser(os.environ.get("HOOKDEV_SSH_KEY", "~/.ssh/hookos_deploy"))
DOMAIN = "hookdev.xyz"
WEBROOT = f"/var/www/{DOMAIN}"
EMAIL = os.environ.get("HOOKDEV_CERTBOT_EMAIL", "hookoseth@gmail.com")
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DIST_DIR = os.path.join(REPO_DIR, "dist")
REMOTE_TMP = "/tmp/hookdev-dist.tgz"

NGINX_CONF = f"""# HookDev — Uniswap V4 Hook Studio (static Astro build). Managed by deploy.py.
# Isolated server block; does not affect other sites on this host.
server {{
    listen 80;
    listen [::]:80;
    server_name {DOMAIN} www.{DOMAIN};

    root {WEBROOT};
    index index.html;

    location / {{
        try_files $uri $uri/ /index.html;
    }}

    location /_astro/ {{
        expires 1y;
        add_header Cache-Control "public, immutable";
        try_files $uri =404;
    }}

    location /assets/ {{
        expires 30d;
        add_header Cache-Control "public";
        try_files $uri =404;
    }}

    gzip on;
    gzip_types text/css application/javascript image/svg+xml application/json;
    gzip_min_length 1024;

    access_log /var/log/nginx/{DOMAIN}.access.log;
    error_log  /var/log/nginx/{DOMAIN}.error.log;
}}
"""


def sh(cmd, cwd=None):
    """Run a local command, streaming output; abort on failure."""
    print(f"$ {cmd}")
    if subprocess.run(cmd, shell=True, cwd=cwd).returncode != 0:
        sys.exit(f"!! local command failed: {cmd}")


def connect():
    c = paramiko.SSHClient()
    c.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    c.connect(HOST, username=USER, key_filename=KEY, timeout=25,
              look_for_keys=False, allow_agent=False)
    return c


def run(c, cmd, check=True):
    _, out, err = c.exec_command(cmd, timeout=300)
    rc = out.channel.recv_exit_status()
    o = out.read().decode(errors="replace").strip()
    e = err.read().decode(errors="replace").strip()
    print(f"[{'OK ' if rc == 0 else 'ERR'}] $ {cmd}")
    if o:
        print(o)
    if e:
        print("  stderr:", e)
    if check and rc != 0:
        c.close()
        sys.exit("!! remote command failed, aborting.")
    return rc, o, e


def build_and_pack():
    sh("npm run build", cwd=REPO_DIR)
    if not os.path.isdir(DIST_DIR):
        sys.exit("!! dist/ not found after build")
    tgz = os.path.join(tempfile.gettempdir(), "hookdev-dist.tgz")
    print(f"packing {DIST_DIR} -> {tgz}")
    with tarfile.open(tgz, "w:gz") as t:
        for name in os.listdir(DIST_DIR):
            t.add(os.path.join(DIST_DIR, name), arcname=name)
    return tgz


def deploy_files(c, tgz):
    print("\n=== upload + extract ===")
    sftp = c.open_sftp()
    sftp.put(tgz, REMOTE_TMP)
    sftp.close()
    run(c, f"sudo mkdir -p {WEBROOT}")
    run(c, f"sudo rm -rf {WEBROOT:s}/* {WEBROOT}/.[!.]* 2>/dev/null; true", check=False)
    run(c, f"sudo tar -xzf {REMOTE_TMP} -C {WEBROOT}")
    run(c, f"sudo chown -R www-data:www-data {WEBROOT}")
    run(c, f"sudo find {WEBROOT} -type d -exec chmod 755 {{}} +")
    run(c, f"sudo find {WEBROOT} -type f -exec chmod 644 {{}} +")
    run(c, f"rm -f {REMOTE_TMP}", check=False)


def deploy_nginx(c):
    print("\n=== nginx server block ===")
    conf_hex = NGINX_CONF.encode().hex()
    run(c, f"echo {conf_hex} | xxd -r -p | "
           f"sudo tee /etc/nginx/sites-available/{DOMAIN}.conf > /dev/null")
    run(c, f"sudo ln -sfn /etc/nginx/sites-available/{DOMAIN}.conf "
           f"/etc/nginx/sites-enabled/{DOMAIN}.conf")
    rc, _, _ = run(c, "sudo nginx -t", check=False)
    if rc != 0:
        run(c, f"sudo rm -f /etc/nginx/sites-enabled/{DOMAIN}.conf", check=False)
        c.close()
        sys.exit("!! nginx config invalid — rolled back, not reloaded.")
    run(c, "sudo systemctl reload nginx")
    run(c, f"sleep 1; curl -s -o /dev/null -w 'local serve: HTTP %{{http_code}}\\n' "
           f"-H 'Host: {DOMAIN}' http://127.0.0.1/", check=False)


def deploy_ssl(c):
    print("\n=== certbot (SSL) ===")
    _, ip, _ = run(c, f"dig +short A {DOMAIN} @1.1.1.1", check=False)
    if ip.strip() != HOST:
        print(f"!! {DOMAIN} resolves to '{ip.strip() or '(none)'}', not {HOST}.")
        print("   Add DNS A records:  @ -> 15.204.8.186  and  www -> 15.204.8.186")
        print("   Then run:  python deploy.py --ssl-only")
        return
    run(c, f"sudo certbot --nginx -d {DOMAIN} -d www.{DOMAIN} --non-interactive "
           f"--agree-tos -m {EMAIL} --redirect", check=False)
    run(c, f"curl -s -o /dev/null -w 'https: HTTP %{{http_code}}\\n' https://{DOMAIN}/",
        check=False)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ssl-only", action="store_true", help="only run certbot")
    ap.add_argument("--no-ssl", action="store_true", help="deploy files, skip certbot")
    args = ap.parse_args()

    c = connect()
    try:
        if args.ssl_only:
            deploy_ssl(c)
        else:
            tgz = build_and_pack()
            deploy_files(c, tgz)
            deploy_nginx(c)
            if not args.no_ssl:
                deploy_ssl(c)
        print("\n=== done ===")
    finally:
        c.close()


if __name__ == "__main__":
    main()
