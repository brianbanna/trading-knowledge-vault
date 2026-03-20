---
aliases: [spread trade, spread trading, relative value spread]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Spread Trade

## Definition
A spread trade is a simultaneous long and short position in 2 related contracts, designed to profit from a change in the price difference (the spread) rather than from the outright directional move of either leg. Spreads come in several types: calendar spreads (same commodity, different expiry months), location spreads (same commodity, different delivery points), quality spreads (different grades of the same commodity), inter commodity spreads (different but related commodities such as corn vs. wheat), and product spreads ([[Crush Spread]], [[Crack Spread]]). Because the 2 legs partially offset each other, spread trading typically involves lower volatility, lower margin requirements, and lower risk than outright directional positions. The trade off is that the profit potential per unit of capital is usually smaller, though the improved risk/reward ratio often makes spreads more capital efficient.

## Why it matters (commodities and FX)
The majority of professional commodity trading is spread based rather than flat price directional. Physical trading houses (Vitol, Trafigura, Glencore, Cargill), bank commodity desks, and sophisticated hedge funds primarily trade relative value to isolate specific fundamental views and reduce exposure to broad market moves. A calendar spread expresses a view on near term versus deferred supply conditions without betting on the absolute price level. An inter commodity spread captures the relative supply/demand between 2 linked commodities. Exchange recognized spread margins are typically 20 to 50% of the sum of outright margins, significantly improving capital efficiency. In FX, relative value trades between currency pairs serve an analogous function.

## Concrete example
**Success case:** A trader believes US corn's [[Stocks to Use Ratio]] for the current crop year is tighter than the market prices. They buy the July/December corn spread (long July old crop, short December new crop) at $0.30/bu. Over the next 2 months, USDA cuts ending stocks twice, and the spread widens to $0.85/bu. Profit: $0.55/bu or $2,750 per spread, with initial margin of only ~$400 per spread. Return on margin: approximately 688%.

**Failure case:** A trader sells the Brent/WTI spread at $4.00/bbl, expecting the historically wide Atlantic basin premium to narrow. Instead, a European refinery maintenance season tightens Brent supply, and the spread widens to $7.50/bbl. Loss: $3.50/bbl or $3,500 per spread. Despite lower margin requirements, the percentage loss on capital is severe. The lesson: spreads are lower risk, not no risk, and can move sharply during structural shifts.

## Key mechanics and formulas
- **Spread types:**
  - Calendar (intra commodity): same commodity, different months (e.g., July/December corn)
  - Inter commodity: different commodities (e.g., corn/wheat, gold/silver, Brent/WTI)
  - Location: same commodity, different delivery points (e.g., Brent/Dubai, HH/TTF natural gas)
  - Product: input vs. output ([[Crush Spread]], [[Crack Spread]])
- **Spread P&L:** P&L = Change in spread x Position size
- **Spread margin:** Typically 20 to 50% of the sum of outright margins, reflecting the exchange's recognition of offsetting risk
- **Spread ratio:** Some inter commodity spreads require ratio adjustment (e.g., 3:2:1 crack spread uses 3 crude, 2 gasoline, 1 heating oil)
- **Correlation and hedge ratio:** Spread risk depends on the correlation between legs. Lower correlation = wider spread moves = more risk.

## Prerequisites
- [[Futures Contract]]
- [[Margin]]

## Related concepts (learn next)
- [[Old Crop New Crop]] is the most important calendar spread in agricultural markets.
- [[Crush Spread]] is the 3 legged product spread for soybeans into meal and oil.
- [[Contango Roll Cost]] is the spread between consecutive months that determines roll economics.
- [[Backwardation Roll Gain]] is earned by rolling through favorable calendar spreads.
- [[Basis Risk]] is the residual risk in a spread when the 2 legs do not move in perfect correlation.
- [[Delivery]] anchors calendar spreads to physical market conditions near expiry.
- [[COT Positioning]] data is available for some spread markets, revealing speculative crowding.
- [[Implied Volatility]] on spread options enables vol trading on relative value rather than outright direction.

## Common misconceptions
- **"Spread trades are risk free."** They are lower risk than outright positions, not zero risk. Spreads can move sharply during market dislocations, structural shifts, or liquidity events. The 2020 WTI negative price event saw calendar spreads move by unprecedented amounts.
- **"Spreads always converge to fair value."** Some spreads are mean reverting, but structural changes (new pipelines, policy shifts, demand regime changes) can permanently shift the long term average. Mean reversion is a tendency, not a guarantee.
- **"Lower margin means lower dollar risk."** Lower margin requirements mean higher leverage on the spread position. A $0.50/bu move on a $400 margin spread represents a 625% change in margin, making position sizing critical.

## Sources
- CME Group, "Spread Trading in Commodity Markets"
- Commodity Trading Manual, Chicago Board of Trade
- "Trading and Hedging with Agricultural Futures and Options" by James B. Bittman
- "Commodity Price Dynamics: A Structural Approach" by Craig Pirrong
