---
aliases: [continuous quoting, price quoting, market making quoting, making a market]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Quoting

## Definition

Quoting is continuously showing [[Bid]] and [[Ask]] prices to the market, signaling willingness to buy and sell. It is the core activity of a [[Market Order|market maker]]. A quoting engine takes [[Mid Price]], [[Inventory]], [[Volatility]], and [[Adverse Selection]] estimates, computes a [[Two Way Price]], and publishes it to one or more venues. Quotes update constantly as conditions change, hundreds or thousands of times per second in electronic markets.

## Why it matters (commodities and FX)

In FX, major dealers quote continuously on EBS, Refinitiv, Bloomberg, and their own [[Single Dealer Platform|SDPs]]. Quoting tighter than competitors while managing risk determines profitability. In commodities, LME ring dealers quote two way prices on base metals. The speed, accuracy, and intelligence of the quoting engine is the most important technology a market maker owns.

## Concrete example

**Concrete:** Bank FX desk runs a quoting engine on [[EUR USD]]. Engine observes mid 1.08500 with target [[Half Spread]] 0.3 [[Pip|pips]]. Normal: quotes 1.08497 / 1.08503. Clients trade. Desk earns spread per [[Round Trip]]. Daily revenue ~$80,000. Inventory builds: large client buys 50M EUR, pushing desk [[Long]] 50M. Engine applies [[Skew Microstructure|skew]], shifting quotes to 1.08494 / 1.08500, making the [[Ask]] more attractive to attract sells reducing inventory. Failure: ECB surprise rate cut, [[Volatility]] spikes. Engine widens to 1.08470 / 1.08530 (6 pips) but latency causes 200ms delay updating. Fast algo hits the [[Stale Quote|stale]] tight quote before the update arrives, costing the desk $35,000 on a single trade.

**Simplified:** Quoting means continuously broadcasting buy and sell prices. The engine adjusts those prices for inventory, volatility, and client identity. Done right, the desk earns the spread on each round trip while keeping inventory manageable. Done wrong, you give away free options to fast counterparties.

## Key mechanics and formulas

**Basic quoting formula (Avellaneda Stoikov):**

Bid = [[Reservation Price]] - [[Half Spread]]
Ask = [[Reservation Price]] + [[Half Spread]]

Where:
- [[Reservation Price]] = [[Mid Price]] - gamma * sigma^2 * q * (T - t)
- gamma = risk aversion parameter
- sigma = [[Volatility]]
- q = current [[Inventory]] (positive = long, negative = short)
- T - t = time remaining

**Key quoting parameters:**
- Spread width: wider in volatile or illiquid conditions
- Skew: shifts quotes based on inventory
- Quote size: how much volume shown per price
- Update frequency: how often quotes refresh
- [[Last Look]] window: time to reject after client hits

## Prerequisites

- [[Bid]]
- [[Ask]]
- [[Two Way Price]]
- [[Mid Price]]
- [[Half Spread]]

## Related concepts (learn next)

- [[Skew Microstructure]] for how inventory drives asymmetric quote placement
- [[Reservation Price]] for the inventory and risk adjusted fair value
- [[Adverse Selection]] for why some client flow is unprofitable to quote against
- [[Client Tiering]] for showing different spreads to different clients
- [[Stale Quote]] for the danger of not updating fast enough
- [[Kill Switch]] for emergency mechanisms to stop quoting instantly
- [[Internalization]] for matching flow internally instead of quoting externally

## Common misconceptions

1. **"Quoting means showing the tightest spread."** Tight spreads attract volume and [[Toxic Flow]]. Smart quoting widens for informed counterparties and tightens for uninformed ones via [[Client Tiering]].

2. **"A quoting engine just adds a spread around mid."** Real engines incorporate inventory skew, vol scaling, adverse selection estimates, venue specific behavior, and dozens of other signals. The spread around mid is the start, not the answer.

3. **"More quotes means more profit."** Excessive quoting without [[Latency]] advantages gets adversely selected. Each quote is a free option to the market. Quoting must pair with the ability to cancel or update fast enough.

## Sources

- Avellaneda, M. and Stoikov, S., "High Frequency Trading in a Limit Order Book," 2008
- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
- Harris, Larry, "Trading and Exchanges," Oxford University Press
