---
aliases: [spread trade, spread trading, relative value spread]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Spread Trade

## Definition
A spread trade is a simultaneous long and short position in 2 related contracts, designed to profit from a change in the price difference (the spread) rather than from the outright move of either leg. Types: calendar spreads (same commodity, different expiry), location spreads (same commodity, different delivery points), quality spreads (different grades), inter commodity spreads (different but related commodities like corn vs wheat), and product spreads ([[Crush Spread]], [[Crack Spread]]). Because the 2 legs partially offset, spread trading involves lower volatility, lower margin, and lower risk than outright positions. Trade off: profit potential per unit of capital is smaller, though the improved risk/reward often makes spreads more capital efficient.

## Why it matters (commodities and FX)
The majority of professional commodity trading is spread based, not flat price directional. Physical houses (Vitol, Trafigura, Glencore, Cargill), bank commodity desks, and sophisticated hedge funds trade relative value to isolate specific fundamental views and reduce exposure to broad market moves. A calendar spread expresses a view on near vs deferred supply without betting on absolute price. An inter commodity spread captures the relative supply/demand between 2 linked commodities. Exchange recognized spread margins are 20 to 50% of the sum of outright margins, improving capital efficiency. In FX, relative value trades between currency pairs serve an analogous function.

## Concrete example
**Concrete:** Trader believes US corn's [[Stocks to Use Ratio]] for the current crop year is tighter than the market prices. Buys the July/December corn spread (long July old crop, short December new crop) at $0.30/bu. Over 2 months, USDA cuts ending stocks twice, spread widens to $0.85/bu. Profit $0.55/bu = $2,750 per spread, on ~$400 initial margin. Return on margin ~688%. Counter case: trader sells the Brent/WTI spread at $4.00/bbl expecting the wide Atlantic basin premium to narrow. European refinery maintenance tightens Brent, spread widens to $7.50/bbl. Loss $3.50/bbl = $3,500 per spread. Lower margin requirements amplified the percentage loss.

**Simplified:** Buy one contract, sell a related contract. You profit from the price gap between them changing, not from prices going up or down. Lower volatility, lower margin, lower risk than betting on price direction. The 2 legs hedge each other's directional exposure. Most professional commodity trading is structured this way.

## Key mechanics and formulas
- **Spread types:**
  - Calendar (intra commodity): same commodity, different months (July/December corn)
  - Inter commodity: different commodities (corn/wheat, gold/silver, Brent/WTI)
  - Location: same commodity, different delivery points (Brent/Dubai, HH/TTF)
  - Product: input vs output ([[Crush Spread]], [[Crack Spread]])
- **Spread P&L:** P&L = Change in spread x Position size
- **Spread margin:** 20 to 50% of the sum of outright margins, reflecting exchange recognition of offsetting risk
- **Spread ratio:** Some inter commodity spreads require ratio adjustment (3:2:1 crack uses 3 crude, 2 gasoline, 1 heating oil)
- **Correlation and hedge ratio:** Spread risk depends on correlation between legs. Lower correlation = wider spread moves = more risk.

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
- **"Spread trades are risk free."** Lower risk than outright, not zero. Spreads move sharply during dislocations, structural shifts, or liquidity events. The 2020 WTI negative price event saw calendar spreads move by unprecedented amounts.
- **"Spreads always converge to fair value."** Some spreads are mean reverting, but structural changes (new pipelines, policy, demand regime) permanently shift the long term average. Mean reversion is a tendency, not a guarantee.
- **"Lower margin means lower dollar risk."** Lower margin = higher leverage on the spread. A $0.50/bu move on a $400 margin spread = 625% change in margin. Position sizing is critical.

## Sources
- CME Group, "Spread Trading in Commodity Markets"
- Commodity Trading Manual, Chicago Board of Trade
- "Trading and Hedging with Agricultural Futures and Options" by James B. Bittman
- "Commodity Price Dynamics: A Structural Approach" by Craig Pirrong
