---
aliases: [contango roll cost, roll cost, negative roll yield, roll drag]
tags:
  - "#energy/crude"
  - "#quant"
date-added: "2026-03-20"
---

# Contango Roll Cost

## Definition
Contango roll cost is the loss incurred when rolling a long [[Futures Contract]] position forward in a contango market, where deferred month prices are higher than nearby month prices. To maintain continuous exposure, a trader must sell the expiring front month contract (at a lower price) and buy the next month contract (at a higher price), paying the difference each time they roll. This "roll drag" can cost 5 to 15% of portfolio value per year in steeply contango markets. It is the dominant hidden cost for commodity ETFs (like the United States Oil Fund, USO) and index funds that mechanically roll positions each month. The roll cost is the negative form of [[roll yield]] and is mathematically the opposite of the [[Backwardation Roll Gain]]. Contango reflects the market's pricing of storage costs, financing costs, and insurance (collectively the cost of carry), and it tends to prevail when inventory is ample and there is no urgency for immediate supply.

## Why it matters (commodities and FX)
Contango roll cost is the hidden tax on passive long commodity exposure that many investors do not fully appreciate. An investor who buys a commodity ETF in a contango market can lose money even if the spot price rises, because the cumulative roll drag erodes returns faster than spot appreciates. During 2014 to 2016, when crude oil was in steep contango (often $1 to $2/bbl per month), the USO ETF dramatically underperformed spot WTI. For systematic commodity strategies, understanding roll costs is essential for determining whether a carry trade (short contango markets) or momentum trade (potentially long contango markets) is net profitable after roll. The level of contango is also a signal about market conditions: steep contango indicates ample supply and storage capacity, while narrow contango or [[Backwardation Roll Gain|backwardation]] signals tightness.

## Concrete example
**Success case (avoiding the cost):** In 2015, WTI was in $1.50/bbl per month contango. A systematic trader avoided passive long exposure and instead shorted the front month WTI calendar spread (sold front, bought deferred), effectively earning the contango as income. Over 6 months, the cumulative roll earned approximately $8/bbl, or $8,000 per spread on a ~$50/bbl base price. This "carry" strategy profited from the contango structure without taking directional risk.

**Failure case (paying the cost):** An investor bought $100,000 of a crude oil ETF in January 2015 when WTI spot was $48/bbl. By December 2015, WTI spot had risen to $50/bbl (a 4% gain). However, the ETF returned negative 12% because the average monthly roll cost of $1.30/bbl accumulated to ~$15/bbl of drag over the year. The investor lost $12,000 despite spot prices rising. The lesson: in steep contango, the roll cost can completely overwhelm spot price appreciation, making passive long commodity exposure a losing proposition.

## Key mechanics and formulas
- **Roll cost per period = Deferred month price - Front month price** (positive in contango, representing a cost for longs)
- **Annualized roll cost ~ Average monthly contango x 12** (approximate, assumes constant roll frequency)
- **Roll yield = Negative roll cost.** In contango, roll yield is negative.
- **ETF total return ~ Spot return + Roll yield + Collateral yield.** When roll yield is deeply negative, the ETF can lose money even as spot rises.
- **Cost of carry relationship:** Contango ~ Storage cost + Financing cost + Insurance - Convenience yield. When convenience yield is low (ample supply), contango equals full carry.
- **Full carry = (Risk free rate + Storage cost) x Spot price x Time.** If contango exceeds full carry, a cash and carry arbitrage opportunity exists (buy spot, store, sell deferred futures).

## Prerequisites
- [[Futures Contract]]
- [[Delivery]]
- [[Spread Trade]]

## Related concepts (learn next)
- [[Backwardation Roll Gain]] is the opposite effect: profit from rolling in a backwardated market where front month trades above deferred.
- [[Spread Trade]] in calendar spreads is the direct expression of contango/backwardation and roll economics.
- [[Stocks to Use Ratio]] in agricultural markets determines whether the curve is in contango (high S/U) or backwardation (low S/U).
- [[Delivery]] and storage economics at the delivery point determine the theoretical maximum contango.
- [[Grains]] in surplus years exhibit contango reflecting the cost of storing grain between crop years.
- [[Old Crop New Crop]] spread in contango indicates that new crop is more expensive, signaling expected tightness ahead.
- [[Margin]] is not directly affected by contango, but the roll process creates a brief period of doubled margin exposure.
- [[Basis Risk]] between the roll date of an ETF and the actual optimal roll timing creates tracking error.

## Common misconceptions
- **"The roll cost is small and can be ignored."** In steep contango, roll costs can consume 10 to 20% of capital annually. Over multi year holding periods, cumulative roll drag is often the dominant factor in commodity investment returns, exceeding spot price moves.
- **"All commodity ETFs have the same roll cost."** ETFs with different roll schedules (monthly, quarterly), different contract selection (front month, optimized deferred month), and different roll periods incur different costs. "Smart roll" strategies attempt to minimize roll drag but cannot eliminate it in contango.
- **"You can avoid roll costs by holding futures to delivery."** This only works if you can and want to take physical delivery, which most financial investors cannot. Even for those who can, the storage and logistics costs are what created the contango in the first place.
- **"Contango means the market expects higher prices."** Contango primarily reflects the cost of carry (storage, financing), not a directional forecast. A contango market can see spot prices fall even as the curve slopes upward.

## Sources
- Gary Gorton and K. Geert Rouwenhorst, "Facts and Fantasies about Commodity Futures"
- AQR, "The Role of Carry in Commodity Returns"
- CME Group, "Understanding Roll Yield in Commodity Markets"
- Erb, C. and Harvey, C., "The Strategic and Tactical Value of Commodity Futures"
