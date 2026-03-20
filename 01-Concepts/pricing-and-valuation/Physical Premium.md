---
aliases: [physical premium, regional premium, delivery premium]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# Physical Premium

## Definition

A physical premium is the price paid above the exchange benchmark (e.g., [[LME]] or [[COMEX]]) for actual delivery of a physical commodity at a specific location. It covers freight, insurance, local taxes/duties, and the local supply/demand balance for physical material. Every physical metal transaction involves two components: the benchmark futures price and the premium. The premium varies by region, product form, and delivery terms. For example, copper [[Cathode]] delivered to Shanghai may command a $150/tonne premium over LME, while the same cathode in Rotterdam may carry only a $60/tonne premium. Premiums are assessed by price reporting agencies (Platts, Fastmarkets, CRU) and negotiated bilaterally.

## Why it matters (commodities and FX)

Physical premiums reveal information that futures prices cannot capture. A rising premium in one region signals local physical tightness even if the LME benchmark is flat or falling. Conversely, collapsing premiums signal local oversupply. For physical traders, premium differentials between regions create arbitrage opportunities: buy where premiums are low, ship where premiums are high. For financial traders, tracking premium trends provides a leading indicator of demand shifts. When Chinese copper premiums spike, it often precedes a rally in LME copper because it signals restocking demand.

## Concrete example

LME aluminum is at $2,400/tonne. The US Midwest premium spikes from $200 to $450/tonne due to Section 232 tariffs and domestic supply constraints. A US manufacturer now pays $2,850/tonne for physical aluminum vs $2,400 on the LME. A trader goes long the Midwest premium (via CME Midwest premium futures) at $300. As tariffs bite and domestic supply tightens, the premium rises to $500, earning $200/tonne. If tariffs are relaxed or imports surge, the premium could drop to $150, losing $150/tonne.

## Key mechanics and formulas

**Delivered price:** `Physical Price = Exchange Benchmark + Regional Premium`

**Premium components:**
- Freight (shipping cost from producer to delivery point)
- Insurance and handling
- Import duties and tariffs
- Local supply/demand balance
- Product form premium (e.g., wire rod vs cathode)

**Premium hedging:** CME lists futures on several physical premiums (US Midwest aluminum, European duty paid aluminum, Shanghai copper premium).

## Prerequisites

- [[LME]]
- [[Cathode]]
- [[Freight]]

## Related concepts (learn next)

- [[Cathode]] because cathode premiums are the most commonly traded physical premiums in copper.
- [[SHFE vs LME Arb]] because inter exchange premium differentials drive physical arb flows.
- [[LME Warehouse Stocks]] because low LME stocks in a region push up local premiums.
- [[Freight]] because shipping costs are a major component of physical premiums.
- [[Location Arbitrage]] because premium differentials across regions are the basis for location arbs.
- [[Cancelled Warrants]] because rising cancellations signal physical demand that supports premiums.

## Common misconceptions

**"The exchange price is the market price."** For physical metal, the exchange price is only the benchmark. Total cost always includes a premium that can be 5 to 20% of the base price.

**"Premiums move with the exchange price."** Premiums can move independently of or even opposite to the exchange price. LME can fall while local premiums rise during regional tightness.

**"All premiums are transparent."** Many premiums are negotiated privately between producer and consumer. Published assessments are indicative but may not capture all bilateral deals.

## Sources

- Fastmarkets: Global Physical Metal Premium Assessments
- CME Group: Aluminum Premium Futures Specifications
- CRU Group: Regional Metal Premium Analysis
