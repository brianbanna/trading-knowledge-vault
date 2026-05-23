---
aliases: [SDP, single dealer platform, bank platform]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Single Dealer Platform

## Definition
A Single Dealer Platform (SDP) is a proprietary electronic trading system operated by a single bank to stream prices and execute directly with its clients. Major examples: Barclays BARX, Citi Velocity, JPMorgan Execute, Deutsche Bank Autobahn, Goldman Marquee. Unlike [[ECN]]s where multiple participants post anonymous orders, an SDP shows one bank's prices to specific clients, customized by tier, relationship, and perceived [[toxicity]] of flow. SDPs incorporate [[last look]] windows, giving the bank the right to reject trades after the client clicks. The bank uses its own balance sheet to [[internalization|internalize]] trades, so the client's order may never reach the public market. SDPs handle 60 to 70% of all spot FX volume, the dominant venue in modern FX.

## Why it matters (commodities and FX)
SDPs are where most institutional FX execution happens. Understanding their mechanics is essential for evaluating execution quality. A commodity fund hedging USDCAD will execute through an SDP rather than an [[ECN]], getting a price that looks tighter than the ECN spread but comes with hidden costs ([[last look]] rejections, [[information leakage]]). Banks use SDP flow information to inform [[proprietary trading]] and [[market making]]. For systematic traders, the SDP vs ECN choice drives [[transaction cost analysis]] and [[alpha]] decay. In commodities, analogous proprietary platforms stream OTC prices on metals, energy, and agriculture.

## Concrete example

**Concrete:** A macro fund sells 100M EURUSD. On a top tier bank SDP the price shows 1.08522/1.08524 (0.2 pip spread), tighter than the 0.5 pip on [[EBS]]. The fund hits the bid at 1.08522. The bank applies a 200 ms [[last look]]. During those 200 ms, EURUSD drops 1 pip to 1.08512 against the bank. The bank rejects. The fund resubmits at 1.08512. Effective fill: 1.08512 vs the displayed 1.08522, costing 100,000 USD. A pension fund selling the same 100M in monthly rebalancing fills instantly: bank algorithms class the flow as non toxic and profitable to [[internalization|internalize]], matching it against a corporate buyer and pocketing the full spread without touching the external market.

**Simplified:** One bank's private trading screen for its clients. Tighter visible prices than public venues, but the bank reserves the right to back out after you click. Bank decides whether to internalize your order (match it against another client) or hedge it externally. The economics depend entirely on whether the bank thinks your flow is informed.

## Key mechanics and formulas
- **Price construction:** SDP price = ECN mid +/- (base spread / 2) + client skew + inventory skew
- **Client skew:** adjustment by perceived [[toxicity]] (informed = wider, passive = tighter)
- **Last look window:** 50 to 200 ms; allows rejection if price moves past threshold
- **Rejection rate:** rejected / attempted × 100; 5 to 30% common for aggressive clients
- **Internalization ratio:** internally matched volume / total SDP volume × 100; top banks internalize 60 to 80%
- **Effective spread including last look:** True cost = displayed spread + (rejection rate × average post rejection slippage)

## Prerequisites
- [[ECN]]
- [[Bid-Ask Spread]]
- [[Market Making]]
- [[Counterparty Risk]]

## Related concepts (learn next)
- [[Last Look]]: lets SDP operators reject trades after submission
- [[Internalization]]: banks match client orders internally rather than hedging externally
- [[ECN]]: anonymous alternative; SDPs and ECNs compete for flow
- [[Flow Signals]]: SDPs give banks privileged access to client flow information
- [[Top of Book]]: SDP prices tighter than ECN top but with hidden costs
- [[Transaction Cost Analysis]]: properly measuring SDP execution requires accounting for rejections and leakage

## Common misconceptions
1. **"Tighter displayed spread means cheaper execution."** SDP spreads look tighter than ECN spreads, but adding [[last look]] rejections, hold times, and information leakage often makes the all in cost higher. Compare effective spread, not displayed.
2. **"SDPs are just for small trades."** SDPs handle the majority of institutional FX volume including very large orders. Banks prefer SDP flow: client identity enables better risk management and internalization.
3. **"All banks' SDPs are equivalent."** Pricing, rejection rates, and internalization capability vary widely. A bank with diverse client base internalizes more and offers tighter prices than one with concentrated directional flow.

## Sources
- Moore, Schrimpf, Sushko, "Downsized FX Markets: Causes and Implications," BIS Quarterly Review (2016)
- Butz, Oomen, "Internalisation by Electronic FX Spot Dealers," Quantitative Finance (2019)
- Hagstromer, Norden, "The Diversity of High-Frequency Traders," Journal of Financial Markets (2013)
