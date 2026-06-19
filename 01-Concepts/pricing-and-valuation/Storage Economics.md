---
aliases: [storage economics, storage, inventory, inventory buffers, storage costs]
tags:
  - "#energy"
  - "#metals"
date-added: "2026-03-20"
---

# Storage Economics

## Definition

Storage economics covers the costs, capacity constraints, and strategic value of holding physical commodity inventories. Storage is the physical mechanism linking spot and futures prices through the [[Cost of Carry]] model. Costs include tank or warehouse rental, insurance, quality degradation (perishables), and financing. Capacity is finite; behavior changes drastically near full utilization. Inventories buffer supply and demand: surplus production builds stocks, surplus consumption draws them.

## Why it matters (commodities and FX)

Storage is why [[Contango]] has an upper bound and why [[Backwardation]] signals real physical stress. In contango, the spot to futures spread is capped by storage rent, insurance, and financing (the full carry ceiling). Above full carry, arbitrageurs buy spot, store it, sell futures for riskless profit, compressing the spread. When storage is full, the arbitrage breaks: you cannot store what you cannot store. Extreme contango or negative prices emerge (WTI April 2020). When inventories are low, [[Convenience Yield]] spikes because the option value of physical supply is high.

## Concrete example

**Concrete:** Cushing, Oklahoma (WTI delivery point): 76 million barrels working capacity. April 2020, Cushing inventories reached 65 million barrels (>85% utilization). With no storage available, holders of expiring WTI could not take delivery. May 2020 WTI settled at −$37.63/bbl. Contango between May and June spiked above $50, far beyond normal carry, because full storage made the front contract toxic. Contrast: late 2021, Cushing at 25 million barrels (33% utilization). WTI in steep backwardation ($2+ M1/M2) because refiners valued prompt barrels and storage was freely available.

**Simplified:** Storage tanks have a maximum size. When tanks are nearly full, no one will buy more physical oil because they have nowhere to put it, so the spot price collapses. When tanks are nearly empty, anyone holding physical has something rare, so spot trades at a premium to futures. The shape of the curve and the level of prices both depend on whether the tanks are filling up or draining down.

## Key mechanics and formulas

**Full carry ceiling:**
`Max Contango = Storage Cost + Insurance + Financing`
`F_max = S x e^((r + c)(T-t))`

Above this, [[Cash and Carry Arbitrage|cash and carry arbitrage]] is profitable.

**Storage utilization and cost:**
Rental rates are convex in utilization:
- Below 50%: low fixed rates, storage is a commodity itself
- 50 to 80%: rates rise gradually
- 80%+: rates spike nonlinearly as remaining capacity becomes scarce
- 95%+: effectively no storage at any price

**Inventory buffer:**
`Days of Supply = Current Inventory / Daily Consumption Rate`

Normalizes inventories across markets. 30 days crude is comfortable, 15 is tight, 5 is a crisis.

**Injection/withdrawal rates (natgas, oil):**
Storage has rate constraints. A salt cavern natgas facility might inject 200 MMcf/day, withdraw 500 MMcf/day. Asymmetry: draw faster than build. Winter drawdowns are sharper than summer builds.

## Prerequisites
- [[Forward Curve]]
- [[Cost of Carry]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)
- [[Convenience Yield]] - the benefit of holding physical inventory versus futures. Rises when inventories are low.
- [[Calendar Spread]] - directly trades storage economics.
- [[Supply Shock]] - storage buffers absorb shocks. Buffer size determines how much price must move.
- [[Cost of Carry]] - storage cost is the "c" in the carry formula.
- [[Seasonality]] - injection/withdrawal cycles create seasonal patterns in inventories and spreads.
- [[Location Arbitrage]] - storage availability at different locations creates locational differentials.

## Common misconceptions

**"Inventories only matter at extremes."** Rate of change matters more than level. A market drawing from 40 to 30 days of supply is tightening aggressively even though 30 days is comfortable. Watch the trajectory.

**"Storage is always available at the quoted rate."** Storage markets have their own supply/demand. During oversupply, floating storage (tankers used as storage at sea) emerges because onshore is full. Floating rates are much higher, shifting the full carry ceiling.

**"All storage is equal."** Cushing tankage versus Gulf Coast caverns versus Rotterdam tanks have different access, costs, and delivery logistics. Know which storage counts for benchmark delivery and which is stranded.

## Sources

- EIA Weekly Petroleum Status Report (Cushing inventory data)
- GIE (Gas Infrastructure Europe): European gas storage data
- LME warehouse stock reports (daily)
- CME Group: Understanding Crude Oil Storage and Delivery
- Knittel and Pindyck, "The Simple Economics of Commodity Price Speculation" (2016)
