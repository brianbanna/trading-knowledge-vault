---
aliases: [contango roll cost, roll cost, negative roll yield, roll drag]
tags:
  - "#energy/crude"
  - "#quant"
date-added: "2026-03-20"
---

# Contango Roll Cost

## Definition
Contango roll cost is the loss from rolling a long [[Futures Contract]] forward in a contango market, where deferred months sit above nearby months. To maintain continuous exposure, the trader sells the expiring contract at the lower price and buys the next at the higher price, paying the difference each roll. This "roll drag" can cost 5 to 15% of portfolio value per year in steeply contangoed markets. It is the dominant hidden cost for commodity ETFs (USO) and index funds that mechanically roll positions. Roll cost is the negative form of [[roll yield]] and the mathematical opposite of [[Backwardation Roll Gain]]. Contango reflects storage costs, financing, and insurance (cost of carry), and prevails when inventory is ample and immediate supply is not urgent.

## Why it matters (commodities and FX)
Contango roll cost is the hidden tax on passive long commodity exposure that many investors miss. A commodity ETF buyer in a contango market can lose money even with rising spot prices, because cumulative roll drag erodes returns faster than spot appreciates. In 2014 to 2016, with crude in steep contango ($1 to $2/bbl per month), USO dramatically underperformed spot WTI. For systematic commodity strategies, understanding roll costs is essential to determine whether a carry trade (short contango) or momentum trade (potentially long contango) is net profitable after roll. The level of contango is also a signal: steep contango indicates ample supply and storage capacity; narrow contango or [[Backwardation Roll Gain|backwardation]] signals tightness.

## Concrete example
**Concrete:** 2015 WTI in $1.50/bbl per month contango. Systematic trader avoids passive long exposure and shorts the front month WTI calendar spread (sells front, buys deferred), earning contango as income. Over 6 months, cumulative roll = ~$8/bbl, or $8,000 per spread on ~$50/bbl base. Reverse case: investor buys $100K of crude ETF January 2015 at $48 spot. By December, spot rises to $50 (+4%). ETF returns −12% because average monthly roll cost of $1.30/bbl accumulates to ~$15/bbl drag. Investor loses $12K despite rising spot. In steep contango, roll cost overwhelms spot appreciation.

**Simplified:** When the next month is more expensive than the current one, rolling forward means selling low and buying high. You pay the gap every month. Even if spot prices climb, the roll bleeds money faster than spot earns it. The cleanest way to see this is a commodity ETF: spot can be up 5% on the year and the fund down 10%, because every month the manager pays the contango to maintain exposure.

## Key mechanics and formulas
- **Roll cost per period** = Deferred month price − Front month price (positive in contango, a cost for longs)
- **Annualized roll cost** ≈ Average monthly contango × 12
- **Roll yield = −Roll cost.** In contango, roll yield is negative.
- **ETF total return** ≈ Spot return + Roll yield + Collateral yield. Deeply negative roll yield → ETF loses while spot rises.
- **Cost of carry relationship:** Contango ≈ Storage + Financing + Insurance − Convenience yield. When convenience yield is low, contango = full carry.
- **Full carry** = (Risk free rate + Storage cost) × Spot × Time. Above full carry, cash and carry arb opens (buy spot, store, sell deferred).

## Prerequisites
- [[Futures Contract]]
- [[Delivery]]
- [[Spread Trade]]

## Related concepts (learn next)
- [[Backwardation Roll Gain]] is the opposite: profit from rolling in a backwardated market.
- [[Spread Trade]] in calendar spreads directly expresses contango/backwardation economics.
- [[Stocks to Use Ratio]] determines whether the curve is contango (high S/U) or backwardation (low S/U).
- [[Delivery]] and storage economics at the delivery point set theoretical maximum contango.
- [[Grains]] in surplus years sit in contango reflecting cost of storing between crop years.
- [[Old Crop New Crop]] spread in contango signals expected tightness ahead.
- [[Margin]] is not directly affected by contango, but the roll briefly doubles margin exposure.
- [[Basis Risk]] between ETF roll date and optimal roll timing creates tracking error.

## Common misconceptions
- **"The roll cost is small and can be ignored."** In steep contango, roll costs consume 10 to 20% of capital annually. Over multi year horizons, cumulative drag is often the dominant factor in commodity returns.
- **"All commodity ETFs have the same roll cost."** ETFs with different roll schedules (monthly, quarterly), contract selection (front vs optimized deferred), and roll periods incur different costs. "Smart roll" minimizes drag but cannot eliminate it in contango.
- **"You can avoid roll costs by holding to delivery."** Only works if you take physical delivery, which most financial investors cannot. Storage and logistics costs are what created the contango.
- **"Contango means the market expects higher prices."** Contango primarily reflects cost of carry, not direction. A contango market can see spot fall even with an upward sloping curve.

## Sources
- Gary Gorton and K. Geert Rouwenhorst, "Facts and Fantasies about Commodity Futures"
- AQR, "The Role of Carry in Commodity Returns"
- CME Group, "Understanding Roll Yield in Commodity Markets"
- Erb, C. and Harvey, C., "The Strategic and Tactical Value of Commodity Futures"
