---
aliases: [continuous quoting, price quoting, market making quoting, making a market]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Quoting

## Definition

Quoting is the act of continuously showing [[Bid]] and [[Ask]] prices to the market, signaling willingness to buy and sell. It is the core activity of a [[Market Order|market maker]]. A quoting engine takes inputs like [[Mid Price]], [[Inventory]], [[Volatility]], and [[Adverse Selection]] estimates, then computes a [[Two Way Price]] and publishes it to one or more venues. The quotes must be updated constantly as conditions change, often hundreds or thousands of times per second in electronic markets.

## Why it matters (commodities and FX)

In FX, major dealers quote continuously on platforms like EBS, Refinitiv, Bloomberg, and their own [[Single Dealer Platform|SDPs]]. The ability to quote tighter than competitors while managing risk determines profitability. In commodities, LME ring dealers quote two way prices on base metals. The speed, accuracy, and intelligence of the quoting engine is the most important piece of technology a market maker owns.

## Concrete example

A bank's FX desk runs a quoting engine on [[EUR USD]]. The engine observes the current [[Mid Price]] at 1.08500 and the desk's target [[Half Spread]] of 0.3 [[Pip|pips]].

**Normal conditions:** The engine quotes 1.08497 / 1.08503. Clients trade against these prices. The desk earns the spread on each [[Round Trip]]. Daily revenue from quoting is approximately $80,000.

**Inventory builds:** A large client buys 50 million EUR, pushing the desk [[Long]] 50M. The engine applies [[Skew Microstructure|skew]], shifting quotes to 1.08494 / 1.08500, making the [[Ask]] more attractive to encourage sells that reduce inventory.

**Failure case:** During an ECB surprise rate cut, [[Volatility]] spikes. The engine widens the spread to 1.08470 / 1.08530 (6 pips wide) but latency causes a 200 millisecond delay in updating. A fast algo hits the [[Stale Quote|stale]] tight quote before the update arrives, costing the desk $35,000 on a single trade.

## Key mechanics and formulas

**Basic quoting formula (Avellaneda Stoikov framework):**

Bid = [[Reservation Price]] minus [[Half Spread]]
Ask = [[Reservation Price]] + [[Half Spread]]

Where:
- [[Reservation Price]] = [[Mid Price]] minus gamma * sigma^2 * q * (T minus t)
- gamma = risk aversion parameter
- sigma = [[Volatility]]
- q = current [[Inventory]] (positive = long, negative = short)
- T minus t = time remaining

**Key quoting parameters:**
- Spread width: wider in volatile or illiquid conditions
- Skew: shifts quotes based on inventory
- Quote size: how much volume shown at each price
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
- [[Reservation Price]] for the theoretical fair value adjusted for inventory and risk
- [[Adverse Selection]] for why some client flow is unprofitable to quote against
- [[Client Tiering]] for showing different spreads to different clients
- [[Stale Quote]] for the danger of not updating fast enough
- [[Kill Switch]] for emergency mechanisms to stop quoting instantly
- [[Internalization]] for matching flow internally rather than quoting externally

## Common misconceptions

1. **"Quoting means always showing the tightest spread."** Tight spreads attract volume but also attract [[Toxic Flow]]. Smart quoting widens for informed counterparties and tightens for uninformed ones via [[Client Tiering]].

2. **"A quoting engine just adds a spread around mid."** Real engines incorporate inventory skew, volatility scaling, adverse selection estimates, venue specific behavior, and dozens of other signals. The spread around mid is the starting point, not the answer.

3. **"More quotes means more profit."** Excessive quoting without [[Latency]] advantages leads to being adversely selected. Each quote is a free option given to the market. Quoting must be paired with the ability to cancel or update fast enough.

## Sources

- Avellaneda, M. and Stoikov, S., "High Frequency Trading in a Limit Order Book," 2008
- Cartea, A., Jaimungal, S., and Penalva, J., "Algorithmic and High Frequency Trading," Cambridge University Press
- Harris, Larry, "Trading and Exchanges," Oxford University Press
