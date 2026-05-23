---
aliases: [internalization, flow internalization, internal matching]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Internalization

## Definition
Internalization is when a bank or dealer matches incoming client orders against other client orders on its own book rather than hedging in the external interbank market (like an [[ECN]]). When a bank gets a buy order from Client A and a sell from Client B in the same pair at roughly the same time, it crosses the orders internally, earning the full [[bid-ask spread]] without taking market risk and without contributing to [[price discovery]] on public venues. Top tier FX dealers internalize 60 to 80% of spot flow, so the vast majority of client trades never reach the public market. Internalization is the primary profit engine for large FX banks and the economic reason they invest in [[Single Dealer Platform]]s and diverse client bases. The practice is legal and generally beneficial to clients (tighter spreads), but reduces transparency and concentrates information in a few mega dealers.

## Why it matters (commodities and FX)
Internalization reshapes FX market structure. Most flow is absorbed internally by a handful of top banks (JP Morgan, Citi, UBS, Deutsche Bank), so volume visible on public [[ECN]]s is a fraction of total trading. Public order books no longer fully reflect true supply and demand. For commodity traders hedging FX, execution quality depends on which bank they use and whether that bank has offsetting flow. A bank with a diversified client base (corporates, real money, hedge funds, central banks) internalizes more efficiently and offers tighter prices. For systematic quant strategies, internalization changes [[market impact]] models because a large order to a high internalization dealer may move the public market less than the same order to an ECN.

## Concrete example

**Concrete:** Citi's FX desk receives in a 500 ms window: a pension fund sells EUR 80 million EUR/USD to rebalance into US bonds, a European corporate buys EUR 65 million to pay a USD invoice. Citi matches 65 million internally: pension sells at 1.08520 (bid), corporate buys at 1.08525 (offer); Citi captures 0.5 pip on 65 million (~$3,250). The remaining 15 million of the pension fund's order is hedged on [[EBS]] at 1.08518. Citi's externalization ratio: 19% (15 / 80). Hedging the full 80 million on EBS would have moved the market 2 to 3 pips, costing the pension fund significantly more. Pension fund benefits from lower impact; Citi benefits from spread revenue. If a hedge fund sends the same 80 million to a smaller bank with no offsetting flow, that bank must hedge externally, creating visible impact and worse fill.

**Simplified:** Banks see flow from many different clients. When two clients want to trade opposite directions at the same time, the bank just matches them internally and keeps the spread without hedging anything outside. Most large bank FX flow never reaches public venues. Clients get tighter prices and less market impact; the bank gets free spread income. The cost is that the public market becomes a smaller and less informative slice of total flow.

## Key mechanics and formulas
- **Internalization ratio**: (internally matched volume / total volume) × 100
- **Spread capture**: profit per internalized trade = (ask − bid) × notional / 2 (both sides matched)
- **Residual risk**: total client flow − internalized flow; residual must be hedged externally
- **Inventory half-life**: average time a dealer holds unmatched inventory before hedging; 30 seconds to 5 minutes for major pairs
- **Optimal client mix**: maximum internalization when client base is diverse (directional hedge funds offset by non directional corporates and real money)
- **Market impact reduction**: external impact is proportional to externalized flow, not total flow. Impact = f(externalized volume, market depth)

## Prerequisites
- [[Single Dealer Platform]]
- [[Market Making]]
- [[Bid-Ask Spread]]
- [[ECN]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: venue through which banks attract client flow for internalization.
- [[Last Look]]: helps dealers manage risk on flow they plan to internalize.
- [[ECN]]: public venue that handles externalized residual flow.
- [[Flow Signals]]: internalized flow gives banks information about aggregate positioning without revealing it.
- [[Top of Book]]: public top of book on ECNs reflects only externalized flow.
- [[Depth of Book]]: ECN depth has declined as internalization rises, raising fragility concerns.
- [[Price Discovery]]: internalization reduces information flowing into public price formation.

## Common misconceptions

**"Internalization is bad for clients."** Usually benefits clients via lower [[market impact]] and tighter spreads. The concern is systemic: too much internalization degrades public price discovery and creates fragility in stress periods when dealers stop internalizing.

**"Any bank can internalize effectively."** Requires a large, diverse client base and sophisticated technology. Smaller banks with concentrated flow cannot internalize meaningfully and must hedge externally.

**"Internalized flow has zero market impact."** The specific trade is invisible externally, but the bank's residual hedging and subsequent inventory management still affect the market. Information the bank gains also informs its own market making.

## Sources
- Butz, Oomen, "Internalisation by Electronic FX Spot Dealers," Quantitative Finance (2019)
- Moore, Schrimpf, Sushko, "Downsized FX Markets: Causes and Implications," BIS Quarterly Review (2016)
- Bank for International Settlements, "Monitoring of Fast-Paced Electronic Markets" (2018)
