---
aliases: [SDP, single dealer platform, bank platform]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Single Dealer Platform

## Definition
A Single Dealer Platform (SDP) is a proprietary electronic trading system operated by a single bank to stream prices and execute trades directly with its clients. Major examples include Barclays BARX, Citi Velocity, JPMorgan Execute, Deutsche Bank Autobahn, and Goldman Sachs Marquee. Unlike [[ECN]]s where multiple participants post anonymous orders, an SDP shows one bank's prices to its specific clients, often customized by client tier, relationship, and perceived [[toxicity]] of flow. SDPs typically incorporate [[last look]] windows, giving the bank the right to reject trades after the client clicks. The bank uses its own balance sheet to [[internalization|internalize]] trades, meaning the client's order may never reach the public market. SDPs now handle approximately 60 to 70% of all spot FX volume, making them the dominant execution venue in modern FX markets.

## Why it matters (commodities and FX)
SDPs are where most institutional FX execution actually happens, and understanding their mechanics is essential for evaluating execution quality. A commodity fund hedging USDCAD exposure will typically execute through an SDP rather than an [[ECN]], receiving a price that may look tighter than the ECN spread but that comes with hidden costs ([[last look]] rejections, [[information leakage]] to the dealer). Banks use the flow information from SDPs to inform their own [[proprietary trading]] and [[market making]] strategies. For systematic traders, the choice between SDP and ECN execution affects both [[transaction cost analysis]] and [[alpha]] decay. In commodities, analogous structures exist where banks stream OTC prices on metals, energy, and agricultural products through proprietary platforms.

## Concrete example
A macro hedge fund wants to sell 100 million EURUSD. On the SDP of a top-tier bank, the displayed price is 1.08522/1.08524 (a 0.2 pip spread), tighter than the 0.5 pip spread on [[EBS]]. The fund hits the bid at 1.08522. The bank's system applies a 200 millisecond [[last look]] window. During those 200 milliseconds, the market moves 1 pip against the bank (EURUSD drops to 1.08512). The bank rejects the trade. The fund must re-submit at the new, lower price. Effective execution: 1.08512 instead of 1.08522, costing the fund 1 pip (100,000 USD on 100 million). In contrast, a pension fund selling the same amount as part of routine monthly rebalancing (uninformed flow) gets filled instantly because the bank's algorithms classify this flow as non-toxic and profitable to [[internalization|internalize]]. The bank matches the pension fund's sell against a corporate client's buy, never touching the external market and earning the full spread.

## Key mechanics and formulas
- **Price construction**: SDP price = ECN mid +/- (base spread / 2) + client skew + inventory skew
- **Client skew**: adjustment based on perceived [[toxicity]] (informed = wider, passive = tighter)
- **Last look window**: typically 50 to 200 milliseconds; allows rejection if price moved beyond a threshold
- **Rejection rate**: Rejection rate = (rejected trades / total attempted trades) x 100; rates of 5 to 30% are common for aggressive clients
- **Internalization ratio**: Internalization ratio = (internally matched volume / total SDP volume) x 100; top banks internalize 60 to 80% of flow
- **Effective spread including last look**: True cost = displayed spread + (rejection rate x average post-rejection slippage)

## Prerequisites
- [[ECN]]
- [[Bid-Ask Spread]]
- [[Market Making]]
- [[Counterparty Risk]]

## Related concepts (learn next)
- [[Last Look]]: the mechanism that allows SDP operators to reject trades after submission.
- [[Internalization]]: the process by which banks match client orders internally rather than hedging externally.
- [[ECN]]: the anonymous alternative venue; SDPs and ECNs compete for order flow.
- [[Flow Signals]]: SDPs give banks privileged access to client flow information.
- [[Top of Book]]: SDP prices may be tighter than ECN top-of-book but carry hidden costs.
- [[Transaction Cost Analysis]]: properly measuring SDP execution quality requires accounting for rejections and information leakage.

## Common misconceptions
1. **"Tighter displayed spread means cheaper execution"**: SDP spreads often look tighter than ECN spreads, but when accounting for [[last look]] rejections, hold times, and information leakage, the true all-in cost can be higher. Always compare effective spread, not displayed spread.
2. **"SDPs are just for small trades"**: SDPs handle the majority of institutional FX volume, including very large orders. Banks prefer SDP flow because it comes with client identity, allowing better risk management and internalization.
3. **"All banks' SDPs are equivalent"**: Pricing, rejection rates, and internalization capability vary enormously across banks. A bank with a large, diverse client base can internalize more and offer tighter prices than a bank with concentrated, directional flow.

## Sources
- Moore, Schrimpf, Sushko, "Downsized FX Markets: Causes and Implications," BIS Quarterly Review (2016)
- Butz, Oomen, "Internalisation by Electronic FX Spot Dealers," Quantitative Finance (2019)
- Hagstromer, Norden, "The Diversity of High-Frequency Traders," Journal of Financial Markets (2013)
