---
aliases: [freight basis risk, freight physical to paper basis, ffa basis risk, freight hedge basis]
tags:
  - "#risk"
  - "#freight/ffa"
date-added: "2026-06-17"
---

# Freight Basis Risk

## Definition
You sold a paper hedge to protect a physical freight position, but the hedge does not pay out exactly what your real cargo costs or earns. The leftover gap is freight basis risk. Formally it is the residual exposure that survives after you offset a physical freight position with a [[Forward Freight Agreement]] or [[Freight Options]], driven by the difference between your actual physical outcome and the [[Baltic Exchange and the Dry Indices|Baltic]] index the paper settles against. It is the freight specific case of [[Basis Risk]]. The hedge removes the index level move; it does not remove the wedge between your lane and the index, so a hedged book is never fully flat. That wedge is where most of a freight desk's hedged profit and loss actually lands.

## Why it matters (commodities and FX)
A freight hedge only cuts total risk if the physical leg and the paper index move together. The cleaner the match, the smaller the residual. Hedging one specific voyage with a basket time charter average such as C5TC leaves far more basis than hedging with a route specific contract, because the basket blends several lanes and dilutes your exposure to the one you actually fixed. The basis is rarely small or stable. Under port congestion, weather disruption, or a regime shift in trade flows, the correlation between a single lane and the basket breaks down and the basis can move several standard deviations against you in days. A trader who treats the FFA as a perfect offset will book a surprise loss precisely when the market is most stressed, which is exactly when the hedge was supposed to help. Sizing the hedge, picking the right [[Baltic Route Codes|route code]], and watching the basis are the work; selling the lot is the easy part.

## Concrete example
**Concrete:** You operate a Capesize carrying iron ore from West Australia (Port Hedland) to Qingdao, the C5 lane. You are exposed to physical freight rising before you fix forward cargoes, so you hedge by selling 30 lots of the C5TC basket FFA for the next quarter at USD 22,000 per day. C5TC is the Capesize 5 time charter basket, an average of several Capesize routes, not the single C5 voyage. One lot is 1 day, so 30 lots per month across 3 months is a notional of roughly 90 vessel days. Then congestion builds at Chinese discharge ports and the Pacific tightens. The C5 voyage rate, converted to a [[Time Charter Equivalent|TCE]], jumps from USD 22,000 to USD 31,000 per day, a USD 9,000 rise on your physical. The C5TC basket, dragged down by softer Atlantic routes inside it, rises only to USD 26,500, a USD 4,500 gain on your short FFA. Per day: physical cost up USD 9,000, FFA gain USD 4,500, net loss USD 4,500 per day. That USD 4,500 is pure basis loss, the part the hedge could not catch because the basket lagged your lane. Across 90 days that is roughly USD 405,000 you did not expect on a position you believed was hedged. Now the symmetric case: if instead the Atlantic had spiked and the Pacific stayed soft, the basket could rise USD 6,000 while your C5 lane rose only USD 2,000. The FFA over hedges, the basis swings in your favor, and you bank a USD 4,000 per day windfall on the same structure. Same hedge, opposite sign, because the basis can cut either way.

**Simplified:** You insure your specific shipping lane using a price index that averages several lanes. When your lane jumps more than the average, the insurance pays out less than your real bill and you eat the difference. When your lane jumps less than the average, you actually come out ahead. The hedge fixes the broad market move; the leftover gap between your exact route and the average is freight basis risk, and it can help you or hurt you.

## Key mechanics and formulas
`basis = physical_rate - index_price` where `physical_rate` is your realized voyage or TCE rate on the actual lane and `index_price` is the Baltic route or basket level the FFA settles on. A positive basis means your physical trades at a premium to the index.

`h* = rho * (sigma_physical / sigma_index)` is the minimum variance optimal hedge ratio, where `rho` is the correlation between physical rate changes and index changes, `sigma_physical` is the standard deviation of physical rate changes, and `sigma_index` is the standard deviation of index changes. A lower `rho` (worse route match) shrinks the hedge you should put on, because over hedging a poorly correlated index adds variance.

`hedge_effectiveness = 1 - var(hedged) / var(unhedged)` measures how much of your unhedged variance the hedge removed. A value near 1 is a tight hedge; a low or negative value means the hedge added risk, which happens when you hedge a single lane with a weakly correlated basket.

Note the FFA settles against a monthly average of the index while your physical fixing or load date is a single point in time, so even a perfect route match carries a timing component of basis.

## Prerequisites
[[Basis Risk]]
[[Forward Freight Agreement]]
[[Baltic Route Codes]]

## Related concepts (learn next)
[[Basis]] — the general physical to paper gap that freight basis risk specializes; learn the parent idea first.
[[Freight Rate Risk]] — the outright exposure the FFA is meant to hedge, before any basis is left behind.
[[Physical vs Paper Freight]] — the two sides whose mismatch creates the basis in the first place.
[[Baltic Exchange and the Dry Indices]] — the index family your hedge settles against, so its construction drives your basis.
[[Freight Options]] — an alternative hedge whose payoff shape changes the residual basis profile versus a linear FFA.
[[TC In and TC Out]] — physical hedging by chartering in and out, which carries its own basis against the paper market.
[[Value at Risk]] — how to size and report the residual basis exposure on a hedged book.
[[Hedging]] — the broader framework for choosing instruments, ratios, and what risk you accept to keep.

## Common misconceptions
An FFA removes all freight risk. Wrong. It removes the index level move only. The wedge between your specific lane and the settlement index survives, and that residual is freight basis risk; a hedged book is reduced risk, not zero risk.

The basket and a single route are interchangeable for hedging. Wrong. C3 (Brazil to China) and C5 (West Australia to China) can move in opposite directions when one basin tightens and the other loosens. Hedging C5 ore with a C3 contract, or with the blended C5TC basket, can leave you exposed to the very move you tried to cover.

Freight basis is small and stable. Wrong. It is benign in calm markets and widens sharply under congestion, weather, or trade flow regime shifts, exactly when you need the hedge. Treating historical calm period correlation as permanent understates tail risk.

More hedging is always safer. Wrong. If the index is weakly correlated with your lane (`rho` low), adding lots past the optimal `h*` raises total variance rather than lowering it. A bad hedge can make a book riskier than no hedge at all.

## Sources
Alizadeh and Nomikos, Shipping Derivatives and Risk Management, chapters on FFA hedging, hedge ratios, and basis risk.
Kavussanos and Visvikis, The International Handbook of Shipping Finance, sections on freight risk management and hedge effectiveness.
Stopford, Maritime Economics, 3rd edition, on freight market structure and route differentials.
Baltic Exchange, FFA and index methodology guides (route definitions, C5TC and Capesize basket construction, settlement on monthly averages).
Clarksons SIN, route rate and TCE data for lane versus basket comparison.
Ship and Bunker and Platts/Argus methodology notes for physical voyage rate references.
