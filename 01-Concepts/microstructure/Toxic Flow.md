---
aliases: [toxic flow, informed flow, toxic order flow]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Toxic Flow

## Definition
Toxic flow is client order flow that consistently predicts the price moving against the market maker who filled it. If every time a particular client buys from me the price subsequently rises, that client's flow is toxic to me. The term is directional: flow is toxic from the liquidity provider's perspective, not the client's. Toxic flow is the empirical manifestation of [[Adverse Selection]]. It is measured through [[Markout]] analysis, where persistently negative markouts indicate that the counterparty had better information at the time of the trade. Not all informed flow is intentionally predatory; some clients simply have better models, faster data, or closer proximity to physical markets.

## Why it matters (commodities and FX)
In FX dealing, identifying toxic flow is the difference between a profitable desk and a losing one. A bank streaming prices to 500 clients on its [[Single Dealer Platform]] might find that 10% of clients generate 80% of the adverse selection losses. In commodities, a broker on the LME might notice that a specific trading house consistently buys copper right before warehouse stock reports show drawdowns. The response is [[Client Tiering]]: widen spreads for toxic clients, tighten them for benign ones. Without flow toxicity measurement, a market maker is flying blind.

## Concrete example
I run an FX desk streaming EUR/USD prices to 200 institutional clients. I measure [[Markout|markouts]] at 1 second, 10 seconds, and 60 seconds for every fill.

**Identifying toxic flow:** Client A (a macro hedge fund) has an average 10 second markout of negative 3.2 pips across 500 trades this month. Every time they buy, EUR/USD tends to rise by 3.2 pips within 10 seconds. My average spread to this client is 1.5 pips. I am losing 3.2 minus 0.75 ([[Half Spread]]) = 2.45 pips per trade, or roughly $2,450 per 10 million trade. Over 500 trades at average 10 million notional, that is $1.225 million in losses per month.

**Win scenario (proper response):** I widen Client A's spread from 1.5 pips to 5 pips and reduce the size I show from 10 million to 2 million. Client A's fill rate drops, their markout against me stays similar, but my [[Half Spread]] now exceeds their information edge. Net: I break even or make small profit on their flow. Meanwhile, Client B (a corporate hedger) has a 10 second markout of +0.1 pips (random). I keep their spread tight at 0.8 pips and earn consistently.

**Fail scenario:** I ignore flow toxicity data and show the same 1.5 pip spread to all 200 clients. The 20 toxic clients generate $2 million in losses per month. The 180 benign clients generate $1.5 million in spread revenue. Net: I lose $500,000 per month because I failed to differentiate.

## Key mechanics and formulas
- **Toxicity score** = Average markout at horizon T for a given client or flow segment. More negative = more toxic
- **Break even spread for client i** = 2 x |Average markout_i at horizon T|. If Client A's markout is negative 3 pips, I need at least a 6 pip spread to break even
- **VPIN (Volume synchronized Probability of Informed Trading):** A metric that estimates the fraction of volume driven by informed traders. VPIN = |Volume_buy minus Volume_sell| / Total Volume, measured over volume buckets
- **Flow toxicity ratio** = Losses from toxic clients / Total spread revenue. If this exceeds 1, the desk is unprofitable
- **Skew adjustment:** When toxic flow is directional (always buying), skew the [[Two Way Price]] to make the ask more expensive and the bid more attractive

## Prerequisites
- [[Adverse Selection]]
- [[Markout]]
- [[Bid-Ask Spread]]
- [[Quote]]

## Related concepts (learn next)
- [[Client Tiering]] , the primary defense: charge toxic clients wider spreads
- [[Markout]] , the measurement tool that reveals which flow is toxic
- [[Last Look]] , allows rejecting trades that look toxic in the milliseconds after the fill request
- [[Sniping]] , a specific type of toxic flow that exploits [[Stale Quote|stale quotes]]
- [[Internalization]] , netting uninformed flow against itself to avoid sending it to toxic external venues
- [[Flow Signals]] , using aggregated flow data to detect informed trading in real time
- [[Market Impact]] , the observable price footprint of toxic flow hitting the book

## Common misconceptions
1. **"Toxic flow is illegal or unethical."** Toxic flow is simply informed trading. A macro fund with a better model for ECB policy is not doing anything wrong by trading on its view. The term "toxic" is from the market maker's perspective, not a moral judgment.
2. **"All high frequency flow is toxic."** Some HFT flow is benign. Retail aggregators, for example, send high frequency flow that has near zero markout because the underlying retail traders are uninformed. The speed of the flow does not determine its toxicity; the information content does.
3. **"I can eliminate toxic flow entirely."** Some adverse selection is unavoidable. Widening spreads too far drives away all flow, including profitable uninformed flow. The goal is to price toxic flow correctly (wide enough to compensate), not to eliminate it.
4. **"If a client loses money overall, their flow is not toxic."** A client can lose money on their portfolio while still generating toxic flow for the dealer. The client may be wrong on the macro trade but right on the 10 second horizon that matters for the market maker's inventory.

## Sources
- Easley, D., Lopez de Prado, M., O'Hara, M. "Flow Toxicity and Liquidity in a High Frequency World," *Review of Financial Studies*, 2012
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
