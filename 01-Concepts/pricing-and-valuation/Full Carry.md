---
aliases: [full carry, carry ceiling, contango ceiling, full carry ceiling]
tags:
  - "#quant"
  - "#microstructure"
date-added: "2026-07-15"
---

# Full Carry

## Definition

Full carry is the maximum contango a forward curve can sustain before it becomes profitable to arbitrage away: futures price = spot + storage cost + insurance + financing, with 0 [[Convenience Yield]]. It is easy to read full carry as just a number the [[Cost of Carry]] model outputs, a theoretical fair value. That undersells it. Full carry is a hard ceiling, enforced by a specific, executable trade, cash and carry arbitrage, buy spot, store it, sell the future, lock in the gap. Any time the market spread trades above that arithmetic, that trade is profitable near risk free, and capital flows into it until the spread is pushed back down to the ceiling. That enforcement mechanism, not historical convention, is what makes full carry hard rather than soft.

## Why it matters (commodities and FX)

For a spread trader, full carry answers a specific and recurring question: does this contango have room to widen, or is it pinned against the ceiling? Below full carry, a calendar spread can legitimately keep widening as new information (a tightening story easing, a storage build) pushes it toward the ceiling, and buying that spread has real asymmetry in its favor. At or near full carry, the picture inverts. There is little to no organic room left; the position's maximum realistic gain is whatever thin gap remains to the ceiling, capped by arbitrage, while the downside if the market snaps back toward [[Backwardation]] is the full width of the spread. Full carry is therefore not just a valuation reference, it is a risk/reward gate: it tells a trader when a "buy the contango" trade has stopped being a carry trade and started being a bet against arbitrageurs with better information and cheaper capital.

## Concrete example

**Concrete:** WTI Cushing, M1 (front) at $74.00/bbl, M2 (2 months out) at $75.20/bbl. Market spread = $1.20/bbl over 2 months. Cushing tank rental runs about $0.45/bbl/month; financing at 5% annual on $74.00 costs 74.00 × 0.05 × (2/12) ≈ $0.617/bbl over 2 months. Full carry for the 2 month gap ≈ (0.45 × 2) + 0.617 ≈ $1.517/bbl. The market spread of $1.20 sits below the $1.517 ceiling, about $0.32/bbl of room. A trader buying the spread here (long the carry) has a legitimate case: if inventories keep building and the spread grinds toward $1.45 to $1.50, that is normal convergence toward a still-unbreached ceiling, not an overshoot needing correction.

Now suppose the spread instead trades to $1.60/bbl, above the $1.517 ceiling. A trader who buys the spread here is not buying room, they are buying against arbitrageurs. Anyone with tank access can buy spot at $74.00, pay $1.517/bbl to store and finance it for 2 months, and sell M2 at $75.60 (= 74.00 + 1.60), netting 75.60 − 74.00 − 1.517 ≈ $0.083/bbl near riskless. At 100,000 bbl that is roughly $8,300 of near-certain profit, and it is exactly the flow (buy spot, sell deferred) that compresses the spread back toward $1.517. A spread trader entering long at $1.60 is competing for the last $0.08/bbl of that gap against professional arbitrage capital that captures it faster and cheaper, while a reversal toward backwardation, say a cold snap draws Cushing stocks and the spread swings to $0.50, costs $1.10/bbl. That asymmetry, tiny residual upside against full downside, is what "pinned against the ceiling" means in practice.

**Caveat:** the ceiling itself assumes storage is available at the quoted rate. When Cushing utilization runs above about 85%, tank rates spike nonlinearly (see [[Storage Economics]]), and above that, storage becomes unavailable at any price. That is what broke the ceiling in April 2020: it was not that the cost of carry arithmetic changed, it was that the arbitrage that enforces the ceiling, buy spot and store it, became physically impossible to execute at scale, and WTI M1 settled at −$37.63/bbl instead of converging to a full carry relationship with M2.

## Key mechanics and formulas

**Multiplicative (matches the general [[Cost of Carry]] model):**
`F_max(t,T) = S(t) × e^((r + c)(T−t))`

**Additive, short-dated approximation (grains, metals spreads measured in cents or dollars per unit):**
`Full Carry(T−t) = Storage cost rate × (T−t) + F × r × (T−t)`

Where F = front price, r = annual financing rate, c = storage cost rate (annualized % of spot), T−t = time between the 2 contracts.

**Why it is a hard ceiling and not a soft tendency:** a seasonal average (see [[Seasonality]]) is a statistical description, exceeded routinely in any given year with no mechanism forcing reversion. Full carry is different: crossing it makes a specific, low-risk trade (cash and carry arbitrage) profitable, and that trade is what pulls the spread back down, usually within days in liquid, storage-unconstrained markets. The ceiling is "hard" only conditional on 2 things holding: storage capacity is actually available, and arbitrage capital is free to act on it. Break either condition (storage full, capital constrained or unwilling) and the ceiling stops binding, which is exactly the mechanism behind extreme blowouts like negative WTI.

**What it means for a spread already sitting on the ceiling:** the only ways the spread can widen further from there are (1) storage cost rate rises (utilization climbing, see [[Storage Economics]]), or (2) financing rates rise. Continued forced selling, seasonal flow, or bullish sentiment on either leg cannot push the spread past full carry on their own, because any attempt to do so is met with arbitrage supply. This is the test to apply to a trade like [[Harvest Pressure]]: is the current spread below the ceiling (room to run) or already sitting on it (no organic room, only rate or capacity shifts can move it further)?

## Prerequisites
- [[Cost of Carry]]
- [[Contango]]
- [[Forward Curve]]
- [[Storage Economics]]

## Related concepts (learn next)
- [[Cost of Carry]] — full carry is the specific ceiling condition (0 convenience yield) inside the general cost of carry model.
- [[Contango]] — full carry is the upper bound on how steep contango can get before arbitrage caps it.
- [[Calendar Spread]] — the instrument used to express a view on whether a spread has room below full carry or is pinned against it.
- [[Storage Economics]] — storage capacity and utilization set the "c" in the formula and determine whether the ceiling can actually be enforced.
- [[Harvest Pressure]] — a concrete case of a spread being driven toward, and sometimes through, the full carry ceiling by concentrated forced selling.
- [[Cash and Carry Arbitrage]] — the actual trade that enforces the ceiling; full carry is the price at which this trade's profit hits 0.

## Common misconceptions

**"Full carry is a soft, statistical tendency, like a seasonal average."** It is not. It is enforced by a specific, executable, near riskless arbitrage trade, not by historical averaging. A spread trading above full carry gets mechanically compressed by capital chasing that arbitrage, typically within days in liquid, storage-unconstrained markets, which is a materially different (and faster, more reliable) mechanism than "reverting to the seasonal mean."

**"A contango spread has room to widen until the market normalizes."** The actual bound is the storage plus financing arithmetic, not a vague sense of what is normal. A spread already sitting at full carry has 0 organic room left regardless of how much further widening might feel intuitively justified by fundamentals; only a rise in storage rates or financing rates can move the ceiling itself.

**"Full carry is a fixed number."** It is not. The storage cost rate is convex in utilization (see [[Storage Economics]]), and the financing rate moves with the broader rate environment. The ceiling itself moves, mostly upward as storage fills or rates rise, which is why a spread can appear to "break through" a ceiling that was calculated weeks earlier but has since risen with it.

**"Buying a calendar spread near full carry is a good carry trade."** The risk/reward there is asymmetric against the buyer: the residual upside is capped at whatever thin gap remains to the ceiling, arbitraged away almost as fast as it appears, while the downside if the curve reverts toward backwardation is the full width of the spread. The trade only has favorable asymmetry when there is real room below the ceiling, not when it is already sitting on it.

## Sources
- Working, Holbrook, "The Theory of Price of Storage" (1949)
- Hull, Options, Futures, and Other Derivatives, Chapter 5
- CME Group: Cost of Carry Model for Commodity Futures
- Session notes, 2026-07-15
