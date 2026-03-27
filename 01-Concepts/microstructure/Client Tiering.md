---
aliases: [client tiering, flow tiering, spread tiering, client segmentation]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Client Tiering

## Definition
Client tiering is the practice of charging different [[Bid-Ask Spread|spreads]] and showing different sizes to different clients based on how informed or toxic their order flow is. A market maker analyzes each client's historical [[Markout|markouts]] and classifies them into tiers. Uninformed clients (corporates, passive funds) get tight spreads because their flow is profitable to fill. Informed clients (aggressive hedge funds, latency sensitive algorithms) get wider spreads to compensate for [[Adverse Selection]]. Tiering is the primary tool for managing flow toxicity in OTC markets where the dealer knows the client's identity.

## Why it matters (commodities and FX)
In FX, tiering is universal. Every major bank on its [[Single Dealer Platform]] maintains a tiering engine that prices each client individually. The spread a corporate treasurer sees on EUR/USD might be 0.5 pips while a macro hedge fund sees 2.0 pips for the same pair. In commodity OTC markets (swaps, forwards, options), brokers implicitly tier by adjusting voice quotes based on who is calling. A physical oil trader known for having cargo intelligence gets a wider Brent swap spread than a passive index rebalancer. Without tiering, a dealer's spread must be wide enough to cover the worst case [[Adverse Selection]], which drives away profitable uninformed flow.

## Concrete example
I run a EUR/USD market making desk. I stream prices to 3 client segments.

**Tier 1 (Corporates, passive funds):** Average 10 second [[Markout]] is +0.2 pips. Their flow is random. I show a 0.6 pip spread. Revenue: [[Half Spread]] of 0.3 pips + markout of 0.2 pips = 0.5 pips per trade. 1000 trades/day at 5 million average = $250,000/day.

**Tier 2 (Active asset managers):** Average 10 second markout is negative 0.5 pips. Mildly informed. I show a 1.5 pip spread. Revenue: half spread of 0.75 pips minus markout loss of 0.5 pips = 0.25 pips per trade. 500 trades/day at 10 million = $125,000/day.

**Tier 3 (Aggressive hedge funds, HFT):** Average 10 second markout is negative 3.0 pips. Highly toxic. I show a 4.0 pip spread and max size of 1 million. Revenue: half spread of 2.0 pips minus markout loss of 3.0 pips = negative 1.0 pip per trade. But volume is small due to wide spreads. 50 trades/day at 1 million = negative $5,000/day. Acceptable cost for maintaining the relationship.

**Win scenario:** Total daily P&L = $250,000 + $125,000 minus $5,000 = $370,000. Tiering concentrates profit in benign flow and limits losses on toxic flow.

**Fail scenario:** I use a single 1.5 pip spread for everyone. Tier 3 clients now trade aggressively at the tight spread, generating negative $150,000/day. Tier 1 clients get the same price either way, so revenue stays flat. Net daily P&L drops to $220,000. Worse, the tier 3 volume explodes because 1.5 pips is cheap for them, and losses could exceed $300,000/day.

## Key mechanics and formulas
- **Optimal spread for client i** = 2 x max(0, |E[Markout_i]|) + minimum margin. This ensures the [[Half Spread]] covers expected adverse selection
- **Tier assignment** is based on rolling markout statistics, typically 1 to 4 week windows, recomputed daily
- **Spread ladder:** Common to have 3 to 7 tiers, with spread multipliers (e.g., Tier 1 = 1x base spread, Tier 2 = 2x, Tier 3 = 5x)
- **Size tiering:** Toxic clients may see both wider spreads and smaller maximum sizes (e.g., 1 million instead of 50 million)
- **Feedback loop:** Widening spreads on a toxic client reduces their volume, but the remaining trades may be even more toxic (they only trade when they are most confident). Must monitor continuously

## Prerequisites
- [[Adverse Selection]]
- [[Markout]]
- [[Toxic Flow]]
- [[Bid-Ask Spread]]

## Related concepts (learn next)
- [[Last Look]] , a complementary tool where the dealer can reject specific fills rather than widening the entire spread
- [[Internalization]] , using tiering data to decide which flow to net internally vs. externalize
- [[Single Dealer Platform]] , the technology through which tiered prices are delivered to clients
- [[ECN]] , anonymous venues where tiering is impossible, making adverse selection management harder
- [[Two Way Price]] , the output that tiering adjusts per client
- [[Flow Signals]] , aggregating tiered flow data to extract market direction signals

## Common misconceptions
1. **"Tiering is unfair to informed clients."** Tiering is rational pricing. An insurance company charges higher premiums to high risk drivers. A market maker charges wider spreads to high cost flow. The informed client is still getting a service (immediate execution), just at a price that reflects the cost of providing it.
2. **"Tiering is static."** Good tiering is dynamic. A corporate that suddenly starts trading around ECB meetings with perfect timing should get reclassified. A hedge fund that changes strategy may become less toxic. Weekly or daily recalibration is standard.
3. **"You can tier on an ECN."** On anonymous central limit order books ([[ECN]]), tiering is impossible because the market maker does not know who is on the other side. This is why dealers prefer [[Single Dealer Platform|SDP]] flow: they can see the client ID and price accordingly.
4. **"Wider tiers solve everything."** If a client's markout is negative 10 pips and I show a 12 pip spread, I might break even, but the client will simply stop trading with me. The flow goes to a competitor or an [[ECN]]. Tiering must balance profitability against losing the relationship.

## Sources
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- King, M., Osler, C., Rime, D. "Foreign Exchange Market Structure, Players, and Evolution," *Handbook of Exchange Rates*
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
