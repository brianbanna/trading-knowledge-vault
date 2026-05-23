---
aliases: [adverse selection, information asymmetry, informed flow]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Adverse Selection

## Definition
Adverse selection is the risk of losing money because the counterparty knows more than I do at the trade moment. A posted [[Quote]] is a free option to anyone with superior information. Counterparties who have seen news, run a faster model, or detected a large order trade against me at a stale price. The name comes from insurance: those most eager to buy insurance are the ones most likely to claim. In trading, those most eager to hit my quote are the ones most likely to profit from it.

## Why it matters (commodities and FX)
In FX, adverse selection is the single largest cost for market makers. A dealer streaming on a [[Single Dealer Platform]] earns the [[Bid-Ask Spread]] on uninformed flow (corporates, tourists) but loses to informed flow (hedge funds, HFT). Net P&L depends on the mix. In commodities, a broker quoting a [[Two Way Price]] in Brent crude faces adverse selection from physical traders who know refinery outages or cargo movements first. Managing adverse selection through [[Client Tiering]], [[Last Look]], spread widening, and [[Markout]] analysis is the core skill of electronic market making.

## Concrete example

**Concrete:** EUR/USD market maker quotes 1.10000 / 1.10020, mid 1.10010. Corporate treasurer sells 10M EUR at 1.10000 to hedge receivables. Mid stays at 1.10010. 1 second [[Markout]] is +1 pip, earning the [[Half Spread]]. Same quote, different counterparty: systematic macro fund sells 10M EUR at 1.10000 after detecting a dovish ECB shift 200ms before the maker's model updated. Within 500ms, EUR/USD drops to 1.0990. 1 second markout is -10 pips. Maker bought at 1.10000, market is now 1.09900. Loss: 10M x 0.0010 = $10,000. The fund's information advantage made the quote a free put option.

**Simplified:** I post a buy price and a sell price. Someone who knows the market is about to drop sells to me at my buy price. Seconds later the market drops and I am stuck holding at the old level. They got a free option from me. Adverse selection is the cost of being on the wrong side of better informed counterparties.

## Key mechanics and formulas
- **Adverse selection cost** = expected [[Markout]] on informed trades. If 20% of flow is informed with -5 pip average markout: AS cost = 0.20 x 5 = 1.0 pip per trade
- **Break even spread** = 2 x AS cost per side. 1 pip AS per side needs minimum 2 pip spread
- **Glosten Milgrom:** Bid = E[Value | Sell], Ask = E[Value | Buy]. Informed traders shift the conditional expectation
- **Kyle lambda (λ):** price impact per unit order flow. Higher λ means more adverse selection. λ = σ_v / (σ_u x √n), σ_v = value vol, σ_u = noise trader volume, n = informed traders

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
- [[Internalization]] , netting uninformed flow internally to avoid leaking it
- [[Information Leakage]] , when my own order reveals information

## Common misconceptions

**"Adverse selection only comes from insiders."** Most adverse selection in modern markets comes from speed, not inside information. A hedge fund with 50 microsecond latency advantage can pick off a dealer whose model updates every 200ms.

**"Widening spreads eliminates adverse selection."** Wider spreads cut damage per trade but also drive away uninformed flow, concentrating the remainder in informed traders. AS share can rise as spreads widen. Optimal response is [[Client Tiering]], not blanket widening.

**"Central limit order books have no adverse selection."** Central [[ECN|limit order books]] have the highest adverse selection because all participants see the same prices. No [[Last Look]] or [[Client Tiering]] means informed and uninformed flow hit the same quotes.

## Sources
- Glosten, L. and Milgrom, P. "Bid, Ask and Transaction Prices in a Specialist Market with Heterogeneously Informed Traders," *Journal of Financial Economics*, 1985
- Kyle, A. "Continuous Auctions and Insider Trading," *Econometrica*, 1985
- Cartea, Jaimungal, Penalva. *Algorithmic and High-Frequency Trading*, Cambridge University Press
- Butz, M. and Oomen, R. "Internalisation by Electronic FX Spot Dealers," *Quantitative Finance*
