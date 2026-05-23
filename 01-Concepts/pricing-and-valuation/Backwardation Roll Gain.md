---
aliases: [backwardation roll gain, positive roll yield, roll return]
tags:
  - "#quant"
date-added: "2026-03-20"
---

# Backwardation Roll Gain

## Definition
Backwardation roll gain is the profit from rolling a long [[Futures Contract]] forward in a backwardated market, where the front month sits above the deferred. The trader sells the expiring contract at the higher price and buys the next month at the lower price, banking the difference. Positive [[roll yield]] is one of the most persistent return sources in commodity markets. Gorton and Rouwenhorst showed roll yield accounts for a substantial portion of long term futures returns, often exceeding spot appreciation. Backwardation arises when convenience yield exceeds cost of carry, which happens when inventories are low (measured by the [[Stocks to Use Ratio]]) and immediate supply is urgent.

## Why it matters (commodities and FX)
Systematic carry strategies in commodities harvest backwardation roll gains across a diversified portfolio. Backwardated commodities stay backwardated because supply tightness persists until new supply arrives. CTAs, risk parity funds, and commodity index strategies all weight roll yield as a primary factor. For individual traders, preferring backwardated longs and avoiding (or shorting) contangoed markets improves risk adjusted returns over multi year horizons. This is the commodity analogue to FX carry. Crude oil, certain base metals, and agricultural markets with low [[Stocks to Use Ratio]] most frequently sit in backwardation.

## Concrete example
**Concrete:** Brent front (June) at $84.00, second month (July) at $82.50: $1.50 backwardation. Trader rolls long from June to July, capturing $1.50/bbl ($1,500 per 1,000 bbl contract). Over 12 months with average $0.80 monthly backwardation, annualized roll gain ≈ $9.60/bbl, or 11.4% on an $84 base, on top of spot. Reverse case: long corn in August during mild backwardation ($0.05/bu monthly). October harvest floods the market, curve flips to $0.08/bu contango. Net over 5 months: $0.10/bu gained, $0.24/bu lost = −$0.14/bu. Backwardation flips after harvest.

**Simplified:** When the near contract is more expensive than the far contract, rolling forward locks in a profit. Sell high (the contract about to expire), buy low (the next one). Repeat each month. As long as the curve stays downward sloping, you keep collecting. The risk is that the curve flips. When supply arrives, the front contract drops below the deferred, and now rolling costs money instead of earning it.

## Key mechanics and formulas
- **Roll gain per period** = Front month price − Deferred month price (positive in backwardation)
- **Annualized roll yield** ≈ Average monthly backwardation × 12
- **Total return:** Futures return = Spot return + Roll yield + Collateral yield
- **Historical evidence:** Gorton/Rouwenhorst, AQR — backwardated commodities outperformed contangoed by 5 to 10% per year over multi decade samples
- **Carry signal:** Rank by roll yield monthly; long most backwardated, short most contangoed. Cross sectional carry Sharpe 0.4 to 0.7 historically.
- **Relationship to scarcity:** Backwardation = low inventory = high convenience yield = positive roll yield

## Prerequisites
- [[Futures Contract]]
- [[Spread Trade]]
- [[Stocks to Use Ratio]]

## Related concepts (learn next)
- [[Contango Roll Cost]] is the opposite: loss from rolling in contango.
- [[Spread Trade]] in calendar spreads directly expresses backwardation/contango economics.
- [[Stocks to Use Ratio]] determines whether a market sits in backwardation (low S/U) or contango (high S/U).
- [[Old Crop New Crop]] spread is a specific form when old crop trades above new.
- [[Delivery]] economics drive the theoretical limits of backwardation near expiry.
- [[Grains]] shift between regimes depending on the [[Crop Year]] balance sheet.
- [[COT Positioning]] shows managed money net long in backwardated markets, reinforcing structure.
- [[Basis Risk]] arises when a futures carry trade hedges a physical exposure tracking a different index.

## Common misconceptions
- **"Backwardation roll gain is guaranteed."** The curve flips with demand destruction, new supply, or inventory builds. Gain is only captured when the curve stays backwardated at roll time.
- **"You need to time the roll perfectly."** Gain is captured on every roll in a backwardated market. Consistency of exposure beats roll date precision.
- **"Roll yield is a free lunch."** Backwardated markets are tight. You bear the risk that supply disruptions persist. If the market loosens, spot and backwardation collapse together, correlating directional and carry losses.
- **"Backwardation means prices will fall."** Backwardation reflects current scarcity and high convenience yield. Spot can keep rising.

## Sources
- Gary Gorton and K. Geert Rouwenhorst, "Facts and Fantasies about Commodity Futures"
- AQR, "Carry" (working paper on cross asset carry strategies)
- CME Group, "Roll Yield and Commodity Returns"
- Erb, C. and Harvey, C., "The Strategic and Tactical Value of Commodity Futures"
