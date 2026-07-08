# Handoff: HookDev — Marketing Site + Brand Kit

## Overview
HookDev is a Web3 development studio that ships five products (HookOS, HookWallet, OV2, HookRPC, HookSwap) and offers Uniswap V4 hook development + general Web3 developer services. This package contains the full one-page marketing site (products, services, capabilities, process, stats, tech stack, FAQ, brand kit, contact) plus a complete social brand kit.

Two visual directions are included in the same design file:
- **1a — Terminal**: dark, data-dense, Bloomberg-terminal-leaning.
- **1b — Signal**: light, spacious, minimal.
Both share one brand system (logo, color, type). Pick one to ship; they are not meant to coexist in production.

## About the Design Files
The files in `design/` are **design references authored in HTML** (a lightweight streaming component format — `.dc.html`). They are prototypes showing the intended look, layout, and behavior — **not production code to copy verbatim**. The task is to **recreate these designs in the target codebase's environment** (e.g. React/Next.js, Vue, Astro) using its established patterns, component library, and styling approach. If no environment exists yet, choose the most appropriate stack (a static React/Next.js or Astro marketing site is a natural fit) and implement there.

The `.dc.html` files can be opened directly in a browser to view the reference. `support.js` is the runtime that renders them — it is only needed to preview the references, not to ship.

## Fidelity
**High-fidelity.** Final colors, typography, spacing, and copy are all specified below and in the files. Recreate the UI pixel-accurately using the codebase's own libraries.

## Design Tokens

### Color
| Token | Hex | Use |
|---|---|---|
| Ink | `#0A0E14` | Primary dark background |
| Slate | `#141B2D` | Raised surfaces on dark |
| Panel (1a) | `#0F1420` | Cards on dark |
| Ticker (1a) | `#0B1120` | Ticker/footer bars |
| Signal | `#1E40AF` | Primary brand blue (buttons, accents) |
| Beam | `#3B82F6` | Bright accent, links, logo "DEV", hook-mark eye |
| Fog | `#8B94A6` | Muted text on dark |
| Text on dark | `#DFE4EC` | Body text on dark |
| Paper | `#F6F7F9` | Light-mode surface / secondary bg (1b) |
| Ink text (1b) | `#0A0E14` | Text on light |
| Muted (1b) | `#5B6472` | Body text on light |
| Positive | `#22C55E` | Status "online / up" dots only |
| Border on dark | `rgba(255,255,255,.08)` | Hairlines, grid |
| Border on light | `rgba(10,14,20,.10)` | Hairlines, card borders |

### Typography
- **Display / headings**: Space Grotesk (600/700). Tight tracking on large sizes (`letter-spacing: -0.02em`).
- **Body / UI**: IBM Plex Sans (400/500/600).
- **Data, labels, code, tickers**: IBM Plex Mono (500), often uppercase with wide tracking (`letter-spacing: .1em–.16em`).
- Hero display sizes: 60px (1a) / 72px (1b). Section headings: 34px (1a) / 40px (1b). Never below 11px for mono labels.

### Spacing & shape
- Section padding: 40px (1a) / 48–64px (1b).
- Card radius: 12px (1a) / 14–16px (1b). Buttons: 6–10px. Pills: 20px.
- 1a uses 1px hairline dividers between every section (terminal grid feel); 1b uses whitespace + a few `#F6F7F9` bands.
- Button primary: bg `#1E40AF`, white text, 600 weight. Secondary: transparent with 1px border.

## Logo / Mascot
The mark is a **geometric "hook" logomark** (see `design/HookMascot.dc.html`), NOT a character mascot. Monochrome stem in `currentColor` (so it tints to context) with a `#3B82F6` "eye" ring at the top. SVG geometry (viewBox `0 0 120 120`):
```
stem+curl: M64 30 L64 66 C64 86 46 90 43 72 C41.5 64 48 62 52 67   (stroke-width 11, round caps)
eye ring:  circle cx=64 cy=26 r=9                                   (stroke #3b82f6, width 7)
```
Wordmark lockup: `HOOK` (ink or white) + `DEV` (Signal/Beam blue), Space Grotesk 700, letter-spacing .02em.

## Screens / Sections (one page, top → bottom)
Order for **1a (Terminal)**: Ticker bar → Nav → Hero (headline + system-status data panel) → Products (table rows) → Capabilities (3-col grid) → Services (2 cards) → Process (4 steps) → Stats (4-col) → Tech Stack (mono chips) → FAQ (2-col) → Brand Kit (logo lockup, palette, type, mark usage, social) → CTA → Footer.
Order for **1b (Signal)**: Nav → Hero (headline + studio-facts card) → Products (2-col cards) → Capabilities → Services → Process → Stats → Tech Stack → FAQ → Brand Kit → CTA → Footer.

### Nav
Logo lockup left; links (Products, Services, Process, Brand) + primary CTA button ("Start a build") right. Mono links on 1a, sans links on 1b.

### Hero
Two-column. Left: mono eyebrow label, big Space Grotesk headline (1a: "We build the hooks that power onchain markets." / 1b: "Hooks that power onchain markets." with "markets" in blue), body paragraph, two buttons. Right: 1a = a dark "system status" board listing the 5 products with green dots + a 2×2 metrics grid; 1b = a dark "studio" facts card (Founded 2023 / Focus V4 + AA / Products 5 / Chains Base·Arb·Uni).

### Products (data below, exact copy)
| # | Name | Category | Chain | Status | Metric | Description |
|---|---|---|---|---|---|---|
| 01 | HookOS | FRAMEWORK | EVM | LIVE | 120+ hooks scaffolded | Modular runtime for building, simulating, and shipping Uniswap V4 hooks. |
| 02 | HookWallet | WALLET | Base · Arbitrum | LIVE | 4337 smart accounts | Account-abstraction wallet purpose-built for hook-powered DeFi. |
| 03 | OV2 | ORACLE | Cross-chain | BETA | <1 blk update latency | Manipulation-resistant, low-latency price oracle feeding hooks on-chain. |
| 04 | HookRPC | INFRA | Multi-chain | LIVE | 99.98% uptime | High-availability RPC and indexing tuned for hook-heavy workloads. |
| 05 | HookSwap | DEX | Unichain | BETA | $40M+ routed volume | A DEX where every pool is programmable through hooks. |

Feature chips per product — HookOS: CLI + SDK, Fork simulation, Hook templates · HookWallet: Passkeys, Batched swaps, Gas sponsorship · OV2: TWAP + spot, Manipulation guard, Push + pull · HookRPC: Archive nodes, Hook indexing, WebSocket · HookSwap: Hook pools, MEV-aware, Limit orders.

### Capabilities (hooks we build)
Dynamic Fees · LVR / MEV Mitigation · On-chain Limit Orders · TWAMM · Custom Oracles · Gated & KYC Pools. (Each with a one-line description — see the file.)

### Services
- **S-01 Uniswap V4 Hook Development** — items: Dynamic fees, LVR / MEV mitigation, On-chain limit orders, Gated & KYC pools.
- **S-02 Web3 Developer Services** — items: Smart contracts, Audit prep, Protocol infra, dApp frontends.

### Process
01 Scope → 02 Build → 03 Harden → 04 Ship (blue top-border cards).

### Stats
5 Products shipped · 12+ V4 hooks deployed · 99.98% RPC uptime · $40M+ Volume routed.

### Tech Stack
Solidity, Foundry, Uniswap V4, EIP-4337, Viem, TypeScript, The Graph, Base, Arbitrum, Unichain (mono outline chips).

### FAQ
Four Q&As (what is a V4 hook / do you audit / which chains / licensing) — exact copy in the file.

### Brand Kit
Logo lockups, 6-swatch palette, typography specimen, mark-usage tiles (ink/blue/paper), and a **Social** block: X, Facebook, YouTube handle cards + a profile banner + circular avatar mock.

### CTA + Footer
CTA: "Let's build your hook." + primary button + `build@hookdev.xyz`. Footer: mark + "HookDev © 2026" + Products/Services/Docs/X links.

## Interactions & Behavior
- Hover states on nav links, buttons, product rows/cards (subtle bg/border lift; keep within the palette).
- Buttons and cards use the radii above; primary CTAs use `#1E40AF`.
- Fully responsive is not specified in the reference (fixed 1200px artboards). Recreate as a responsive marketing page: hero two-col → stacked on mobile; product table (1a) → stacked cards on mobile; grids collapse to 1 col.
- No data fetching — all content is static copy (see `renderVals()` in the site file for the source-of-truth data arrays).

## State Management
None required beyond a possible light/dark theme toggle if you want to offer both 1a and 1b. Content is static.

## Assets
`social-assets/` — production PNG exports (exact platform dimensions):
- `hookdev-avatar-ink-400.png`, `hookdev-avatar-signal-400.png` — profile avatars (square, circle-safe; export at 400/512/800).
- `hookdev-x-header-1500x500.png` — X/Twitter header.
- `hookdev-youtube-2560x1440.png` — YouTube channel art (content within 1546×423 safe area).
- `hookdev-facebook-820x312.png` — Facebook cover.
- `hookdev-linkedin-1128x191.png` — LinkedIn cover.
Handles across platforms: X `@hookdev`, YouTube `@hookdev`, Facebook `/hookdev`, LinkedIn `/company/hookdev`, Discord `/hookdev`, Telegram `@hookdev`.
Fonts: Space Grotesk, IBM Plex Sans, IBM Plex Mono (Google Fonts).

## Files
- `design/HookDev Site.dc.html` — the full site, both directions (1a + 1b). Data arrays live in the `<script data-dc-script>` `renderVals()` at the bottom.
- `design/HookDev Social Assets.dc.html` — the social artboards + handle set.
- `design/HookMascot.dc.html` — the hook logomark SVG.
- `design/support.js` — preview runtime (reference only; do not ship).
- `claude-prompt.md` — a ready-to-paste prompt for Claude Code.
