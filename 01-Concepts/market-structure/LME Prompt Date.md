---
aliases: [prompt date, LME prompt date system, LME dating]
tags:
  - "#metals/base"
  - "#microstructure"
date-added: "2026-03-20"
---

# LME Prompt Date

## Definition

The LME prompt date system is the contract structure where metals trade on specific calendar dates rather than standardized monthly expiries. Key dates: Cash (spot, T+2), Tom (next day), 3 Month (most liquid benchmark, rolling daily), then monthly out to 15, 27, or 63 months depending on metal. Between Cash and 3 Month, every business day is a tradeable prompt date, creating granular term structure exposure. The system evolved from the LME's physical metal trade origins, where merchants hedged specific cargo arrival dates.

## Why it matters (commodities and FX)

The system makes LME spread trading far more granular than exchanges with monthly contracts. A trader expresses a view on tightness over the next 5 days vs 10 days, impossible on CME or SHFE. Tom/Next (tomorrow vs the day after) and Cash/3M are the most traded and signal ultra short term and medium term physical tightness. For algo traders, daily prompts create a rich dataset for term structure dynamics and carry signals. Every business day some positions expire, creating continuous delivery pressure.

## Concrete example

**Concrete:** LME copper 3M trades at $9,800/tonne, Cash at $9,850: $50 backwardation. A trader goes long Cash/3M at $50, expecting physical tightness to persist as Chinese buying depletes warehouse stocks. Cancelled warrants surge, the backwardation widens to $120, profit $70/tonne. If stocks instead build unexpectedly, the spread flips to $20 contango, losing $70/tonne. Daily prompts let her time the cash leg to match expected delivery demand precisely, something impossible on a monthly contract grid.

**Simplified:** Every business day for the next 3 months is its own tradeable date. You can trade "today vs tomorrow" or "today vs next Friday" instead of being forced into monthly buckets. Useful when physical metal needs to be delivered on a specific cargo arrival date, which is the whole point of the LME.

## Key mechanics and formulas

**Key prompt dates:**
- Cash: T+2 (spot delivery)
- Tom: T+1 (next business day settlement)
- 3 Month: 3 calendar months from today (most liquid)
- Monthly: 3rd Wednesday of each month beyond 3 months

**Spread conventions:**
- Cash/3M: the benchmark carry/tightness spread
- Tom/Next: overnight carry rate, ultra short term signal
- Cash/3M contango (normal): reflects storage, insurance, financing
- Cash/3M backwardation: signals physical scarcity

## Prerequisites

- [[LME]]
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)

- [[Cash to 3 Month Spread]]: primary spread from the prompt date structure
- [[LME]]: prompt dates are unique to the London Metal Exchange
- [[Warrant]]: physical delivery on prompt dates involves warrant transfer
- [[Contango Carry Metals]]: prompts determine carry economics
- [[Backwardation Squeeze]]: daily expirations create continuous squeeze potential

## Common misconceptions

**"LME prompt dates work like monthly futures."** They do not. Every business day within 3 months is a separate tradeable date, far more contracts than monthly systems.

**"The 3 month is always most important."** For spread traders, Cash and nearby daily dates can matter more because they reflect immediate physical conditions.

**"Prompt dates are confusing and unnecessary."** The system exists because physical metal trading needs date specific hedging. A cargo arriving March 15 needs a hedge expiring March 15, not March 31.

## Sources

- LME: Prompt Date Calendar and Trading Conventions
- LME: Understanding the Prompt Date System (educational guide)
- Neil Buxton, The London Metal Exchange
