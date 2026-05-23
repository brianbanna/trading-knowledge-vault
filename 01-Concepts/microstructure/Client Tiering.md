---
aliases: [client tiering, flow tiering, spread tiering, client segmentation]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Client Tiering

## Definition
Client tiering is charging different [[Bid-Ask Spread|spreads]] and showing different sizes to different clients based on how informed or toxic their flow is. The market maker analyzes each client's historical [[Markout|markouts]] and classifies them into tiers. Uninformed clients (corporates, passive funds) get tight spreads because their flow is profitable. Informed clients (aggressive hedge funds, latency sensitive algos) get wider spreads to compensate for [[Adverse Selection]]. Tiering is the primary tool for managing flow toxicity in OTC markets where the dealer sees client identity.

## Why it matters (commodities and FX)
In FX, tiering is universal. Every major bank on its [[Single Dealer Platform]] runs a tiering engine that prices each client individually. A corporate treasurer might see 0.5 pips on EUR/USD while a macro hedge fund sees 2.0 pips on the same pair. In commodity OTC markets (swaps, forwards, options), brokers implicitly tier by adjusting voice quotes to the caller. A physical oil trader with cargo intelligence gets a wider Brent swap spread than a passive index rebalancer. Without tiering, the spread must cover the worst case [[Adverse Selection]], which drives away profitable uninformed flow.

## Concrete example

**Concrete:** EUR/USD desk streams 3 client segments. Tier 1 (corporates, passive funds): 10s [[Markout]] +0.2 pips, random flow. Show 0.6 pip spread. Revenue: 0.3 [[Half Spread]] + 0.2 markout = 0.5 pip/trade. 1000 trades/day at 5M average = $250,000/day. Tier 2 (active asset managers): 10s markout -0.5 pips. Show 1.5 pip spread. Revenue: 0.75 half spread - 0.5 markout = 0.25/trade. 500 trades at 10M = $125,000/day. Tier 3 (HFT, aggressive funds): 10s markout -3.0 pips. Show 4.0 pip spread, max 1M. Revenue: 2.0 half spread - 3.0 markout = -1.0/trade. 50 trades at 1M = -$5,000/day. Total: $370,000/day. Flat spread for all: tier 3 trades aggressively at 1.5 pips, generating -$150,000/day, dropping net to $220,000 or worse.

**Simplified:** Different clients cost the dealer different amounts. A corporate treasurer is profitable to trade with. A fast hedge fund is expensive. Charge each one a price that reflects what they cost you. Same idea as insurance companies charging high risk drivers more.

## Key mechanics and formulas
- **Optimal spread for client i** = 2 x max(0, |E[Markout_i]|) + minimum margin. [[Half Spread]] covers expected AS
- **Tier assignment** uses rolling markout stats, typically 1 to 4 week windows, recomputed daily
- **Spread ladder:** 3 to 7 tiers, with spread multipliers (Tier 1 = 1x base, Tier 2 = 2x, Tier 3 = 5x)
- **Size tiering:** toxic clients see both wider spreads and smaller max sizes (1M vs 50M)
- **Feedback loop:** widening spreads on a toxic client cuts their volume, but residual trades may be even more toxic (they only trade when most confident). Monitor continuously

## Prerequisites
- [[Adverse Selection]]
- [[Markout]]
- [[Toxic Flow]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Last Look]] , complementary tool to reject specific fills rather than widen the entire spread
- [[Internalization]] , using tiering data to decide which flow to net internally
- [[Single Dealer Platform]] , the venue delivering tiered prices
- [[ECN]] , anonymous venues where tiering is impossible
- [[Two Way Price]] , the output tiering adjusts per client
- [[Flow Signals]] , aggregating tiered flow data to extract direction signals

## Common misconceptions
1. **"Tiering is unfair to informed clients."** Tiering is rational pricing. The informed client still gets a service (immediate execution) at a price reflecting the cost of providing it.
2. **"Tiering is static."** Good tiering is dynamic. A corporate suddenly trading around ECB meetings with perfect timing should be reclassified. Weekly or daily recalibration is standard.
3. **"You can tier on an ECN."** On anonymous CLOBs ([[ECN]]), tiering is impossible because the counterparty is unknown. Dealers prefer [[Single Dealer Platform|SDP]] flow for this reason.
4. **"Wider tiers solve everything."** If a client's markout is -10 pips and I show 12 pip spread, they stop trading. Tiering must balance profitability against losing the relationship.

## Sources
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- King, M., Osler, C., Rime, D. "Foreign Exchange Market Structure, Players, and Evolution," *Handbook of Exchange Rates*
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
