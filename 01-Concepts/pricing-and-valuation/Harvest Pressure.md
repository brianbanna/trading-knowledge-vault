---
aliases: [harvest pressure, harvest selling, harvest hedge pressure]
tags:
  - "#agri/grains/wheat"
  - "#agri/grains"
  - "#microstructure"
date-added: "2026-07-15"
---

# Harvest Pressure

## Definition

Harvest pressure is concentrated forced selling that hits a grain market during the annual harvest window: farmers with more grain than bin space truck it straight to the elevator and sell because they have nowhere else to put it, and elevators, now long a wall of physical grain, hedge that inventory by shorting futures. Neither side is expressing a price view. The farmer sells because storage is finite, the elevator shorts because it does not want directional wheat risk on its balance sheet. The result is a burst of commercial selling concentrated in a 3 to 6 week window, landing hardest on the futures contract closest to delivery. Technically, it shows up as [[Cost of Carry|calendar spread]] widening, front month cheapening relative to deferred, not necessarily as a fall in the outright price level.

## Why it matters (commodities and FX)

Harvest pressure is a spread driver, not a level driver, and distinguishing the 2 is the whole test for a grains trader. Flat price can do almost anything into harvest, rally on a export demand story, sell off on a bumper crop, chop sideways, depending on the macro and fundamental backdrop. What harvest pressure reliably does is widen the relationship between the harvest-month contract and the deferred contract, because forced commercial selling is structurally concentrated in the front. A trader who reads "harvest is coming, wheat will fall" is trading the wrong variable; the professional trade is in the [[Calendar Spread]], not the outright. It also shows up directly in [[COT Positioning]]: commercial short interest builds mechanically into harvest as elevators put on hedges against inventory, independent of what commercials think prices will do next.

## Concrete example

**Concrete:** Mid June, Kansas HRW wheat. KC July futures (KE) at $6.30/bu, September futures at $6.45/bu. Sept minus July spread = +$0.15/bu, a normal early season carry. A farmer with 5,000 tonnes of production (about 183,700 bu at 36.74 bu/tonne) has bins for 40% of that, roughly 73,500 bu. The remaining 110,200 bu has to move off the combine straight to town, sold at whatever bid the elevator posts, because there is no on-farm storage left and no logistics to arrange alternative storage on short notice. Multiply that farmer by thousands across the Kansas HRW belt hitting the combine in the same 3 to 4 week window, and the elevator system is buying grain far faster than it can place it with end users. One regional elevator operation accumulating inventory this way is short 50,000 tonnes of futures (about 1.84 million bu, roughly 367 KE contracts at 5,000 bu each) as a hedge against the cash grain it is taking in. That short hedge program leans on the nearby, most liquid, delivery-linked contract: July.

By mid July, July futures have sagged to $6.05/bu (down $0.25) under the weight of concentrated commercial selling. September, one crop year removed from the immediate physical glut and still carrying the export demand book, is down only $0.10, to $6.35/bu. The spread has widened from +$0.15 to +$0.30/bu. That is harvest pressure: the front cheapened relative to the back, the outright price fell only modestly.

Now the full carry check (see [[Full Carry]]). Storage at a commercial elevator runs about $0.03/bu/month; financing at 6% annual on $6.05/bu futures costs about 6.05 × 0.06 × (2/12) ≈ $0.06/bu over the 2 month July to September gap. Total full carry for 2 months ≈ $0.06 + $0.06 = $0.12/bu. The actual spread has widened to $0.30/bu, about $0.18/bu above what storage and financing justify. That $0.18/bu overshoot, not the fact of contango itself, is the tradeable signal: a merchandiser with bin space can buy cash wheat near the July price, store it 2 months for about $0.12/bu of true cost, and sell September at $6.35, locking close to $0.18/bu of near riskless profit. That flow, buying the front, selling the back, is exactly what compresses the spread back toward full carry.

**If it works:** a trader who sells the Sept/July spread at +$0.30 (short Sept, long July) profits as commercial cash-and-carry flow and normalizing elevator hedge activity pull the spread back to $0.12 to $0.15 over the following weeks. On a 5,000 bu KE contract, capturing $0.15 to $0.18/bu of reversion is $750 to $900 per contract.

**If it fails:** a drought scare hits Black Sea or Argentine wheat mid trade, export demand for US wheat spikes into the deferred contract, and September jumps instead of July catching up. The spread blows out further to $0.45/bu instead of converging. The trader is down $0.15/bu, or $750 per contract, and the position needs a stop or a fundamental reassessment, not a "wait it out," because the widening now has a demand driven cause that has nothing to do with harvest logistics.

## Key mechanics and formulas

**Transmission chain:**
`Forced selling (bin space exhausted) → elevator cash inventory builds → commercial (elevator) shorts futures to hedge inventory → short flow concentrates in the front, delivery-linked contract → front month cheapens vs deferred → spread widens toward, and sometimes through, full carry`

**Full carry arithmetic for the front to deferred gap (T−t in months):**

`Full Carry(T−t) = Storage rate ($/bu/month) × (T−t) + F × r × (T−t)`

Where F = front futures price, r = annual financing rate, Storage rate = commercial elevator storage cost per bushel per month.

**Ceiling test**, comparing the actual observed spread to Full Carry(T−t):
- Actual spread < full carry → the widening has room; forced selling can keep pushing the spread out without triggering arbitrage.
- Actual spread ≈ full carry → the ceiling. Further widening needs storage rates or financing rates to rise, not just more forced farmer selling. See [[Full Carry]].
- Actual spread > full carry → cash and carry arbitrage (buy cash, store, sell deferred) becomes profitable, and that flow mechanically compresses the spread back down, usually the true constraint on how far harvest pressure can run.

## Prerequisites
- [[Crop Year]]
- [[Forward Curve]]
- [[Contango]]
- [[Cost of Carry]]

## Related concepts (learn next)
- [[Old Crop New Crop]] — harvest pressure is the mechanical driver behind the old crop to new crop transition; new crop cheapens relative to old crop as the physical glut arrives at the field.
- [[Contango]] — the curve shape harvest pressure typically pushes toward, front under deferred.
- [[Cost of Carry]] — the model that separates how much of the harvest driven widening is storage and financing justified versus pure overshoot.
- [[Calendar Spread]] — the instrument that actually trades harvest pressure; almost nobody trades it as an outright.
- [[Seasonality]] — harvest pressure is the specific, physically grounded seasonal pattern in grains; the trade is in the deviation from the seasonal norm, not the pattern itself.
- [[Basis]] — cash basis weakens hardest right at harvest for the same forced-selling reason that hits the futures spread.
- [[COT Positioning]] — commercial short interest building into harvest is the direct CFTC fingerprint of elevator hedge pressure.
- [[Convenience Yield]] — collapses toward 0, or goes negative, right at harvest when physical grain is abundant and nobody pays up for prompt supply.
- [[Crop Year]] — harvest pressure marks the boundary crossing from one crop year into the next; timing shifts by hemisphere and crop.
- [[Structural Break]] — the reason a multi decade seasonal average can mislead; a shift in export flows or acreage resets what "normal" harvest pressure looks like.
- [[Hedging]] — the elevator short futures position that transmits farmer selling into the futures market is a textbook short hedge.
- [[WASDE]] — the monthly report that recalibrates how heavily harvest pressure should weigh on the spread, by updating production and ending stocks.
- [[Full Carry]] — the arbitrage bound that caps how far harvest pressure can push the spread; once the spread reaches full carry, further widening requires storage or financing costs to rise, not more forced selling.

## Common misconceptions

**"Harvest pressure means flat price falls."** It does not. It means the front weakens relative to the deferred, a spread effect, not a level effect. Outright price can rise into harvest on a strong export or weak dollar story while the calendar spread still widens underneath it, because the forced-selling mechanism (bin space, elevator hedging) acts on the relationship between contract months, not on the market's overall price view. Trading harvest as a flat price bear thesis conflates 2 different variables.

**"The seasonal is the edge."** It is not. A seasonal chart shows the average path a spread has taken into and through harvest over many years. That average is already public and already priced into where the curve sits relative to full carry. The actual edge is the deviation, how far the current spread sits from full carry, from its own seasonal norm, or from what commercial positioning implies, not the existence of the seasonal pattern itself. Buying "the seasonal" when the spread already sits at its normal harvest level or at full carry has no edge left in it.

**"30 years of seasonal data describes 1 market."** It does not. The export and production structure underlying US grain seasonals shifted materially once the Black Sea region (Russia, Ukraine) and Brazil became marginal suppliers capable of dominating price action, a change that accelerated from roughly 2010 onward. A seasonal built mostly on pre 2010, US-centric export flow describes a different market than one where a Black Sea harvest, war risk, or Brazilian safrinha timing can override the US crop calendar. Treat the pre and post structural break periods as separate samples (see [[Structural Break]]), not one continuous 30 year seasonal.

## Sources
- CME Group, KC HRW Wheat (KE) futures contract specifications
- USDA NASS, Wheat harvest progress reports
- Session notes, 2026-07-15
