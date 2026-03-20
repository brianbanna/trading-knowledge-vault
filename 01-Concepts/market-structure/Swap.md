---
aliases: [swap, commodity swap, price swap, OTC swap]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Swap

## Definition
A commodity swap is an OTC agreement between 2 parties to exchange cash flows based on a commodity price index over a specified period. In the most common structure (a fixed for floating swap), one party pays a fixed price and receives the floating (market) price, while the counterparty does the opposite. For example, an oil producer might enter a swap to receive a fixed $80/bbl and pay the monthly average of Brent crude, effectively locking in a selling price for its production. Banks and trading houses act as intermediaries, earning the bid/ask spread between the fixed prices they quote to producers versus consumers. Swaps are settled in cash with no physical delivery, and settlements occur at periodic intervals (monthly, quarterly) over the life of the contract. A swap can be understood as a strip of [[Forward Contract|forward contracts]], one for each settlement period. Swaps are the primary hedging tool for commodity producers and consumers who need customized tenor, volume profiles, and index references that exchange traded [[Futures Contract|futures]] cannot provide.

## Why it matters (commodities and FX)
Swaps are the workhorse of commodity hedging across energy, metals, and agriculture. Airlines hedge jet fuel exposure, copper miners hedge production revenue, and utilities hedge natural gas procurement costs, overwhelmingly through swaps rather than futures. The swap market is substantially larger than the futures market in many commodities because swaps can match exact production schedules, custom price indexes (e.g., Platts JKM for Asian LNG), and specific delivery periods. For traders, the swap curve provides additional price information beyond the futures curve, especially for maturities and indexes not covered by exchange contracts. Post 2008 reforms under Dodd Frank and EMIR have pushed many standardized swaps toward central clearing, reducing counterparty risk.

## Concrete example
**Success case:** A copper miner expects to produce 5,000 tonnes over the next 12 months and enters a fixed for floating swap at $9,500/tonne with monthly settlements against the LME cash copper average. In a month when LME averages $8,800/tonne, the miner receives $700/tonne from the swap counterparty (approximately 417 tonnes that month x $700 = $291,900). Combined with the $8,800 physical sale price, the miner's effective revenue is the locked in $9,500/tonne. The hedge provided $291,900 of incremental revenue that month.

**Failure case:** In a month when LME averages $10,200/tonne, the miner pays $700/tonne to the counterparty ($291,900 outflow). The miner sells physical copper at $10,200 but nets only $9,500 after the swap payment. If copper continues to $11,000, the miner watches competitors earn $1,500/tonne more. The lesson: swaps lock in both upside and downside. The opportunity cost of hedging is real and can be substantial in strong bull markets.

## Key mechanics and formulas
- **Fixed for floating swap payoff (per period):** Net payment = (Fixed price - Floating price) x Notional quantity. If positive, the floating payer (producer) receives; if negative, the fixed payer (consumer) receives.
- **Swap pricing:** The fixed price is set so that the present value of all expected future cash flows equals zero at initiation (par swap). This is equivalent to the weighted average of the forward curve over the swap tenor.
- **Par swap rate = Sum of (Forward price x Discount factor x Quantity) / Sum of (Discount factor x Quantity)**
- **Key participants:** Producers (receive fixed, pay floating), Consumers (pay fixed, receive floating), Banks/dealers (intermediate, earn bid/ask)
- **Basis swap:** Both legs are floating but reference different indexes (e.g., Brent vs. Dubai crude). Used to hedge location or quality basis.

## Prerequisites
- [[Futures Contract]]
- [[Forward Contract]]
- [[Cash Settlement]]

## Related concepts (learn next)
- [[Forward Contract]] is the building block: a swap is effectively a series of forwards with periodic cash settlements.
- [[Futures Contract]] is what dealers use to hedge their swap exposure, creating a linkage between OTC and exchange markets.
- [[Cash Settlement]] is the mechanism through which swap payments are made; no physical commodity changes hands.
- [[Basis Risk]] arises when a swap references one price index but the hedger's actual exposure is linked to a different one.
- [[Implied Volatility]] is relevant when pricing swaptions (options on swaps) that give the holder the right to enter a swap.
- [[Margin]] requirements for cleared swaps mirror futures margin, requiring initial and variation margin.
- [[Option]] structures can be combined with swaps (e.g., collars, participating swaps) to allow partial upside participation.

## Common misconceptions
- **"Swaps are risky exotic instruments."** They are straightforward hedging tools used by virtually every commodity producer and consumer globally. The fixed for floating mechanic is conceptually identical to locking in a price.
- **"Swaps and futures are interchangeable."** Swaps offer customization (index, tenor, quantity profile) that futures cannot match, but carry counterparty risk (even with clearing) and are less liquid in the secondary market.
- **"Only banks can trade swaps."** While banks are the primary intermediaries, trading houses, hedge funds, pension funds, and corporates all participate actively in the commodity swap market.

## Sources
- John Hull, "Options, Futures, and Other Derivatives"
- CME Group, "OTC Clearing for Commodity Swaps"
- ISDA, "Commodity Derivatives Definitions and Documentation Standards"
- McDonald, R., "Derivatives Markets"
