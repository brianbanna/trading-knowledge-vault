---
aliases: [geopolitical risk, geopolitics, political risk, geopol risk]
tags:
  - "#macro"
  - "#energy/crude"
date-added: "2026-03-20"
---

# Geopolitical Risk

## Definition

Geopolitical risk refers to the potential for political events, military conflicts, sanctions, regime changes, and territorial disputes to disrupt commodity supply chains, trade flows, and market pricing. In commodity markets, geopolitical risk is concentrated in energy (Middle East, Russia, Venezuela, Libya, Nigeria), metals (DRC cobalt, Russian nickel/palladium, Chilean copper), and trade routes (Strait of Hormuz, Suez Canal, Malacca Strait). Geopolitical risk creates asymmetric payoff profiles: the risk premium is often small and persistent (a few dollars per barrel in oil), but the realized events are large and sudden ([[Supply Shock]]).

## Why it matters (commodities and FX)

Geopolitical risk is priced into commodity markets at all times through a "risk premium" embedded in the price. The risk premium represents the probability weighted cost of supply disruptions that have not yet occurred. When tensions rise, the premium increases even without any actual supply loss. When tensions ease, the premium deflates. This risk premium is separate from fundamental supply/demand pricing and can add $5 to $15/bbl to crude oil during elevated geopolitical periods.

For FX, geopolitical events trigger [[Safe Haven Assets|safe haven]] flows (into USD, JPY, CHF, gold) and away from [[Commodity Currencies]] of affected regions. Russian ruble, Turkish lira, and other EM currencies at the center of geopolitical events can move 10 to 30% in days.

## Concrete example

**Strait of Hormuz risk:** Approximately 20% of global oil supply (~20 million bbl/d) transits the Strait of Hormuz. Iran has periodically threatened closure. The risk is asymmetric: there is a small persistent premium in [[Brent Crude]] reflecting the non zero probability of closure, but if closure actually occurred, oil could spike $30 to $50/bbl immediately. Trading this: long out of the money Brent call options (defined risk, convex payoff) vs paying the persistent premium in outright longs.

**Russia sanctions (2022):** The geopolitical risk premium in European gas went from EUR 5 to 10/MWh (pre 2022) to EUR 100+/MWh as the market priced in the possibility, then reality, of Russian pipeline gas curtailment. The premium was not proportional to the probability; it reflected the magnitude of the potential disruption times the market's inability to substitute quickly.

## Key mechanics and formulas

**Risk premium decomposition:**
`Commodity Price = Fundamental Value + Geopolitical Risk Premium + Speculative Premium`

The geopolitical premium is unobservable directly but can be estimated by comparing current prices to model implied fair values based on inventory, production, and demand fundamentals.

**Geopolitical risk indices:**
- Caldara and Iacoviello Geopolitical Risk Index (GPR): text based index from news articles. Spikes correlate with oil price moves.
- Political Risk Services (PRS) Group: country level political risk scores

**Asymmetric payoff:**
The expected value of geopolitical risk in oil = Probability x Magnitude. If there is a 5% chance of a 10 million bbl/d disruption lasting 1 month (reducing global supply by ~10%), the price impact could be $30+/bbl. A 5% probability x $30 = $1.50/bbl expected premium. This is why the risk premium seems "small" most of the time but produces outsized moves when events materialize.

## Prerequisites
- [[Supply Shock]]
- [[Forward Curve]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Supply Shock]] - geopolitical events are the primary cause of negative supply shocks in energy.
- [[Safe Haven Assets]] - the cross asset response to geopolitical risk. Gold and JPY typically strengthen.
- [[Risk-On Risk-Off]] - geopolitical escalation shifts markets to risk off, compressing equity/credit and supporting safe havens.
- [[Commodity Currencies]] - currencies of geopolitically exposed nations (RUB, IQD, NGN) are directly affected. Currencies of beneficiary nations (US shale = bullish CAD/USD) can strengthen.
- [[Brent Crude]] - the most geopolitically sensitive major commodity benchmark due to seaborne exposure.
- [[Volatility]] - geopolitical risk spikes implied volatility in energy options, creating trading opportunities in vol markets.

## Common misconceptions

**"Geopolitical events always push prices up."** Only supply threatening events push prices up. Geopolitical events that increase supply (e.g., Iran nuclear deal in 2015 lifting sanctions, adding ~1 million bbl/d) push prices down.

**"The risk premium is wasted money."** The premium is insurance. Over long periods, the premium appears as a cost (most months, the Strait of Hormuz stays open). But the premium compensates for the tail risk. Removing it from your model means you are unhedged against the worst case.

**"Markets panic for a long time after geopolitical events."** Most geopolitical risk premiums decay within 1 to 4 weeks unless the event produces actual, sustained supply loss. The pattern is: spike, assess, fade. The 2019 Abqaiq attack (Saudi Arabia) removed 5.7 million bbl/d temporarily, but Brent's $10/bbl spike fully reversed in 2 weeks when production was restored.

## Sources

- Caldara and Iacoviello, "Measuring Geopolitical Risk" (2022, American Economic Review)
- IEA Emergency Response mechanisms (coordinated SPR release protocols)
- Platts: OPEC and geopolitical analysis
- Reuters, Bloomberg: real time geopolitical monitoring
