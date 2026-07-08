# Claude Code prompt — HookDev site + brand kit

Paste this into Claude Code from the root of your project (with this `design_handoff_hookdev/` folder present).

---

You are implementing the **HookDev** marketing site and brand kit in this codebase. HookDev is a Web3 development studio: 5 products (HookOS, HookWallet, OV2, HookRPC, HookSwap) plus Uniswap V4 hook development and Web3 developer services.

**Read `design_handoff_hookdev/README.md` first** — it has the exact design tokens, copy, product data, and section-by-section spec. Then open the HTML references in `design_handoff_hookdev/design/` in a browser to see the intended look.

Important: the `.dc.html` files are **design references**, not production code. Recreate them in this project's stack and conventions:
- If this repo already has a framework (React/Next, Vue, Astro, etc.), use it, along with its existing component and styling patterns.
- If it's empty, scaffold a **Next.js (App Router) + TypeScript + Tailwind** static marketing site.

Requirements:
1. Build it as a **single responsive one-page site** with these sections in order: Nav, Hero, Products, Capabilities, Services, Process, Stats, Tech Stack, FAQ, Brand Kit, CTA, Footer.
2. Implement **direction 1a (Terminal — dark, data-dense)** as the default. Structure the components so a light theme (direction 1b — "Signal") could be layered later; don't hardcode colors — use tokens/CSS variables from the README palette.
3. Use the exact **copy, product table, feature chips, capabilities, process steps, stats, and FAQ** from the README. Put the product/capability/service/FAQ data in a typed data module, not inline JSX.
4. Typography: Space Grotesk (display), IBM Plex Sans (body), IBM Plex Mono (data/labels) via Google Fonts. Match the tracking/weights in the README.
5. Logo: recreate the hook logomark as an inline SVG component (geometry in the README / `HookMascot.dc.html`), tintable via `currentColor` with the `#3B82F6` eye ring. Wordmark = `HOOK` + blue `DEV`.
6. Use the PNGs in `design_handoff_hookdev/social-assets/` for OG/social images and favicons where useful.
7. Make it responsive: two-col hero → stacked on mobile; the 1a product table → stacked cards on mobile; multi-col grids collapse to 1 column.
8. Accessibility: semantic landmarks, focus-visible states on all interactive elements, sufficient contrast, `alt` text.
9. No backend or data fetching — all content is static. Wire the CTA buttons to `mailto:build@hookdev.xyz` and the nav links to in-page anchors.

Deliver a running dev build and a short note on how the theming is structured so I can flip to the light direction later.
