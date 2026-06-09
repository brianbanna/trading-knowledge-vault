---
aliases: [bdi, baltic dry index, baltic exchange, bci, bpi, bsi, bhsi, dry indices]
tags:
  - "#freight/routes"
date-added: "2026-06-09"
---
# Baltic Exchange and the Dry Indices
## Definition
The [[Baltic Exchange and the Dry Indices|Baltic Exchange]] is a membership organisation in London that has been the central marketplace for arranging ocean freight since 1744. It does not trade cargo itself. Instead, it collects daily price quotes from a panel of independent shipbroker firms and turns them into published numbers that everyone in the shipping market can see. Think of it like a thermometer for the cost of moving raw materials by sea: every business day the panellists submit their honest assessment of what it costs to hire a ship on specific, standardised routes, and the Exchange averages those submissions into indices. The headline number is the Baltic Dry Index ([[Baltic Exchange and the Dry Indices|BDI]]), a single figure that blends the cost of hiring the four main sizes of dry bulk ship. Technically the BDI is a composite of four vessel size sub indices, each itself an average of several time charter and voyage route assessments, expressed in index points rather than dollars.
## Why it matters (commodities and FX)
A dry bulk trader lives and dies by these indices because they are the agreed settlement reference for [[Forward Freight Agreement]] contracts, so the difference between where you fixed a hedge and where the index prints decides your profit and loss. They are also the only transparent, daily, public price for an otherwise opaque physical market, which means a trader uses them to mark a position to market, to value a [[Time Charter]] versus the spot alternative, and to spot when freight is cheap or expensive relative to the [[Forward Curve]]. Because dry bulk carries iron ore, coal and grain, the [[Baltic Exchange and the Dry Indices|BDI]] doubles as a macro barometer: a rising index often signals Chinese steel mills restocking iron ore or a tight grain export season, and macro desks watch it as a real economy demand gauge that moves commodity FX pairs like AUD, the currency of the largest iron ore exporter. Knowing which sub index is driving a BDI move tells you whether the story is a Capesize iron ore story or a smaller ship grain story, and that distinction changes which trades you put on.
## Concrete example
**Concrete:** On a Monday the [[Baltic Exchange and the Dry Indices|BDI]] jumps from 1,800 to 2,050 points, a 14 percent move in one print. You decompose it and find the Capesize sub index ([[Baltic Exchange and the Dry Indices|BCI]]) is up sharply while [[Baltic Exchange and the Dry Indices|BPI]], [[Baltic Exchange and the Dry Indices|BSI]] and [[Baltic Exchange and the Dry Indices|BHSI]] barely moved. The driver is route C5, the [[Baltic Route Codes|West Australia to Qingdao]] iron ore run, where rates went from 9.50 to 11.20 dollars per tonne because Chinese mills are restocking ahead of stimulus. You hold a long position of 30 [[Forward Freight Agreement]] lots on the C5TC Capesize time charter average at 22,000 dollars per day for the current quarter, where each lot is 1 day. The published index average for the settlement period prints at 26,000 dollars per day. Your gain is `(26,000 - 22,000) * 30 = 120,000` dollars because the index you bet on rose. If instead you had misread the move as broad demand and gone long the [[Baltic Exchange and the Dry Indices|BPI]] Panamax average at 14,000 dollars per day, and Panamax stayed flat at 13,800 while only Capesize rallied, your Panamax FFA would settle at a 200 dollar per day loss, costing `(13,800 - 14,000) * 30 = -6,000` dollars while you missed the actual Capesize move entirely.
**Simplified:** The BDI went up, but the whole rise came from the biggest ships hauling iron ore to China. Betting on the right ship size made money. Betting on the wrong size, even with the headline number rising, lost money and missed the real story.
## Key mechanics and formulas
- The BDI is published once per business day around 13:00 London time after panellists submit assessments. It is dimensionless index points, not a dollar rate.
- It is a weighted composite of 3 of the 4 dry sub indices. The current convention weights each of [[Baltic Exchange and the Dry Indices|BCI]], [[Baltic Exchange and the Dry Indices|BPI]] and [[Baltic Exchange and the Dry Indices|BSI]] equally and applies a published multiplier: `BDI = 0.40 * (BCI + BPI + BSI) / 3` is the rough form, where the 0.40 factor links today's level to the historical base. [[Baltic Exchange and the Dry Indices|BHSI]] Handysize is published but currently excluded from the BDI composite.
- Each sub index is the average of several route assessments. `BCI` Capesize covers routes for the roughly 180,000 [[Vessel Classes and Deadweight Tonnage|deadweight tonnage]] ships, `BPI` Panamax the roughly 82,000 dwt ships, `BSI` Supramax the roughly 58,000 dwt ships, `BHSI` Handysize the roughly 38,000 dwt ships. See [[Wet Tanker Classes]] for the tanker analogue.
- Routes are of two types. [[Voyage Charter]] routes are quoted in dollars per tonne of cargo (for example C5 iron ore West Australia to China). [[Time Charter]] routes are quoted in dollars per day for hiring the whole ship (for example C5TC, the Capesize time charter basket). See [[Baltic Route Codes]] for the naming system.
- Each sub index also publishes a time charter average, the headline daily hire number (C5TC, P4TC, S10TC, HS7TC) that [[Forward Freight Agreement]] and [[Freight Options]] contracts settle against. FFA settlement uses the arithmetic average of the daily index over all business days in the contract month or quarter.
- Panellists are vetted shipbroker firms bound by a code of conduct to submit a professional, unbiased assessment of where they could fix business that day, not where they wish it would trade.
## Prerequisites
- [[Freight]]
- [[Vessel Classes and Deadweight Tonnage]]
- [[Dry Bulk versus Wet Bulk]]
- [[Time Charter]]
- [[Voyage Charter]]
## Related concepts (learn next)
- [[Baltic Route Codes]] decodes the C5, P4TC and S10TC labels so you can read exactly which trade each index assessment represents.
- [[Forward Freight Agreement]] is the derivative that settles against these index averages, the main way a trader takes or hedges a freight view.
- [[Freight Options]] add convexity on top of the index, letting you buy or sell the right rather than the obligation to a freight level.
- [[TC In and TC Out]] explains how an operator uses the index to value chartering a ship in versus out.
- [[Ballast Leg Economics]] shows why the dollar per day index hides the empty repositioning leg that route economics must absorb.
- [[Seasonality]] matters because grain and coal flows give the smaller ship indices a different annual rhythm than Capesize iron ore.
- [[Backwardation]] and [[Contango]] in the freight forward curve tell you whether the market expects spot index levels to fall or rise.
- [[Port Congestion and Waiting Time]] is a hidden supply shock that lifts the indices by tying up ships that would otherwise be available.
## Common misconceptions
- **"The BDI is quoted in dollars, so a reading of 2,000 means 2,000 dollars."** Wrong. The BDI is a dimensionless index in points, anchored to a historical base. The dollar values live inside the underlying route assessments and the time charter averages like C5TC, not in the headline composite number.
- **"The BDI measures the price of the commodities being shipped."** Wrong. It measures the cost of the shipping itself, the hire of the vessel, not the value of the iron ore or coal aboard. Freight cost and commodity price can and do move in opposite directions.
- **"All four sub indices feed the BDI equally."** Wrong. Under the current methodology only [[Baltic Exchange and the Dry Indices|BCI]], [[Baltic Exchange and the Dry Indices|BPI]] and [[Baltic Exchange and the Dry Indices|BSI]] enter the composite, and [[Baltic Exchange and the Dry Indices|BHSI]] Handysize is published separately but excluded. The exact weights and the multiplier have been revised over the index history.
- **"A rising BDI always means broad based shipping strength."** Wrong. The composite can be dragged up by a single sub index. A Capesize iron ore spike can lift the BDI while Panamax and Supramax stay flat, so the headline number can mislead unless you decompose it by vessel size.
## Sources
- The Baltic Exchange, Guide to Market Benchmarks and Indices, balticexchange.com
- The Baltic Exchange, Manual for Panellists, current edition
- Stopford, Martin. Maritime Economics, 3rd edition, Routledge, chapters on freight markets and shipping cycles
- Alizadeh, Amir and Nomikos, Nikos. Shipping Derivatives and Risk Management, Palgrave Macmillan
- Baltic Exchange historical BDI series and methodology change notices
