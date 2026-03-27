---
aliases: [adverse selection, information asymmetry, informed flow]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Adverse Selection

## Definition
Adverse selection is the risk of losing money because the counterparty knows more than I do at the moment of the trade. When I post a [[Quote]], I am offering a free option to anyone with superior information. If the counterparty has seen news, run a faster model, or detected a large order before I have, they will trade against me at a price that is already stale. The name comes from insurance: the people most eager to buy insurance are the ones most likely to claim. In trading, the counterparties most eager to hit my quote are the ones most likely to profit from it.

## Why it matters (commodities and FX)
In FX, adverse selection is the single largest cost for market makers. A dealer streaming prices on a [[Single Dealer Platform]] earns the [[Bid-Ask Spread]] on uninformed flow (corporate hedgers, tourists) but loses to informed flow (hedge fund algorithms, high frequency traders). The net P&L depends on the mix. In commodities, a broker quoting a [[Two Way Price]] in Brent crude faces adverse selection from physical traders who know refinery outages or cargo movements before the market. Managing adverse selection through [[Client Tiering]], [[Last Look]], spread widening, and [[Markout]] analysis is the core skill of electronic market making.

## Concrete example
I am making markets in EUR/USD. My quote is 1.10000 / 1.10020. My model says the mid is 1.10010.

**Win scenario (uninformed flow):** A corporate treasurer sells 10 million EUR at my 1.10000 bid to hedge receivables. The mid stays at 1.10010. My 1 second [[Markout]] is +1 pip. The treasurer had no information about direction; they simply needed to convert EUR to USD. I earned the [[Half Spread]].

**Fail scenario (informed flow):** A systematic macro fund sells 10 million EUR at my 1.10000 bid. They have detected a dovish shift in ECB communication 200 milliseconds before my model updated. Within 500 milliseconds, EUR/USD drops to 1.0990. My 1 second markout is negative 10 pips. I bought at 1.10000 and the market is now 1.09900. Loss: 10 million x 0.0010 = $10,000. The fund's information advantage made my quote a free put option for them.

## Key mechanics and formulas
- **Adverse selection cost** = Expected [[Markout]] on informed trades. If 20% of my flow is informed and the average informed markout is negative 5 pips, then: AS cost = 0.20 x 5 = 1.0 pip per trade on average
- **Break even spread** = 2 x Adverse Selection cost per side. If AS costs 1 pip per side, I need at least a 2 pip spread to break even
- **Glosten Milgrom model:** The spread exists because of adverse selection. The market maker sets Bid = E[Value | Sell] and Ask = E[Value | Buy]. Informed traders cause the conditional expectation to shift
- **Kyle lambda (λ):** Measures the price impact per unit of order flow. Higher λ means more adverse selection in the market. λ = σ_v / (σ_u x √n), where σ_v is value volatility, σ_u is noise trader volume, n is number of informed traders

## Prerequisites
- [[Bid-Ask Spread]]
- [[Quote]]
- [[Mid Price]]
- [[Liquidity]]

## Related concepts (learn next)
- [[Toxic Flow]] , the practical label for persistently adversely selecting order flow
- [[Markout]] , the empirical tool for measuring adverse selection after the fact
- [[Client Tiering]] , the main defense against adverse selection in OTC markets
- [[Last Look]] , an FX mechanism that lets dealers reject adversely selecting fills
- [[Sniping]] , a specific form of adverse selection where a fast trader picks off [[Stale Quote|stale quotes]]
- [[Market Impact]] , the footprint that informed trading leaves in the order book
- [[Internalization]] , netting uninformed flow internally to avoid leaking it to the adversely selecting external market
- [[Information Leakage]] , when my own order reveals information that causes adverse selection against me

## Common misconceptions
1. **"Adverse selection only comes from insiders."** Most adverse selection in modern markets comes from speed, not inside information. A hedge fund with a 50 microsecond latency advantage can adversely select a dealer whose model updates every 200 milliseconds. No inside information is needed.
2. **"Widening spreads eliminates adverse selection."** Wider spreads reduce the damage per trade but also drive away uninformed flow, concentrating the remaining flow in informed traders. The share of adverse selection can actually increase as spreads widen. The optimal response is [[Client Tiering]], not blanket widening.
3. **"If I use a central limit order book, there is no adverse selection."** Central [[ECN|limit order books]] have the highest adverse selection because all participants see the same prices. The lack of [[Last Look]] or [[Client Tiering]] means informed and uninformed flow hit the same quotes.

## Sources
- Glosten, L. and Milgrom, P. "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*, 1985
- Kyle, A. "Continuous Auctions and Insider Trading," *Econometrica*, 1985
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
