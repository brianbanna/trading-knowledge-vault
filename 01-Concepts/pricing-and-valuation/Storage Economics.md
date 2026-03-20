---
aliases: [storage economics, storage, inventory, inventory buffers, storage costs]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Storage Economics

## Definition

Storage economics encompasses the costs, capacity constraints, and strategic value of holding physical commodity inventories. Storage is the physical mechanism that links spot and futures prices through the [[Cost of Carry]] model. Storage costs include rental of tank space or warehouse, insurance, quality degradation (for perishables), and financing. Storage capacity is finite, and when it approaches full utilization, the market behaves very differently than when ample space is available. Inventories act as a buffer between supply and demand: when production exceeds consumption, inventories absorb the surplus; when consumption exceeds production, inventories are drawn.

## Why it matters (commodities and FX)

Storage is why [[Contango]] has an upper bound and why [[Backwardation]] signals real physical stress. In a contango market, the maximum spread between spot and futures is capped by the cost of renting storage, insuring the commodity, and financing the purchase (the "full carry" ceiling). If the spread exceeds full carry, arbitrageurs buy spot, store it, and sell futures for risk free profit, compressing the spread. When storage is nearly full, this arbitrage breaks down: you cannot store what you cannot store. This is when extreme contango or even negative prices emerge (WTI April 2020). Conversely, when inventories are low, [[Convenience Yield]] spikes because the option value of having physical supply is high.

## Concrete example

**Cushing, Oklahoma** (WTI delivery point): approximately 76 million barrels of working storage capacity. In April 2020, Cushing inventories reached ~65 million barrels (>85% utilization). With no available storage, traders holding expiring WTI futures could not take delivery. The May 2020 WTI contract settled at negative $37.63/bbl. The contango between May and June spiked to over $50, far beyond any normal carry cost, because the physical constraint of full storage made the front contract toxic.

Contrast with a low inventory environment: in late 2021, Cushing inventories fell to ~25 million barrels (~33% utilization). WTI went into steep backwardation ($2+ M1/M2 premium) because refiners valued immediate barrels highly and storage was freely available for anyone willing to sell.

**LME metals warehouses:** LME copper, aluminum, and zinc inventories in LME approved warehouses are reported daily. When LME copper stocks fall below 100,000 tonnes (approximately 2 days of global consumption), the market enters "low stock" territory. Backwardation steepens, and delivery squeezes become possible. When stocks exceed 500,000 tonnes, the curve trades near full carry.

## Key mechanics and formulas

**Full carry ceiling:**
`Max Contango = Storage Cost + Insurance + Financing`
`F_max = S x e^((r + c)(T-t))`

When futures trade above this level, cash and carry arbitrage is profitable.

**Storage utilization and cost:**
Storage rental rates are not linear. They follow a convex function of utilization:
- Below 50% utilization: low fixed rates, storage is a commodity itself
- 50 to 80%: rates rise gradually
- 80%+: rates spike nonlinearly as remaining capacity becomes scarce
- 95%+: effectively no storage available at any price

**Inventory buffer concept:**
`Days of Supply = Current Inventory / Daily Consumption Rate`

This normalizes inventories across different markets. 30 days of supply in crude oil is comfortable. 15 days is tight. 5 days is a crisis.

**Injection/withdrawal rates (natgas, oil):**
Physical storage has rate constraints. A salt cavern natgas facility might inject 200 MMcf/day and withdraw 500 MMcf/day. You can draw faster than you build. This asymmetry affects curve shape: winter drawdowns can be sharper than summer builds.

## Prerequisites
- [[Forward Curve]]
- [[Cost of Carry]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Convenience Yield]] - the benefit of holding physical inventory vs futures. Convenience yield is the "return" on storage, and it rises when inventories are low.
- [[Calendar Spread]] - directly trades storage economics. When storage is expensive and scarce, calendar spreads reflect it.
- [[Supply Shock]] - storage buffers absorb supply shocks. The size of the buffer determines how much price adjustment is needed.
- [[Cost of Carry]] - storage cost is the "c" in the carry formula. Understanding actual storage costs (not textbook estimates) is critical.
- [[Seasonality]] - storage injection/withdrawal cycles create seasonal patterns in inventories and spreads.
- [[Location Arbitrage]] - storage availability at different locations creates locational price differentials.

## Common misconceptions

**"Inventories only matter at extremes."** The rate of change matters more than the level. A market drawing from 40 to 30 days of supply is tightening aggressively even though 30 days is "comfortable." Traders watch the trajectory, not the snapshot.

**"Storage is always available at the quoted rate."** Storage markets have their own supply/demand. During oversupply periods, floating storage (oil tankers used as storage at sea) emerges because onshore capacity is full. Floating storage rates are much higher than onshore, shifting the full carry ceiling.

**"All storage is equal."** Cushing tankage vs Gulf Coast caverns vs Rotterdam tanks have different access, costs, and delivery logistics. A trader needs to know which storage counts for benchmark delivery and which is stranded.

## Sources

- EIA Weekly Petroleum Status Report (Cushing inventory data)
- GIE (Gas Infrastructure Europe): European gas storage data
- LME warehouse stock reports (daily)
- CME Group: Understanding Crude Oil Storage and Delivery
- Knittel and Pindyck, "The Simple Economics of Commodity Price Speculation" (2016)
