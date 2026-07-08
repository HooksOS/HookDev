// ============================================================
// HookDev — content single source of truth.
// Mirrors the original inline DATA object; now consumed at
// build time by the .astro components (no client-side render).
// ============================================================

export interface Product {
  idx: string;
  name: string;
  cat: string;
  chain: string;
  status: string;
  icon: string;
  accent: string;
  logo: string | null;
  url: string;
  desc: string;
  metric: { v: string; l: string };
  feats: string[];
}

export interface Capability {
  hook: string;
  name: string;
  desc: string;
}

export interface Service {
  k: string;
  name: string;
  desc: string;
  items: string[];
}

export interface ProcessStep {
  n: string;
  title: string;
  desc: string;
}

export interface Stat {
  v: string;
  l: string;
}

export interface Faq {
  q: string;
  a: string;
}

export const products: Product[] = [
  { idx: "01", name: "HookOS", cat: "FRAMEWORK", chain: "EVM", status: "LIVE", icon: "ic-os", accent: "#4ADE80", logo: "hookos.svg", url: "https://hookos.fun/", desc: "Modular runtime for building, simulating, and shipping Uniswap V4 hooks.", metric: { v: "120+", l: "Hooks scaffolded" }, feats: ["CLI + SDK", "Fork simulation", "Hook templates"] },
  { idx: "02", name: "HookOS Wallet", cat: "WALLET", chain: "Base · Arbitrum", status: "LIVE", icon: "ic-wallet", accent: "#22C55E", logo: "hookoswallet.svg", url: "https://hookoswallet.xyz/", desc: "Account-abstraction wallet purpose-built for hook-powered DeFi.", metric: { v: "4337", l: "Smart accounts" }, feats: ["Passkeys", "Batched swaps", "Gas sponsorship"] },
  { idx: "03", name: "OV2", cat: "ORACLE", chain: "Cross-chain", status: "BETA", icon: "ic-oracle", accent: "#A855F7", logo: null, url: "https://ov2.fun/", desc: "Manipulation-resistant, low-latency price oracle feeding hooks on-chain.", metric: { v: "<1 blk", l: "Update latency" }, feats: ["TWAP + spot", "Manipulation guard", "Push + pull"] },
  { idx: "04", name: "HookRPC", cat: "INFRA", chain: "Multi-chain", status: "LIVE", icon: "ic-rpc", accent: "#38BDF8", logo: null, url: "https://hookrpc.xyz/", desc: "High-availability RPC and indexing tuned for hook-heavy workloads.", metric: { v: "99.98%", l: "Uptime" }, feats: ["Archive nodes", "Hook indexing", "WebSocket"] },
  { idx: "05", name: "HookSwap", cat: "DEX", chain: "Unichain", status: "BETA", icon: "ic-swap", accent: "#2FE07E", logo: "hookswap.png", url: "https://hookswap.org/", desc: "A DEX where every pool is programmable through hooks.", metric: { v: "$40M+", l: "Routed volume" }, feats: ["Hook pools", "MEV-aware", "Limit orders"] },
];

export const capabilities: Capability[] = [
  { hook: "beforeSwap", name: "Dynamic Fees", desc: "Fees that respond to volatility, volume, or time of day." },
  { hook: "beforeSwap", name: "LVR / MEV Mitigation", desc: "Capture or neutralize loss-versus-rebalancing at the pool." },
  { hook: "afterSwap", name: "On-chain Limit Orders", desc: "Resting orders executed directly inside the pool." },
  { hook: "beforeSwap", name: "TWAMM", desc: "Time-weighted market makers for large orders, split over time." },
  { hook: "afterSwap", name: "Custom Oracles", desc: "Pool-native price feeds with manipulation guards." },
  { hook: "beforeAddLiquidity", name: "Gated & KYC Pools", desc: "Permissioned liquidity with on-chain compliance rules." },
];

export const services: Service[] = [
  { k: "S-01", name: "Uniswap V4 Hook Development", desc: "Custom hooks engineered end-to-end — from spec to audit-ready mainnet deployment.", items: ["Dynamic fees", "LVR / MEV mitigation", "On-chain limit orders", "Gated & KYC pools"] },
  { k: "S-02", name: "Web3 Developer Services", desc: "Full-stack protocol engineering, from smart contracts to production infrastructure.", items: ["Smart contracts", "Audit prep", "Protocol infra", "dApp frontends"] },
];

export const process: ProcessStep[] = [
  { n: "01", title: "Scope", desc: "We map your pool logic, constraints, and threat model into a clear spec." },
  { n: "02", title: "Build", desc: "Hooks written in Solidity, tested with Foundry, simulated against forks." },
  { n: "03", title: "Harden", desc: "Invariant tests, gas profiling, and audit-ready documentation." },
  { n: "04", title: "Ship", desc: "Mainnet deployment, monitoring, and post-launch support." },
];

export const stats: Stat[] = [
  { v: "5", l: "Products shipped" },
  { v: "12+", l: "V4 hooks deployed" },
  { v: "99.98%", l: "RPC uptime" },
  { v: "$40M+", l: "Volume routed" },
];

export const stack: string[] = [
  "Solidity", "Foundry", "Uniswap V4", "EIP-4337", "Viem", "TypeScript", "The Graph", "Base", "Arbitrum", "Unichain",
];

export const faqs: Faq[] = [
  { q: "What is a Uniswap V4 hook?", a: "A contract that runs custom logic at key points in a pool's lifecycle — before and after swaps, liquidity changes, and initialization — letting you reshape how a market behaves." },
  { q: "Do you audit the hooks you build?", a: "We deliver audit-ready code with full test coverage and coordinate third-party audits; we don't self-certify security." },
  { q: "Which chains do you deploy to?", a: "Any EVM chain running Uniswap V4 — including Base, Arbitrum, and Unichain." },
  { q: "Can we license the products standalone?", a: "Yes. HookOS, OV2, and HookRPC are available on their own or bundled with a build engagement." },
];

// hero signature: the real Uniswap V4 hook lifecycle callbacks.
// `on` marks the attachment points where HookDev most often captures value.
export const lifecycle: { name: string; on: boolean }[] = [
  { name: "beforeInitialize", on: false },
  { name: "beforeAddLiquidity", on: true },
  { name: "beforeSwap", on: true },
  { name: "afterSwap", on: true },
  { name: "afterDonate", on: false },
];

// helper shared by the product card component
export const domain = (u: string): string => u.replace(/^https?:\/\//, "").replace(/\/$/, "");
