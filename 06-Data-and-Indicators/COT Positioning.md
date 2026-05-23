---
aliases: [COT positioning, CFTC positioning, managed money positioning, speculative positioning]
tags:
  - "#quant"
  - "#macro"
date-added: "2026-03-20"
---

# COT Positioning

## Definition
COT positioning is the analysis of trader category positions disclosed in the CFTC Commitment of Traders report, published Friday based on the prior Tuesday's data. The report splits open interest by category: commercials (producer and consumer hedgers), managed money (hedge funds, CTAs, systematic funds), swap dealers (banks running OTC books), and other reportables. The focus for trading signals is managed money net position (longs minus shorts). Extreme net long = crowded bull trade vulnerable to liquidation. Extreme net short = washed out, vulnerable to short covering. Positioning is normalized as a percentile rank over a 1, 3, or 5 year window to account for changing open interest.

## Why it matters (commodities and FX)
COT positioning is the most widely used contrarian indicator in commodity and FX markets. Managed money net long above the 90th percentile (vs prior 3 years) marks a crowded market where a bearish catalyst triggers disproportionate selling. Net short below the 10th percentile signals a washed out market where a bullish catalyst sparks aggressive short covering. The signal is reliable at extremes and weak in the 25th to 75th percentile zone. Pairing positioning with fundamental analysis (is the position justified by the balance sheet or speculative excess?) sharpens timing.

## Concrete example
**Concrete:** September 2022, managed money net short CBOT corn reaches 120,000 contracts, the 5th percentile over 5 years. Trader reads this as extreme bearish crowding and buys 20 March corn lots at $6.50/bu. Over 6 weeks USDA tightens the corn balance sheet and exports surprise higher. Specs cover 80,000 contracts of shorts. Corn rallies to $6.95/bu. Gain: $0.45/bu × 5,000 bu × 20 lots = $45,000. The extreme positioning made the move mechanically larger once the catalyst arrived.

**Simplified:** Hedge funds tend to crowd into the same trade. The COT report shows you how crowded. When the crowd is extremely long, the trade is fragile; a piece of bad news triggers a stampede out. When the crowd is extremely short, the opposite. You sit on the other side and wait for the catalyst. Without a catalyst, extreme positioning can persist for months, so positioning alone is not a trade.

## Key mechanics and formulas
- **Managed money net = Long contracts − Short contracts**
- **Percentile ranking:** Percentile = (Current net − Min over lookback) / (Max − Min) × 100
- **Contrarian zones:**
  - >90th percentile: crowded long, watch for sell signal on negative catalyst
  - <10th percentile: crowded short, watch for buy signal on positive catalyst
  - 25th to 75th: neutral, low signal
- **Z score:** Z = (Current net − Mean) / Std. |Z| > 2 is statistically extreme.
- **Key markets:** WTI crude, Henry Hub gas, gold, copper, corn, soybeans, wheat, cocoa, coffee, sugar, EUR, JPY, AUD
- **Cocoa specific:** Cocoa OI is small (200k to 400k lots) vs WTI (2M+), so managed money positions are a larger share of the market with bigger price impact. During the 2024 to 2025 crisis, MM net long hit the 95th+ percentile while commercials were heavily short hedging production. COCOBOD forward defaults and producer margin calls amplified the rally. Watch the commercial/MM ratio more closely in cocoa than in liquid markets.
- **Data lag:** Tuesday measurement, Friday publication. The 3 day lag is negligible for position and swing horizons.

## Prerequisites
- [[Futures Contract]]
- [[Margin]]
- [[Spread Trade]]

## Related concepts (learn next)
- [[WASDE]] is a common catalyst that triggers positioning unwinds in agricultural futures.
- [[Implied Volatility]] compression often accompanies extreme positioning, then expands when the unwind begins.
- [[Stocks to Use Ratio]] gives fundamental context for whether extreme positioning is justified.
- [[Weather Premium]] buildup pushes managed money to extreme long in grains during the growing season.
- [[Grains]] are among the most useful markets for COT analysis due to seasonal positioning cycles.
- [[Backwardation Roll Gain]] is earned more reliably when commercial hedging is heavy and managed money is moderately long.
- [[Basis Risk]] exists between the aggregate COT signal and individual trader positions.
- [[Option]] markets complement COT: extreme futures positioning plus elevated put skew signals an imminent turn.

## Common misconceptions

**"Extreme positioning guarantees a reversal."** Crowded positions persist for weeks or months if the underlying driver stays intact. A catalyst is required; positioning alone is not.

**"COT data is too lagged."** The 3 day lag is negligible for weekly to monthly horizons. COT is strategic, not intraday.

**"Only managed money matters."** Commercial positioning provides essential context. When commercials are extreme, the physical side is heavily hedged, which can absorb speculative selling.

**"High open interest means bullish."** OI measures total positions outstanding, not direction. OI can grow in either direction depending on which category is adding.

## Sources
- CFTC, "Commitment of Traders: Explanatory Notes and Data"
- JP Morgan Commodities Research, "COT Positioning Analysis Framework"
- AQR, "Speculative Positioning and Commodity Returns"
- Sanders, D. and Irwin, S., "The Impact of Index and Swap Funds on Commodity Futures Markets," OECD Food, Agriculture and Fisheries Papers
