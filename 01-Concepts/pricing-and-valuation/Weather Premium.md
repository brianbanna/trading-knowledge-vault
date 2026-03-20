---
aliases: [weather premium, weather risk premium, crop risk premium]
tags:
  - "#agri/grains"
date-added: "2026-03-20"
---

# Weather Premium

## Definition
A weather premium is the additional risk premium embedded in agricultural commodity futures prices to compensate holders for the uncertainty of growing season weather and its potential impact on crop yields. It typically builds during the planting and pollination windows (May to July for US [[Corn]] and [[Soybeans]]) when the crop is most vulnerable to heat stress, drought, or excessive rainfall. The premium is additive to the fundamental value implied by the current [[Stocks to Use Ratio]] and demand forecasts. If weather turns favorable during the critical growing period, the premium fades rapidly (a "weather premium unwind"), often producing sharp price declines of 10 to 20% in July and August. Conversely, confirmed weather damage converts the premium into a permanent upward price adjustment reflecting reduced supply. The magnitude of the justified weather premium depends heavily on the starting [[Stocks to Use Ratio]]: when stocks are already tight, the market prices in larger premiums because there is less buffer available to absorb a production shortfall.

## Why it matters (commodities and FX)
Weather premium dynamics create the most volatile and highest opportunity trading window of the year in [[Grains]] and soft commodities, with corn and soybeans routinely moving 15 to 30% during June to August. Correctly assessing whether the embedded premium is justified or excessive is the core analytical skill in agricultural trading during the growing season. For FX traders, weather premium buildup in US crops affects export revenue expectations and seasonal dollar demand from agricultural trade flows. [[Implied Volatility]] in grain options is structurally higher during the weather premium window, creating opportunities for both volatility buyers (who expect a weather event) and sellers (who expect normal conditions to unwind the premium).

## Concrete example
**Success case:** In June 2012, US corn futures traded near $5.50/bu with a moderate weather premium building. The Palmer Drought Severity Index showed rapidly worsening conditions across the western Corn Belt. A trader went long July 2012 corn at $5.70/bu. By August, the drought confirmed severe yield losses (USDA cut yield from trend 166 to 123 bu/acre), and corn hit $8.40/bu, a gain of $2.70/bu or $13,500 per contract. The weather premium was fully validated by actual crop destruction.

**Failure case:** In June 2015, a trader bought December corn at $3.90/bu expecting the seasonal weather premium to persist and expand. July rainfall across Illinois and Iowa was above average, and USDA's weekly crop condition report improved to 70% good/excellent. Corn dropped to $3.55/bu by harvest as the premium unwound completely, a loss of $0.35/bu or $1,750 per contract. The lesson: in roughly 7 out of 10 years, US growing season weather is adequate, and the weather premium fades.

## Key mechanics and formulas
- **Weather premium = Current futures price - Fair value estimated from known supply/demand fundamentals**
- **Fair value estimation:** Regress historical prices against [[Stocks to Use Ratio]] to derive the "no weather risk" price level for comparison
- **Key weather indicators:** Palmer Drought Severity Index (PDSI), Crop Moisture Index, USDA weekly Crop Progress (% good/excellent), NOAA 6 to 10 day and 8 to 14 day temperature and precipitation outlooks
- **Critical period (US corn):** Pollination occurs approximately July 5 to 25. Daytime temperatures above 95F during this window reduce kernel set and permanently impair yield.
- **Premium decay rate:** If weather normalizes after a scare, the premium can unwind at $0.05 to $0.15/bu per week in corn
- **Volatility term structure:** Weather premium inflates [[Implied Volatility]] in near term options during June/July; vol typically collapses 20 to 40% after pollination passes without damage

## Prerequisites
- [[Grains]]
- [[Stocks to Use Ratio]]
- [[Crop Year]]
- [[Implied Volatility]]
- [[Option]]

## Related concepts (learn next)
- [[Stocks to Use Ratio]] determines baseline vulnerability: lower S/U means a larger justified weather premium because there is less inventory cushion.
- [[WASDE]] yield assumptions published during the growing season are the key reference point that weather conditions threaten.
- [[Old Crop New Crop]] spread widens when weather premium builds specifically in new crop contracts.
- [[Implied Volatility]] in grain options rises as weather premium builds and collapses when weather risk resolves favorably.
- [[COT Positioning]] shows whether managed money has already priced in maximum weather risk, creating contrarian signals.
- [[Option]] strategies such as buying calls or call spreads are common ways to express weather premium views with defined maximum loss.
- [[Basis Risk]] can increase during localized weather events when regional damage creates divergence between local cash and national futures prices.

## Common misconceptions
- **"Weather premium always means prices will go up."** The premium is compensation for uncertainty, not a guarantee of realized damage. In most years (roughly 7 out of 10), US growing season weather is adequate and the premium unwinds, producing losses for traders who bought at peak uncertainty.
- **"You can predict weather accurately enough to trade directionally."** Weather forecasts beyond 10 to 14 days have low skill. The trading edge comes from assessing the embedded premium relative to the probability distribution of outcomes, not from predicting specific weather patterns.
- **"Weather premium only applies to US crops."** Brazilian safrinha corn (February to May), Argentine soybeans (December to March), Australian wheat (October to December), and Indian sugar (monsoon season) all embed weather premiums during their respective critical growing windows.

## Sources
- "Weather Derivatives and Agriculture" by Jewson, Brix, and Ziehmann
- CME Group, "Corn Seasonal Tendencies and Weather Risk"
- USDA National Agricultural Statistics Service (NASS), Crop Progress Reports
- Irwin, S. and Good, D., "Forming Expectations for the 2012 US Average Corn Yield," farmdoc daily
