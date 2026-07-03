---
aliases: [process margin, processing margin, transformation spread, conversion spread, production margin]
tags:
  - "#energy/refined"
  - "#agri"
date-added: "2026-07-03"
---

# Process Margin

## Definition
A process margin is the value of the outputs minus the cost of the inputs, earned by whoever physically converts one into the other. It is the single shape behind a whole family of commodity spreads. A refiner turns crude into gasoline and diesel and earns the [[Crack Spread]]. A crusher turns soybeans into meal and oil and earns the [[Crush Spread]]. A gas fired power plant turns gas into electricity and earns the spark spread. Same structure every time: buy the input, sell the transformed output, live on the gap. Whoever runs the physical conversion asset is structurally long its process margin, because that margin is literally their operating profit per unit processed.

## Why it matters (commodities and FX)
Once you see the pattern in the crack spread you see it across the complex, and it gives you two things at once. First, a hedge: the converter locks a fat margin by selling the spread, shorting the output futures and buying the input futures, freezing operating profit regardless of where flat prices go. Second, a signal: the process margin reads the health of conversion demand in real time. A wide margin means the asset runs hard and pulls more input, a narrow or negative margin means it cuts runs, often the early tell before the input's flat price reacts. For a freight seat this is not abstract. Bunker fuel is a refined product, so the [[Scrubber Spread]] (VLSFO minus HSFO) is a process margin sitting directly on the bunker bill, and when it widens, scrubber fitted ships burning cheap HSFO gain a cost edge that shifts vessel economics and TCE.

## Concrete example
**Concrete:** The canonical instance is the 3:2:1 [[Crack Spread]]. WTI = 80.00/bbl, RBOB gasoline = 2.30/gal (× 42 = 96.60/bbl), ULSD diesel = 2.45/gal (× 42 = 102.90/bbl). Margin = (2 × 96.60 + 1 × 102.90 − 3 × 80.00) / 3 = 18.70/bbl of crude processed. Now apply the identical template to two other assets:

- **Crush (soybeans to meal + oil):** margin = (meal value + oil value per bushel) − soybean price. Same subtraction, different units to align (meal in USD per short ton, oil in cents per pound, beans in USD per bushel).
- **Spark (gas to power):** margin = power price − (gas price × heat rate). The heat rate is the yield: MMBtu of gas needed per MWh of electricity. A 7.5 heat rate at 3.00/MMBtu gas and 30/MWh power gives 30 − 22.50 = 7.50/MWh.

Case it works: the plant operator sees a fat spark spread, sells forward power and buys forward gas, and banks the 7.50/MWh even if both flat prices halve. Case it fails: the operator locks the margin, then the spread widens further and the capped upside is opportunity cost, or the yield assumption (heat rate, crush yield, crack ratio) does not match the real asset and residual [[Basis Risk]] leaks P&L.

**Simplified:** Anyone who buys a raw thing and sells a finished thing makes money on the gap between them. That gap is the process margin. Every one of these spreads (crack, crush, spark) is the same bet with different inputs: is it profitable to run the machine right now.

## Key mechanics and formulas
- **General form:** margin = Σ (output_i price × yield_i) − Σ (input_j price × rate_j), normalized per unit of the primary input processed.
- **Unit alignment first.** Inputs and outputs almost always quote in different units (barrels vs gallons, bushels vs pounds, MMBtu vs MWh). Convert everything to a common basis before subtracting, the single most common error.
- **The yield ratio is the model.** 3:2:1 for a crack, the crush yield for beans, the heat rate for a spark spread. It is a fixed proxy for a variable real yield, so the paper margin diverges from any specific asset's true margin.
- **Restoring force.** When a margin blows out, the converter tilts its yield toward the rich output (cracker severity, crush slate, dispatch order), pulling more to market and partially closing the spread. This self correction works only while the asset has swing room.
- **Where it breaks.** When capacity binds, the asset is already flat out and cannot shift yield further, so the margin stops mean reverting and can run far past what looks reasonable. That is the difference between a spread you fade and one you respect.

## Prerequisites
- [[Crack Spread]]
- [[Relative Value Trade]]
- [[Basis Risk]]

## Related concepts (learn next)
- [[Crack Spread]]: crude to gasoline plus distillate, the refiner's margin and the archetype of the family.
- [[Crush Spread]]: soybeans to meal plus oil, the crusher's margin, same template in agriculture.
- [[Scrubber Spread]]: VLSFO minus HSFO, the marine fuel process margin that lands on the freight bunker bill.
- [[Spark Spread]]: natural gas to electricity, the gas fired power plant's margin, yield set by the heat rate.
- [[Dark Spread]]: coal to electricity, the coal plant's margin, the spark spread's dirtier cousin.
- [[Quality Spread]]: the input side cousin, the discount a lower quality input trades at, which a complex converter captures as extra margin.
- [[Seasonality]]: process margins swing with the demand calendar of their outputs, gasoline in summer, distillate and heating in winter.

## Common misconceptions
1. **The paper process margin is a real asset's margin.** It is a proxy built on a fixed yield ratio and benchmark prices. Any specific refiner, crusher, or power plant earns location and configuration specific prices, so its true margin diverges.
2. **A blown out margin always mean reverts.** Only while the converter has yield swing room. When the binding constraint is total capacity rather than slate mix, the restoring force is gone and fading the spread gets run over. Fade when there is slack, respect it when the system is flat out.

## Sources
- CME Group. *Crack Spread Handbook* and process spread contract guides.
- Eydeland, Alexander and Krzysztof Wolyniec. *Energy and Power Risk Management*, chapters on spark and dark spreads.
- Geman, Hélyette. *Commodities and Commodity Derivatives*, sections on processing and transformation spreads.
