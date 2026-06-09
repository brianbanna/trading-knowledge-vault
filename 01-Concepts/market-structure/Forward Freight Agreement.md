---
aliases: [ffa, forward freight agreement, freight swap, freight forward]
tags:
  - "#freight/ffa"
date-added: "2026-06-09"
---
# Forward Freight Agreement
## Definition
A Forward Freight Agreement is a bet on where a shipping freight rate will be in the future, settled in cash with no ship ever changing hands. Two parties agree today on a fixed price for moving cargo on a specific route or basket of routes over a future period such as a month, a quarter or a calendar year. When that period ends, they compare the agreed price to the average rate that actually prevailed, taken from a published [[Baltic Exchange and the Dry Indices]] assessment, and the loser pays the winner the difference. Technically it is a cash settled swap on a freight index where the floating leg is the average daily Baltic assessment over the settlement period and the fixed leg is the contract price. No vessel, no cargo and no physical delivery is involved, only money.
## Why it matters (commodities and FX)
[[Freight]] is one of the largest and most volatile costs in moving a physical commodity, and a freight trader cannot always lock it in with a physical [[Time Charter]] or [[Voyage Charter]] at the moment exposure appears. FFAs let a charterer, owner, or commodity desk fix a freight rate on paper instantly, months before a cargo loads, without finding a counterparty willing to fix a real ship. An owner who fears a falling market sells FFAs to lock revenue. A charterer or trader who fears rising rates buys FFAs to cap cost. Speculators and freight funds take outright positions on direction or trade spreads between routes and periods. Because FFAs are liquid and standardized they also produce a freight [[Forward Curve]] that informs physical fixing decisions, [[Floating Storage]] arbitrage, and the relative value between paper and steel.
## Concrete example
**Concrete:** A trader has chartered out 2 Capesize voyages from West Australia to Qingdao loading in 90 days and is exposed to the iron ore freight leg priced off [[Baltic Route Codes]] route C5. Spot C5 sits at 10.00 USD per tonne. To lock the cost the trader buys the C5 FFA for the relevant 1 month period at 10.50 USD per tonne for 320,000 tonnes total, which is 2 Capesize stems of 160,000 tonnes each. At settlement the exchange averages the daily C5 assessment over the month. Case A, market rises: the monthly average C5 prints 13.00 USD per tonne. The FFA pays the trader (13.00 minus 10.50) times 320,000 equals 800,000 USD. The physical freight now costs about 2.50 USD per tonne more than the original 10.50 fixed view, roughly 800,000 USD extra, so the paper gain offsets the physical pain and the net cost is locked near 10.50. Case B, market falls: the monthly average prints 8.00 USD per tonne. The FFA loses the trader (10.50 minus 8.00) times 320,000 equals 800,000 USD. Physical freight is now cheaper, but the trader gave up that windfall by hedging. The hedge worked as designed in both cases: it converted an uncertain cost into a fixed one near 10.50, paying off when rates rose and costing the saved windfall when they fell. The residual wobble comes from [[Basis]], the gap between the trader's actual fixed physical rate and the C5 index it is hedged against.
**Simplified:** You fix tomorrow's freight bill today at 10.50. If freight jumps to 13, your paper position pays you the 2.50 difference so your true cost stays 10.50. If freight drops to 8, you pay away 2.50 on paper and still effectively pay 10.50. You traded the chance of a cheaper bill for certainty.
## Key mechanics and formulas
- Settlement payment per tonne or per day: `payoff = (S_avg − F) × Q` where `F` is the agreed FFA fixed price, `S_avg` is the average Baltic assessment over the settlement period, and `Q` is the contracted quantity in tonnes (dry voyage routes) or in days (timecharter routes). The buyer receives this amount when positive and pays when negative.
- Floating leg: the arithmetic average of the published daily index prints across all index business days in the period. A single high or low day barely moves a monthly average, which damps manipulation and matches a real chartering programme spread over the month.
- Contract units: voyage routes such as C5 or C3 settle in USD per tonne; timecharter average routes such as C5TC, the Capesize 5 timecharter basket, settle in USD per day.
- Route specific FFA: tracks one Baltic route, for example C5 alone. Tightest hedge for a specific physical lane but lower liquidity.
- Basket FFA: tracks a published timecharter average across several routes, for example the Capesize 5TC or the [[Baltic Exchange and the Dry Indices]] Capesize index. Deeper liquidity and the main speculative instrument, but looser fit to any single physical voyage, which widens [[Basis Risk]].
- Periods: months (M), quarters (Q1 to Q4), and calendar years (CAL). Calendar and quarter strips are split into their constituent months at settlement.
- Clearing: most FFAs clear through a central counterparty to remove bilateral credit risk. Main clearing houses are [[SGX]], [[EEX]], and [[LCH]]. Cleared trades post initial and variation margin daily, so an adverse move triggers margin calls before final settlement.
- The physical to paper gap: a hedge is only as good as the correlation between your real fixed rate and the index. If you fix a vessel at a premium or discount to C5, or load on a slightly different lane, the FFA leaves a residual exposure. See [[Basis]] and [[Basis Risk]].
## Prerequisites
- [[Freight]]
- [[Baltic Exchange and the Dry Indices]]
- [[Baltic Route Codes]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Voyage Charter]]
- [[Time Charter]]
- [[Forward Curve]]
## Related concepts (learn next)
- [[Freight Options]] because options on FFAs let you cap or floor freight cost while keeping the upside, the next tool after the linear swap.
- [[Basis]] because the residual gap between your physical rate and the settled index is the main reason a freight hedge is imperfect.
- [[Basis Risk]] because quantifying that gap drives how many lots and which route you choose to hedge with.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because fuel is the other big freight cost and is hedged separately alongside FFAs.
- [[TC In and TC Out]] because paper positions are managed against a physical book of vessels taken in and chartered out.
- [[Contango]] and [[Backwardation]] because the shape of the freight [[Forward Curve]] determines roll economics and which periods are cheap to hedge.
- [[Value at Risk]] because freight desks size FFA books and margin needs against VaR limits.
- [[Ballast Leg Economics]] because the unpaid repositioning leg shapes the spot rate that the FFA ultimately settles against.
## Common misconceptions
- **"An FFA delivers a ship or cargo at expiry."** Wrong. An FFA is purely cash settled against a published index average. No vessel is nominated, no cargo moves, and the only thing exchanged at settlement is the price difference times the quantity. Physical transport is arranged separately through a [[Voyage Charter]] or [[Time Charter]].
- **"Hedging with an FFA removes all freight risk."** Wrong. It removes the index level risk but leaves [[Basis Risk]]: your actual fixed rate, route, and load timing rarely match the settled index perfectly, so a residual gap remains. A basket FFA against a single voyage leaves more basis than a route specific FFA.
- **"The FFA price is just today's spot rate."** Wrong. The FFA price is the market's forward expectation for the average over the settlement period, which can sit well above or below spot depending on whether the freight curve is in [[Contango]] or [[Backwardation]]. In the example the trader paid 10.50 forward while spot was 10.00.
- **"Cleared FFAs have no risk because there is a clearing house."** Wrong. Central clearing removes counterparty default risk but introduces daily margin calls. A large adverse move forces you to post variation margin immediately, which is a real liquidity drain even if the trade is a sound hedge.
## Sources
- Baltic Exchange, Guide to Market Benchmarks and the FFA documentation, balticexchange.com
- FIS (Freight Investor Services), Introduction to Freight Derivatives training notes
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management
- SGX, EEX and LCH freight clearing specifications and contract summaries
- Stopford, Maritime Economics, chapters on the freight market and derivatives
- Routing note: this note lives in 01-Concepts/market-structure because freight has no matching 02-Instruments commodity subfolder among energy, metals, agriculture, softs, fx, rates, equities, or crypto.
