---
aliases: [prompt date, LME prompt date system, LME dating]
tags:
  - "#metals/base"
  - "#microstructure"
date-added: "2026-03-20"
---

# LME Prompt Date

## Definition

The LME prompt date system is the unique contract structure used by the [[LME]] where metals trade on specific calendar dates rather than standardized monthly expiry cycles. The key dates are: Cash (spot, delivery in 2 business days), Tom (next day), 3 Month (the most liquid benchmark date, rolling daily), and then monthly dates out to 15, 27, or 63 months depending on the metal. Between Cash and the 3 Month date, every individual business day is a tradeable prompt date, creating extremely granular term structure exposure. This system evolved from the LME's origins in the physical metal trade, where merchants needed to hedge specific delivery dates matching cargo arrival times.

## Why it matters (commodities and FX)

The prompt date system makes LME spread trading far more granular than on exchanges with monthly contracts. A trader can express a view on tightness over the next 5 days vs the next 10 days, which is impossible on CME or SHFE. The Tom/Next spread (tomorrow vs the next day) and the Cash/3M spread are the most actively traded and signal very short term and medium term physical tightness respectively. For algo traders, the daily prompt date structure creates a rich dataset for modeling term structure dynamics and carry signals. The system also means that every business day, some positions are expiring, creating continuous delivery pressure.

## Concrete example

LME copper 3 Month is at $9,800/tonne and Cash is at $9,850, a $50 backwardation. A trader goes long the Cash/3M spread at $50, expecting physical tightness to persist as a Chinese buying wave depletes warehouse stocks. If cancelled warrants surge and the backwardation widens to $120, she profits $70/tonne. If stocks unexpectedly build, the spread could flip to $20 contango, losing $70/tonne. The daily prompt dates let her precisely time the cash leg to match expected delivery demand.

## Key mechanics and formulas

**Key prompt dates:**
- Cash: T+2 (spot delivery)
- Tom: T+1 (next business day settlement)
- 3 Month: 3 calendar months from today (most liquid)
- Monthly: 3rd Wednesday of each month beyond 3 months

**Spread conventions:**
- Cash/3M: the benchmark carry/tightness spread
- Tom/Next: overnight carry rate, ultra short term signal
- Cash/3M contango (normal): reflects storage, insurance, financing costs
- Cash/3M backwardation: signals physical scarcity

## Prerequisites

- [[LME]]
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)

- [[Cash to 3 Month Spread]] because it is the primary spread derived from the prompt date structure.
- [[LME]] because the prompt date system is unique to the London Metal Exchange.
- [[Warrant]] because physical delivery on prompt dates involves warrant transfer.
- [[Contango Carry Metals]] because the prompt date system determines the carry economics.
- [[Backwardation Squeeze]] because daily expirations create continuous delivery pressure that can squeeze shorts.

## Common misconceptions

**"LME prompt dates work like monthly futures."** They do not. Every business day within 3 months is a separate tradeable date, creating far more contracts and spread combinations than monthly systems.

**"The 3 month contract is always the most important."** For spread traders, the Cash and nearby daily dates can be more relevant because they reflect immediate physical conditions.

**"Prompt dates are confusing and unnecessary."** The system exists because physical metal trading requires date specific hedging. A cargo arriving on March 15 needs a hedge expiring on March 15, not March 31.

## Sources

- LME: Prompt Date Calendar and Trading Conventions
- LME: Understanding the Prompt Date System (educational guide)
- Neil Buxton, The London Metal Exchange
