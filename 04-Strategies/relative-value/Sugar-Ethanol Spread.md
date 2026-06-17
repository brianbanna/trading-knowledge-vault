---
aliases: [sugar ethanol spread, sugar ethanol parity, hydrous parity, sugar ethanol arbitrage, mill mix, Brazilian mix, ethanol parity]
tags:
  - "#agri/softs/sugar"
  - "#energy/crude"
date-added: "2026-06-17"
---

# Sugar-Ethanol Spread

## Core Thesis

A Brazilian cane mill takes 1 input, sugarcane, and routes it to 2 outputs: crystallized sugar (exported, priced in USD on [[Sugar Futures|ICE No. 11]]) or ethanol (mostly domestic, priced in BRL). Every safra the mill sets a production mix based on a single question: per tonne of cane, do I make more money as sugar or as ethanol? It runs whichever pays. Aggregated across hundreds of Center South mills processing hundreds of millions of tonnes of cane, that choice determines how much sugar Brazil ships to the world. Brazil is roughly 40% of global raw sugar exports, so the aggregate mill mix is a primary driver of the world raw price.

The deeper structure: the mill's flex capacity is a production switching option on sugar parity vs ethanol parity. The value of the flexibility is option value, not a point estimate. This is the same object as [[Crack Spread|refinery yield switching]] (gasoline vs distillate) and fuel switching in power (gas vs coal, see [[Spark Spread]] when built). The sugar mill is the cleanest agricultural instance of it. Learn this as optionality, not as cane.

## Mechanics

### The Comparison: ATR and CONSECANA

The common denominator is ATR, Açúcar Total Recuperável, total recoverable sugar in kg per tonne of cane (roughly 140 kg/tonne). Brazil prices cane on ATR through the CONSECANA formula, and both the sugar and ethanol yields are expressed per tonne of cane. So the comparison is clean: R$ per tonne of cane as sugar vs R$ per tonne of cane as ethanol. Desks watch it as hydrous ethanol parity expressed in cents per pound sugar equivalent, sitting on the same axis as NY No. 11. When parity prints above No. 11, ethanol pays.

### Calculating the Break-even

Convert the sugar price (US cents/lb, ICE No. 11) into R$ per tonne of cane, convert the ethanol price (R$/litre, domestic) into R$ per tonne of cane, and compare.

**Sugar path (R$/t cane)** = sugar yield (lb/t cane) x No. 11 price (USD/lb) x BRL/USD
**Ethanol path (R$/t cane)** = ethanol yield (litres/t cane) x ethanol price (R$/litre)

The break-even is the point of indifference where the two are equal. It is **not fixed**. It moves with the USD sugar price, the BRL ethanol price, [[BRL/USD]] FX, blending mandates, CBios, export logistics, and each mill's technical flex.

### Entry / Read

This is not traded as a clean spread by a softs desk. It is used to project exportable Brazilian supply, which feeds a directional view on No. 11 outright or the [[White Premium|raw vs white spread]], or hedges a physical book. The output is a supply estimate feeding conviction, not a tradable signal.

- Parity above No. 11 (ethanol pays) leans the mix toward ethanol, cutting exportable sugar, supportive of No. 11.
- Parity below No. 11 (sugar pays) leans the mix toward sugar, raising exportable sugar, bearish No. 11.

## The Hidden Oil Beta (the part that moves billions and is missing from most framings)

The ethanol leg is not cleanly domestic or BRL insulated. Hydrous ethanol competes with gasoline at the pump for flex fuel cars, and drivers switch near 70% energy parity (ethanol carries less energy per litre). Brazilian gasoline is set by Petrobras with reference to international oil in USD, imperfectly and politically managed at times. So ethanol's ceiling is tethered to oil and to fuel tax policy (CIDE, PIS/COFINS, state ICMS).

Consequence: an oil rally can lift Brazilian pump gasoline, lift ethanol parity, pull mills toward ethanol, and cut sugar exports, moving No. 11 with no sugar specific news. **Sugar carries a hidden oil beta running through the Brazilian pump.** A desk modeling sugar supply without [[Crude Oil]] is missing its most mobile linkage.

Two adjacent levers:
- **Anhydrous vs hydrous ethanol.** Anhydrous is blended into gasoline under a mandate (historically ~27%, trending up) and is mandate driven baseline demand. Hydrous is the discretionary pump fuel doing the gasoline competing. The hydrous side carries the oil beta.
- **CBios (RenovaBio).** Tradable decarbonization credits that add to ethanol economics at the margin. Like the mandate, they nudge the break-even up or down; they do not change the switching logic.

## Instruments Used

- ICE No. 11 raw sugar (SB), 112,000 lbs, USD cents/lb, the export benchmark
- ICE No. 5 white sugar (London), for the raw vs white leg
- B3 hydrous ethanol futures (ETH) and CEPEA/ESALQ ethanol price reference, BRL/litre
- [[BRL/USD]] as the FX bridge between the two legs
- [[Crude Oil|Brent]] / Petrobras gasoline pricing as the input to the ethanol ceiling

## Risk Profile

| Metric | Description |
|--------|-------------|
| Primary Risk | Treating the mix as the only swing while ignoring Indian export policy (bans, quotas) and Thai output, which have been at least as large a shock to the world balance in recent years |
| Modeling Risk | Assuming symmetric flex. Ethanol is the easy direction; sugar is hardware constrained (crystallization, centrifuge capacity), so the flex is asymmetric |
| FX Double-count | Treating BRL/USD as a clean one way knob on the sugar side alone. Part of the ethanol side also moves with USD through gasoline |
| Timing Risk | Assuming weekly toggling. The strategic physical mix is set around and during the safra (April to December, Center South) with real switching frictions and inertia. Pricing and hedging move continuously; the physical mix does not |

## Edge Source

The edge is in modeling the switching option correctly, not in restating that mills choose. Specifically: estimating each mill's true technical flex range, tracking the oil-to-pump-to-ethanol chain that most sugar desks ignore, and pricing the optionality of the mill fleet rather than a point estimate of the mix. The aggregate of mill exercises is the market level supply response, the same logic as aggregate refinery yield exercise setting the product slate or aggregate power dispatch setting the supply curve.

## Where the Mix Range Actually Sits (correcting the common framing)

The often quoted 40% sugar / 60% ethanol to 60% / 40% range overstates the flex. Most mills cannot reach 60% sugar. Industry aggregate has historically run roughly 32% to 49% sugar, capped near 48 to 50% by crystallization and centrifuge capacity. The flex is asymmetric: ethanol is the easy, cheap direction; sugar is hardware constrained.

## When It Works / When It Fails

### Read Holds When
- Oil and BRL/USD move materially while the cane crop is stable, so the mix shift is the dominant supply variable
- Parity sits near the indifference point, where small moves in oil or FX flip marginal mills and the supply response is largest
- Indian and Thai balances are quiet, leaving Brazil as the clear swing

### Read Fails When
- Indian export policy dominates: an Indian export ban or a sudden quota release swamps the Brazilian mix effect on the world balance
- A Center South weather event (drought, frost) cuts the cane crop itself, so total sugar falls regardless of the mix
- The mill fleet is already hard against a capacity cap (max sugar), so a further bullish parity move cannot pull more sugar out, the switching option is out of the money

## Concrete Example

**Concrete:** Round numbers to show the mechanism, not a live quote. Inputs: No. 11 at 20 US cents/lb; BRL/USD at 5.0; mill ethanol at R$3.0/litre; per tonne of cane yields about 130 kg (287 lb) sugar or about 85 litres ethanol.

- Sugar path: 287 lb x $0.20 = $57.40/t cane x 5.0 = **R$287/t cane**
- Ethanol path: 85 L x R$3.0 = **R$255/t cane**
- R$287 vs R$255: sugar wins by R$32, mill leans max sugar.

Now move one variable at a time.

*Move 1, BRL strengthens to 4.5:* sugar is in USD, so a stronger BRL shrinks its R$ value. $57.40 x 4.5 = R$258. Ethanol is domestic, still R$255. R$258 vs R$255, basically a tie. Same 20 cent sugar price, FX alone nearly flipped the decision. This is why a sugar desk watches BRL/USD as hard as it watches No. 11.

*Move 2, oil rallies (FX back at 5.0):* higher oil lifts Brazilian pump gasoline, ethanol can be priced higher and still undercut it, say ethanol rises to R$3.3/litre. Ethanol path: 85 x R$3.3 = R$281. Sugar still R$287. The gap collapses from R$32 to R$6. Push oil a little more and ethanol wins, mills cut sugar, less sugar reaches the world market, and No. 11 rises with no sugar harvest problem anywhere. That is the hidden oil link buried inside the sugar price.

| Scenario | Sugar R$/t cane | Ethanol R$/t cane | Mill makes |
|----------|-----------------|-------------------|------------|
| Base: 20c, FX 5.0 | 287 | 255 | Sugar |
| BRL strengthens to 4.5 | 258 | 255 | Tie |
| Oil rallies, FX 5.0 | 287 | 281 | Almost ethanol |

**Simplified:** The mill is a switch. 3 things move which way it points: the USD sugar price, BRL/USD, and the ethanol price (secretly tied to oil through gasoline). When the switch points to ethanol, Brazil exports less sugar and the world price rises. Brazil is about 40% of global raw exports, so this single switch is a primary driver of the world sugar price. Mandates and CBios only nudge the break-even; they do not change the logic.

## The Probe

Oil rallies 20%, BRL flat, cane crop unchanged. Walk the chain to No. 11 and name every link. Skipping straight to "less sugar" skips the part that matters: oil up, Petrobras pump gasoline up, hydrous ethanol can price up and still undercut gasoline at the ~70% energy parity, ethanol parity rises above sugar parity, marginal mills shift cane to ethanol, exportable Brazilian sugar falls, and Brazil being ~40% of raw exports, the world balance tightens and No. 11 rises.

## Related Strategies
- [[Crack Spread]] is the energy analog: a refiner switching gasoline vs distillate yield on relative cracks, the same aggregate-exercise-sets-supply structure.
- [[Spark Spread]] (build when ready) is the power analog: a plant dispatching gas vs coal on spark vs dark, the flexible unit long a switching option.
- [[Inter-Commodity Spread]] is the general class this sits in.
- [[Crush Spread]] is the other agricultural processing spread, though crush has no switching option (fixed yield).
- [[Relative Value Trade]] for the broader framework.

## Related Concepts
- [[Sugar Futures]] for the contract, benchmarks, and the parity floor.
- [[BRL/USD]] is the FX bridge and a primary input to the mix decision.
- [[Crude Oil]] is the hidden beta through the Brazilian pump.
- [[White Premium]] is the raw vs white leg a desk often trades alongside the supply view.
- [[Seasonality]] of the Center South safra (April to December) sets when the mix is actually flexible.
- [[Optionality]] is the right lens: mill flex is a spread option, not a point estimate.

## Common Misconceptions
- **"The ethanol leg is domestic and BRL insulated."** Wrong. Hydrous ethanol is tethered to oil through pump gasoline competition, so sugar carries a hidden oil beta.
- **"Mills toggle the mix weekly."** Wrong. The strategic physical mix is set around the safra with real frictions and inertia; only pricing and hedging move continuously.
- **"Mills can run 60% sugar."** Mostly wrong. Sugar is hardware constrained near 48 to 50%; the flex is asymmetric, ethanol is the easy direction.
- **"Brazil is the only swing exporter."** Wrong. India (policy) and Thailand are comparable shocks to the world balance; tracking the mix while ignoring Indian policy is just as incomplete as the reverse.

## Sources
- CONSECANA (Conselho dos Produtores de Cana, Açúcar e Etanol) cane pricing methodology
- CEPEA/ESALQ ethanol and sugar price references
- RenovaBio / CBios program (ANP)
- ICE No. 11 and No. 5 contract specs
- USDA FAS and International Sugar Organization (ISO) for the global balance

---
*Status: #solid | Last reviewed: 2026-06-17*
