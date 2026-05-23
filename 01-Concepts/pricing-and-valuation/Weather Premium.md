---
aliases: [weather premium, weather risk premium, crop risk premium]
tags:
  - "#agri/grains"
date-added: "2026-03-20"
---

# Weather Premium

## Definition
A weather premium is the additional risk premium embedded in agricultural futures to compensate holders for uncertainty about growing season weather and its impact on crop yields. It builds during planting and pollination (May to July for US [[Corn]] and [[Soybeans]]) when the crop is most vulnerable to heat stress, drought, or excess rainfall. The premium is additive to fundamental value implied by [[Stocks to Use Ratio]] and demand. If weather turns favorable, the premium fades fast (a "weather premium unwind"), often producing 10 to 20% declines in July and August. Confirmed damage converts the premium into a permanent upward adjustment. Magnitude depends on starting [[Stocks to Use Ratio]]: tighter stocks justify larger premiums because there is less buffer for a shortfall.

## Why it matters (commodities and FX)
Weather premium creates the most volatile and highest opportunity trading window of the year in [[Grains]] and softs, with corn and soybeans routinely moving 15 to 30% from June to August. Assessing whether the embedded premium is justified or excessive is the core analytical skill in agricultural trading during growing season. For FX traders, premium buildup in US crops affects export revenue and seasonal dollar demand from agricultural flows. [[Implied Volatility]] in grain options is structurally higher during the window, creating opportunities for vol buyers (expecting an event) and sellers (expecting normalization).

## Concrete example

**Concrete:** June 2012. US corn futures near $5.50/bu with a moderate weather premium building. Palmer Drought Severity Index shows rapidly worsening conditions across the western Corn Belt. Trader goes long July 2012 corn at $5.70/bu. By August, drought confirmed severe yield losses (USDA cut yield from trend 166 to 123 bu/acre). Corn hits $8.40/bu, $2.70/bu = $13,500/contract. Premium fully validated by crop destruction. Failure case: June 2015, trader buys Dec corn at $3.90 expecting the seasonal premium to persist. July rain across Illinois and Iowa above average, USDA crop conditions improve to 70% good/excellent. Corn drops to $3.55 by harvest, losing $0.35/bu = $1,750/contract. In 7 of 10 years, US growing season weather is adequate and the premium fades.

**Simplified:** Crops need decent weather to grow. Before the critical months, the futures price builds in a buffer for the risk of drought or heat. If the weather scare materializes, the buffer was too small and prices explode upward. If the weather is fine, the buffer was wasted, and prices collapse as harvest reveals the bumper crop. Most years the weather is fine. The years it is not pay for everything.

## Key mechanics and formulas
- **Weather premium = Current futures price − Fair value from known supply/demand fundamentals**
- **Fair value estimation**: regress historical prices against [[Stocks to Use Ratio]] for the "no weather risk" baseline
- **Key indicators**: Palmer Drought Severity Index (PDSI), Crop Moisture Index, USDA weekly Crop Progress (% good/excellent), NOAA 6 to 10 day and 8 to 14 day outlooks
- **Critical period (US corn)**: pollination July 5 to 25. Daytime temps above 95F during this window reduce kernel set and permanently impair yield.
- **Premium decay rate**: if weather normalizes after a scare, premium unwinds at $0.05 to $0.15/bu per week in corn
- **Volatility term structure**: weather premium inflates [[Implied Volatility]] in near term options during June/July. Vol collapses 20 to 40% after pollination passes without damage.

## Prerequisites
- [[Grains]]
- [[Stocks to Use Ratio]]
- [[Crop Year]]
- [[Implied Volatility]]
- [[Option]]

## Related concepts (learn next)
- [[Stocks to Use Ratio]] determines baseline vulnerability: lower S/U means a larger justified premium because there is less cushion.
- [[WASDE]] yield assumptions during growing season are the key reference point weather threatens.
- [[Old Crop New Crop]] spread widens when premium builds specifically in new crop contracts.
- [[Implied Volatility]] in grain options rises as premium builds and collapses when weather risk resolves favorably.
- [[COT Positioning]] shows whether managed money has already priced maximum weather risk, creating contrarian signals.
- [[Option]] strategies (long calls, call spreads) express premium views with defined max loss.
- [[Basis Risk]] increases during localized weather events when regional damage diverges local cash from national futures.

## Common misconceptions
- **"Weather premium always means prices will go up."** Premium is compensation for uncertainty, not a guarantee of damage. In 7 of 10 years US weather is adequate and the premium unwinds, producing losses for traders who bought peak uncertainty.
- **"You can predict weather accurately enough to trade directionally."** Forecasts beyond 10 to 14 days have low skill. Edge comes from assessing the embedded premium relative to the probability distribution, not predicting specific weather.
- **"Weather premium only applies to US crops."** Brazilian safrinha corn (Feb to May), Argentine soybeans (Dec to Mar), Australian wheat (Oct to Dec), and Indian sugar (monsoon) all embed weather premiums during their critical windows.
- **"Buy the dip on weather scares."** Scares often resolve favorably. Selling vol or fading the rally has historically been the higher Sharpe expression of the average outcome.

## Sources
- "Weather Derivatives and Agriculture" by Jewson, Brix, and Ziehmann
- CME Group, "Corn Seasonal Tendencies and Weather Risk"
- USDA National Agricultural Statistics Service (NASS), Crop Progress Reports
- Irwin, S. and Good, D., "Forming Expectations for the 2012 US Average Corn Yield," farmdoc daily
