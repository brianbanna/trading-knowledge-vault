---
aliases: [internalization, flow internalization, internal matching]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Internalization

## Definition
Internalization is the practice where a bank or dealer matches incoming client orders against other client orders on its own book, rather than hedging in the external interbank market (such as an [[ECN]]). When a bank receives a buy order from Client A and a sell order from Client B in the same currency pair at roughly the same time, it can cross the 2 orders internally, earning the full [[bid-ask spread]] without taking market risk and without contributing to [[price discovery]] on public venues. Top-tier FX dealers internalize 60 to 80% of their spot flow, meaning the vast majority of client trades never reach the public market. Internalization is the primary profit engine for large FX banks and is the key economic reason they invest in building [[Single Dealer Platform]]s and attracting diverse client bases. The practice is legal and generally beneficial to clients (tighter spreads), but it reduces transparency and concentrates information with a small number of mega-dealers.

## Why it matters (commodities and FX)
Internalization reshapes the entire FX market structure. Because most flow is absorbed internally by a handful of top banks (JP Morgan, Citi, UBS, Deutsche Bank, and others), the volume visible on public [[ECN]]s is only a fraction of total trading. This means that public order books no longer fully reflect true supply and demand. For commodity traders hedging in FX, internalization means that execution quality depends heavily on which bank they use and whether that bank has sufficient offsetting flow to match their trades internally. A bank with a diversified client base (corporates, real money, hedge funds, central banks) can internalize more efficiently and offer tighter prices. For systematic quant strategies, internalization affects [[market impact]] models because a large order sent to a high-internalization dealer may move the public market less than the same order sent to an ECN.

## Concrete example
Citi's FX desk receives the following flow within a 500 millisecond window: a pension fund sells 80 million EURUSD to rebalance into US bonds, and a European corporate buys 65 million EURUSD to pay a USD invoice. Citi matches 65 million internally: the pension fund sells at 1.08520 (the bid) and the corporate buys at 1.08525 (the offer), giving Citi a 0.5 pip spread profit on 65 million (approximately $3,250). The remaining 15 million of the pension fund's sell order is hedged on [[EBS]] at 1.08518. Citi's externalization ratio for this flow is only 19% (15 / 80). If Citi had hedged the full 80 million on EBS, the trade would have moved the market 2 to 3 pips, costing the pension fund significantly more. The pension fund benefits from lower market impact; Citi benefits from the spread revenue. However, if a hedge fund sends the same 80 million sell to a smaller bank with no offsetting flow, that bank must hedge externally, creating visible market impact and a worse fill.

## Key mechanics and formulas
- **Internalization ratio**: Internalization ratio = (internally matched volume / total volume handled) x 100
- **Spread capture**: Profit per internalized trade = (ask price - bid price) x notional / 2 (when both sides are matched)
- **Residual risk**: Residual = total client flow - internalized flow; this residual must be hedged externally
- **Inventory half-life**: the average time a dealer holds unmatched inventory before hedging; typically 30 seconds to 5 minutes for major pairs
- **Optimal client mix**: Maximum internalization occurs when client base includes diverse flow types (directional hedge funds offset by non-directional corporates and real money)
- **Market impact reduction**: External market impact is proportional to externalized flow, not total flow. Impact = f(externalized volume, market depth)

## Prerequisites
- [[Single Dealer Platform]]
- [[Market Making]]
- [[Bid-Ask Spread]]
- [[ECN]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: the venue through which banks attract client flow for internalization.
- [[Last Look]]: helps dealers manage risk on flow they intend to internalize; rejected trades are not internalized.
- [[ECN]]: the public venue that handles externalized (non-internalized) residual flow.
- [[Flow Signals]]: internalized flow gives banks information about aggregate client positioning without revealing it to the market.
- [[Top of Book]]: public top-of-book on ECNs reflects only externalized flow, not the full picture.
- [[Depth of Book]]: ECN depth has declined as internalization has increased, raising concerns about market fragility.
- [[Price Discovery]]: internalization reduces the amount of information flowing into public price formation.

## Common misconceptions
1. **"Internalization is bad for clients"**: In most cases, internalization benefits clients by reducing [[market impact]] and enabling tighter spreads. The concern is systemic: if too much flow is internalized, public price discovery degrades and markets become fragile in stress periods when dealers stop internalizing.
2. **"Any bank can internalize effectively"**: Internalization requires a large, diverse client base and sophisticated technology. Smaller banks with concentrated client flow (e.g., all hedge fund flow going the same direction) cannot internalize meaningfully and must hedge externally.
3. **"Internalized flow has zero market impact"**: While the specific trade is not visible externally, the bank's residual hedging and subsequent inventory management still affect the market. Additionally, the information the bank gains from internalized flow informs its own market-making and trading decisions.

## Sources
- Butz, Oomen, "Internalisation by Electronic FX Spot Dealers," Quantitative Finance (2019)
- Moore, Schrimpf, Sushko, "Downsized FX Markets: Causes and Implications," BIS Quarterly Review (2016)
- Bank for International Settlements, "Monitoring of Fast-Paced Electronic Markets" (2018)
