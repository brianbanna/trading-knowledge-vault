---
aliases: [toxic flow, informed flow, toxic order flow]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Toxic Flow

## Definition
Toxic flow is client order flow that consistently predicts price moving against the market maker who filled it. If every time a client buys from me the price rises, that client's flow is toxic to me. The term is directional: toxic from the liquidity provider's perspective, not the client's. Toxic flow is the empirical manifestation of [[Adverse Selection]]. Measured through [[Markout]] analysis, where persistently negative markouts indicate the counterparty had better information. Not all informed flow is intentionally predatory; some clients simply have better models, faster data, or closer proximity to physical markets.

## Why it matters (commodities and FX)
In FX dealing, identifying toxic flow separates profitable desks from losing ones. A bank streaming prices to 500 clients on its [[Single Dealer Platform]] might find that 10% of clients generate 80% of adverse selection losses. In commodities, an LME broker might notice a specific trading house consistently buys copper right before warehouse stock reports show drawdowns. The response is [[Client Tiering]]: widen spreads for toxic clients, tighten for benign ones. Without flow toxicity measurement, a market maker is flying blind.

## Concrete example

**Concrete:** FX desk streaming EUR/USD to 200 institutional clients. Measure [[Markout|markouts]] at 1s, 10s, 60s on every fill. Client A (macro hedge fund) has 10s markout of -3.2 pips across 500 trades this month. Every buy: EUR/USD rises 3.2 pips within 10s. Average spread to Client A: 1.5 pips. Losing 3.2 - 0.75 ([[Half Spread]]) = 2.45 pips/trade, ~$2,450 per 10M trade. Over 500 trades at avg 10M: $1.225M losses/month. Response: widen Client A spread to 5 pips, cut size to 2M. Fill rate drops, markout stays similar, but [[Half Spread]] now exceeds their information edge. Break even or small profit. Meanwhile Client B (corporate hedger) has +0.1 pip markout (random). Keep spread tight at 0.8 pips, earn consistently. Failure: ignore toxicity data, show 1.5 pips to all 200 clients. 20 toxic clients generate $2M losses/month, 180 benign generate $1.5M spread revenue. Net loss $500,000/month.

**Simplified:** Toxic flow is clients whose trades make money at your expense. Right after they trade, the price moves their way. Repeatedly. The fix is to charge them a wider spread that covers what they cost you. Sometimes they stop trading with you; that is fine if the alternative is bleeding money.

## Key mechanics and formulas
- **Toxicity score** = average markout at horizon T per client or segment. More negative = more toxic
- **Break even spread for client i** = 2 x |Avg markout_i at T|. Client A -3 pips: need 6 pip spread
- **VPIN:** estimates the fraction of volume driven by informed traders. VPIN = |Vol_buy - Vol_sell| / Total Volume measured over volume buckets
- **Flow toxicity ratio** = losses from toxic clients / total spread revenue. >1: desk is unprofitable
- **Skew adjustment:** when toxic flow is directional (always buying), skew the [[Two Way Price]] to make ask more expensive and bid more attractive

## Prerequisites
- [[Adverse Selection]]
- [[Markout]]
- [[Bid-Ask Spread]]
- [[Quote]]

## Related concepts (learn next)
- [[Client Tiering]] , primary defense: charge toxic clients wider spreads
- [[Markout]] , the measurement tool revealing which flow is toxic
- [[Last Look]] , allows rejecting trades that look toxic in ms after the request
- [[Sniping]] , a specific type of toxic flow exploiting [[Stale Quote|stale quotes]]
- [[Internalization]] , netting uninformed flow against itself to avoid sending it to toxic external venues
- [[Flow Signals]] , using aggregated flow data to detect informed trading in real time
- [[Market Impact]] , the observable price footprint of toxic flow

## Common misconceptions
1. **"Toxic flow is illegal or unethical."** Toxic flow is informed trading. A macro fund with a better ECB model does nothing wrong by trading on its view. The term is from the maker's perspective, not a moral judgment.
2. **"All HF flow is toxic."** Some HFT flow is benign. Retail aggregators send HF flow with near zero markout because underlying retail is uninformed. Speed does not determine toxicity; information content does.
3. **"I can eliminate toxic flow entirely."** Some AS is unavoidable. Widening too far drives away all flow including profitable uninformed flow. Goal: price toxic flow correctly, not eliminate it.
4. **"If a client loses money overall, their flow is not toxic."** A client can lose on their portfolio while still generating toxic flow for the dealer. They may be wrong on the macro trade but right on the 10s horizon that matters for the maker's inventory.

## Sources
- Easley, D., Lopez de Prado, M., O'Hara, M. "Flow Toxicity and Liquidity in a High Frequency World," *Review of Financial Studies*, 2012
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
