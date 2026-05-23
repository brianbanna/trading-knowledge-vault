---
aliases: [geopolitical risk, geopolitics, political risk, geopol risk]
tags:
  - "#macro"
  - "#energy/crude"
date-added: "2026-03-20"
---

# Geopolitical Risk

## Definition

Geopolitical risk is the potential for political events, military conflicts, sanctions, regime changes, and territorial disputes to disrupt commodity supply chains, trade flows, and pricing. In commodities, the risk is concentrated in energy (Middle East, Russia, Venezuela, Libya, Nigeria), metals (DRC cobalt, Russian nickel/palladium, Chilean copper), and trade routes (Strait of Hormuz, Suez Canal, Malacca Strait). Geopolitical risk produces asymmetric payoffs: the premium is small and persistent (a few dollars per barrel in oil), but realized events are large and sudden ([[Supply Shock]]).

## Why it matters (commodities and FX)

Geopolitical risk is priced into commodities through a "risk premium" embedded in price. The premium represents the probability weighted cost of supply disruptions that have not occurred. When tensions rise, the premium expands even without supply loss. When tensions ease, it deflates. The premium is separate from fundamental supply/demand and adds $5 to $15/bbl to crude during elevated periods.

For FX, geopolitical events trigger [[Safe Haven Assets|safe haven]] flows (into USD, JPY, CHF, gold) and away from [[Commodity Currencies]] of affected regions. Russian ruble, Turkish lira, and other EM currencies at the center can move 10 to 30% in days.

## Concrete example

**Concrete:** Strait of Hormuz risk. ~20% of global oil supply (~20 mb/d) transits the Strait. Iran has periodically threatened closure. The risk is asymmetric: a small persistent premium in [[Brent Crude]] reflects non zero closure probability, but actual closure could spike oil $30 to $50/bbl immediately. Trade expression: long out of the money Brent calls (defined risk, convex payoff) vs paying persistent premium in outright longs. Russia sanctions (2022): geopolitical premium in European gas went from EUR 5 to 10/MWh pre 2022 to EUR 100+/MWh as the market priced in, then realized, Russian pipeline curtailment. The premium reflected potential disruption magnitude times the market's inability to substitute quickly.

**Simplified:** Markets pay a small insurance premium every day for the chance that something blows up in a sensitive region. Most days, nothing happens, and the premium looks like a tax. When it does happen, the price spikes far above the prior premium because the actual event is bigger than what was being priced. The right trade is usually long out of the money options, not outright long the commodity, because options pay the convex payoff without bleeding capital each day.

## Key mechanics and formulas

**Risk premium decomposition:**
`Commodity Price = Fundamental Value + Geopolitical Risk Premium + Speculative Premium`

The geopolitical premium is unobservable directly but can be estimated by comparing current prices to model implied fair values based on inventory, production, and demand.

**Geopolitical risk indices:**
- Caldara and Iacoviello Geopolitical Risk Index (GPR): text based index from news. Spikes correlate with oil price moves.
- Political Risk Services (PRS) Group: country level political risk scores

**Asymmetric payoff:**
Expected value of geopolitical risk in oil = Probability x Magnitude. A 5% chance of a 10 mb/d disruption lasting 1 month (~10% of global supply) could move price $30+/bbl. 5% x $30 = $1.50/bbl expected premium. This is why the premium seems small most of the time but produces outsized moves when events materialize.

## Prerequisites
- [[Supply Shock]]
- [[Forward Curve]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Supply Shock]] - geopolitical events are the primary cause of negative supply shocks in energy.
- [[Safe Haven Assets]] - cross asset response. Gold and JPY typically strengthen.
- [[Risk-On Risk-Off]] - escalation shifts markets to risk off, compressing equity/credit and supporting safe havens.
- [[Commodity Currencies]] - currencies of geopolitically exposed nations (RUB, IQD, NGN) are directly affected. Beneficiary nations (US shale = bullish CAD/USD) can strengthen.
- [[Brent Crude]] - the most geopolitically sensitive major benchmark due to seaborne exposure.
- [[Volatility]] - geopolitical risk spikes implied vol in energy options, creating vol trade opportunities.

## Common misconceptions

**"Geopolitical events always push prices up."** Only supply threatening events. Events that increase supply (Iran nuclear deal 2015 lifting sanctions, adding ~1 mb/d) push prices down.

**"The risk premium is wasted money."** The premium is insurance. Over long periods it looks like a cost (the Strait stays open most months). But the premium compensates for tail risk. Removing it leaves you unhedged against the worst case.

**"Markets panic for a long time after geopolitical events."** Most premiums decay within 1 to 4 weeks unless the event produces sustained supply loss. Pattern: spike, assess, fade. The 2019 Abqaiq attack removed 5.7 mb/d temporarily; Brent's $10/bbl spike fully reversed in 2 weeks once production restored.

## Sources

- Caldara and Iacoviello, "Measuring Geopolitical Risk" (2022, American Economic Review)
- IEA Emergency Response mechanisms (coordinated SPR release protocols)
- Platts: OPEC and geopolitical analysis
- Reuters, Bloomberg: real time geopolitical monitoring
