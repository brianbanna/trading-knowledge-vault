---
aliases: [swap, commodity swap, price swap, OTC swap]
tags:
  - "#microstructure"
date-added: "2026-03-20"
---

# Swap

## Definition
A commodity swap is an OTC agreement between 2 parties to exchange cash flows based on a commodity index over a specified period. In the standard fixed for floating structure, one party pays a fixed price and receives the floating (market) price; the counterparty does the opposite. An oil producer enters a swap to receive a fixed $80/bbl and pay the monthly average of Brent, effectively locking in a selling price. Banks and trading houses intermediate, earning the bid/ask between fixed prices quoted to producers vs consumers. Swaps settle in cash with no physical delivery, periodically (monthly, quarterly) over the contract life. A swap is conceptually a strip of [[Forward Contract|forwards]], one per settlement period. Swaps are the primary hedging tool for producers and consumers needing custom tenor, volume profiles, and index references that exchange traded [[Futures Contract|futures]] cannot match.

## Why it matters (commodities and FX)
Swaps are the workhorse of commodity hedging across energy, metals, agriculture. Airlines hedge jet fuel, copper miners hedge production revenue, utilities hedge gas procurement: overwhelmingly through swaps rather than futures. The swap market is substantially larger than the futures market in many commodities because swaps match exact production schedules, custom indexes (Platts JKM for Asian LNG), and specific delivery periods. For traders, the swap curve provides additional price information beyond futures, especially for maturities and indexes not covered by exchange contracts. Post 2008 reforms (Dodd Frank, EMIR) pushed many standardized swaps toward central clearing, cutting counterparty risk.

## Concrete example

**Concrete:** A copper miner expects 5,000 tonnes production over the next 12 months and enters a fixed for floating swap at $9,500/tonne with monthly settlement vs LME cash copper average. In a month when LME averages $8,800, the miner receives $700/tonne from the counterparty (~417 tonnes × $700 = $291,900). Combined with the $8,800 physical sale, the miner's effective revenue is the locked $9,500. The hedge added $291,900 that month. Adverse month: LME averages $10,200. Miner pays $700/tonne to the counterparty ($291,900 outflow). Physical sells at $10,200 but nets only $9,500 after the swap. Copper continues to $11,000 and the miner watches unhedged competitors earn $1,500/tonne more. Swaps lock both upside and downside. Opportunity cost is real.

**Simplified:** A long term agreement to swap a fixed price for a floating market price each month. Producer locks in revenue, consumer locks in cost. Custom tenor, custom volume, any index. Settled in cash, no physical delivery. Think of it as a series of monthly forwards bundled into one contract.

## Key mechanics and formulas
- **Fixed for floating payoff (per period):** Net payment = (Fixed price minus Floating price) × Notional quantity. Positive: floating payer (producer) receives. Negative: fixed payer (consumer) receives.
- **Swap pricing:** fixed price set so PV of expected future cash flows = 0 at initiation (par swap). Equivalent to the weighted average of the forward curve over the tenor.
- **Par swap rate** = Sum of (Forward price × Discount factor × Quantity) / Sum of (Discount factor × Quantity)
- **Key participants:** Producers (receive fixed, pay floating), Consumers (pay fixed, receive floating), Banks/dealers (intermediate)
- **Basis swap:** both legs floating but referencing different indexes (Brent vs Dubai). Used to hedge location or quality basis.

## Prerequisites
- [[Futures Contract]]
- [[Forward Contract]]
- [[Cash Settlement]]

## Related concepts (learn next)
- [[Forward Contract]]: building block; a swap is a series of forwards with periodic cash settlement
- [[Futures Contract]]: what dealers use to hedge swap exposure, linking OTC and exchange markets
- [[Cash Settlement]]: mechanism for swap payments; no commodity changes hands
- [[Basis Risk]]: arises when the swap index differs from the hedger's actual exposure
- [[Implied Volatility]]: relevant for swaptions (options on swaps)
- [[Margin]]: cleared swaps require initial and variation margin like futures
- [[Option]] structures combine with swaps (collars, participating swaps) for partial upside

## Common misconceptions
- **"Swaps are risky exotic instruments."** Straightforward hedging tools used by virtually every commodity producer and consumer globally. Fixed for floating is conceptually identical to locking in a price.
- **"Swaps and futures are interchangeable."** Swaps offer customization (index, tenor, profile) futures cannot, but carry counterparty risk (even cleared) and are less liquid in secondary trading.
- **"Only banks trade swaps."** Banks are the primary intermediaries, but trading houses, hedge funds, pension funds, and corporates all participate actively.

## Sources
- John Hull, "Options, Futures, and Other Derivatives"
- CME Group, "OTC Clearing for Commodity Swaps"
- ISDA, "Commodity Derivatives Definitions and Documentation Standards"
- McDonald, R., "Derivatives Markets"
