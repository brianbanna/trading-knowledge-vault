---
aliases: [freight rate risk, freight risk, freight price risk, ocean freight risk]
tags:
  - "#risk"
  - "#freight"
date-added: "2026-06-17"
---

# Freight Rate Risk

## Definition
Freight rate risk is the exposure of your profit and loss to changes in the price of moving cargo by sea, quoted as USD per tonne for dry bulk or as Worldscale points for tankers. Think of it like the cost of a delivery truck for a online order, except the truck price can double in a week and you have already promised to ship the goods. Anyone who will receive freight income is structurally long freight, meaning they profit when rates rise: shipowners, operators with open ships, and anyone short tonnage. Anyone who must pay to move cargo is structurally short freight, meaning they lose when rates rise: charterers, cargo owners, and commodity traders running inter regional arbitrage whose margin is the spread minus the cost of transport. Technically the exposure is the partial derivative of P&L with respect to the freight rate, scaled by the tonnage committed and the duration of that commitment.

## Why it matters (commodities and FX)
Freight is one of the most volatile inputs in physical commodity trading and it is the gating variable that decides whether an arbitrage clears. In [[Location Arbitrage]] and [[EFS]] economics the trade only works if the commodity price spread between two regions exceeds the full cost of transport. A freight spike can close an arb window even when the underlying commodity spread still looks attractive on screen, and the reverse hands a windfall to whoever locked transport early. For a shipowner the symmetry is brutal: revenue collapses when rates fall while OPEX and crew cost stays fixed, so the entire business is a long freight position. Freight also feeds back into the macro chain, because physical flows priced by freight drive futures basis and even commodity currencies like AUD, so ignoring it is not an option even for paper traders.

## Concrete example
**Concrete:** A trader sees crude cheaper on the US Gulf than in China and books a WTI to China arbitrage. The gross commodity spread is 6.00 USD/bbl. After insurance of 0.30 USD/bbl and port and canal costs of 0.20 USD/bbl, the trade needs voyage freight below 5.50 USD/bbl to clear, and the trader models freight at 5.00 USD/bbl, leaving a 0.50 USD/bbl margin on a 2,000,000 barrel VLCC cargo, that is 1,000,000 USD of expected profit. The trader commits the cargo but does not fix the ship immediately. Over the next 2 weeks the VLCC market tightens and the freight equivalent jumps to 7.00 USD/bbl. The arb now costs 7.00 plus 0.50 in other costs against a 6.00 spread, a loss of 1.50 USD/bbl, or 3,000,000 USD on the committed cargo. Now the hedged case. Suppose at trade inception the trader had sold freight exposure by buying the relevant tanker route forward via a [[Forward Freight Agreement]] at the equivalent of 5.00 USD/bbl. When physical freight rises to 7.00, the FFA settles in the trader's favor by roughly 2.00 USD/bbl, about 4,000,000 USD, offsetting the higher physical fixture and restoring the trade close to its planned 0.50 USD/bbl margin. What remains is [[Freight Basis Risk]]: the FFA settles against a Baltic index route while the actual fixture is a specific ship on a specific date, so the offset is imperfect and a residual of perhaps 0.10 to 0.30 USD/bbl can persist.

**Simplified:** You can ship oil from A to B for a 6 USD per barrel price gap, but only if the boat costs less than about 5.50. You promised the cargo at a planned boat cost of 5. The boat then costs 7, so your 1 million dollar profit turns into a 3 million dollar loss. If you had locked the boat price at 5 ahead of time with a paper freight contract, the paper gain pays for the dearer boat and you keep your profit, minus a small slippage because the paper contract tracks an average route, not your exact ship.

## Key mechanics and formulas
`freight_pnl = position_in_tonnes * rate_change` where `position_in_tonnes` is signed (positive if long freight, negative if short) and `rate_change` is new rate minus old rate in USD per tonne. A long position gains when the rate rises.

`arb_clears if commodity_spread > freight + insurance + port_costs + canal_costs` where all terms are in the same per unit basis (USD per barrel or USD per tonne). The trade only books when the left side exceeds the right.

`ffa_lots = (tonnes / lot_size) * hedge_ratio` where `lot_size` is the contract size of the chosen FFA route (often 1,000 tonnes or 1 day depending on the contract), and `hedge_ratio` is the regression beta between your physical route and the index route, less than 1 when correlation is imperfect. Sizing lots without the beta adjustment over hedges or under hedges.

`var = position_value * rate_volatility * z_score * sqrt(holding_days)` is the rough single factor [[Value at Risk]] of an unhedged freight book, where `rate_volatility` is the daily return volatility of the route and `z_score` is the confidence multiplier (1.65 for 95 percent).

## Prerequisites
[[Freight]]
[[Forward Freight Agreement]]
[[Basis Risk]]

## Related concepts (learn next)
[[Freight Basis Risk]] is the residual exposure left after hedging with an index FFA, the next layer of precision once you hedge.
[[Market Hire]] is the spot time charter rate that translates freight rate risk into a daily rate view of the same exposure.
[[Bunker Risk]] is the fuel cost cousin of freight risk and the two move together when fuel drives rates.
[[Value at Risk]] is the tool to size the freight book and set risk limits across positions.
[[Freight Options]] gives convex protection, useful when you want a floor or cap without locking a level.
[[Location Arbitrage]] is the trade most directly killed by a freight spike, so understanding the exposure is essential there.
[[Baltic Route Codes]] are the specific index routes you hedge against, defining where basis risk comes from.
[[Physical vs Paper Freight]] clarifies the distinction between the cargo you move and the derivative you trade to hedge it.

## Common misconceptions
Only physical traders care about freight. Wrong: freight sets which cargoes actually move, and those flows drive futures basis, inventory builds, and commodity currencies like AUD, so paper only desks that ignore freight misread the physical signal behind the curve.
Freight rates are stable enough to ignore in the model. Wrong: a Capesize or VLCC route can double in a week on a single weather event, port closure, or a wave of demand, which is why freight is often the single largest swing factor in an arb P&L.
Fixing a rate removes all freight risk. Wrong: locking an index FFA removes index level risk but leaves [[Freight Basis Risk]] from the mismatch between your specific ship, load date, and port versus the standardized index route the contract settles against.

## Sources
Alizadeh and Nomikos, Shipping Derivatives and Risk Management, on freight rate exposure and FFA hedging.
Kavussanos and Visvikis, International Handbook of Shipping Finance, on freight risk measurement and hedge ratios.
Stopford, Maritime Economics, on freight rate formation and volatility.
Baltic Exchange route and index methodology guides for the settlement routes underlying FFAs.
Clarksons Shipping Intelligence Network (SIN) for route rates and time series.
ICE and CME dry and tanker FFA contract specifications.
Platts and Argus tanker and dry freight assessment methodology for Worldscale and per tonne conventions.
