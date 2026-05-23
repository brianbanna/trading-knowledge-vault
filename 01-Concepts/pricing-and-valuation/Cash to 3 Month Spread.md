---
aliases: [cash-3M spread, LME spread, cash to three month]
tags:
  - "#metals/base"
date-added: "2026-03-20"
---

# Cash to 3 Month Spread

## Definition

The Cash to 3 Month spread is the difference between the [[LME]] Cash (spot) price and the 3 Month forward price for a base metal. The LME equivalent of the front month calendar spread in oil and the single most important indicator of physical supply tightness for base metals. Cash above 3 Month (backwardation) signals physical metal is scarce and buyers pay a premium for immediate delivery. 3 Month above Cash (contango) signals comfortable supply, with storage and financing costs setting spread width.

## Why it matters (commodities and FX)

The Cash/3M spread is where physical and financial metals markets converge. Physical traders watch it to decide whether buying and storing metal is economic (contango carry trade) or delivering metal is more profitable (backwardation). Financial traders use it as a leading indicator for flat price direction: widening backwardation precedes price rallies; widening contango signals building oversupply. Extreme backwardation (squeeze conditions) generates massive short term P&L swings on anyone with short positions approaching Cash delivery.

## Concrete example

**Concrete:** LME copper Cash $9,900/tonne, 3 Month $9,750: $150 backwardation. A short Cash/3M spread (positioned for backwardation to narrow) is exposed. A Chile mine strike tightens copper supply; backwardation widens to $300. Short spread loses $150/tonne. Long Cash/3M (bet on continued tightness) gains $150/tonne. If the strike resolves and Chinese demand disappoints, the spread flips to $30 contango. Short spread now profits ~$180/tonne from the move.

**Simplified:** The spread tells you whether physical copper is hard or easy to get right now. If the spot price is higher than the 3 month forward, physical is scarce: people pay extra to take delivery today instead of waiting. If the forward is higher, there is enough metal around that nobody pays a premium for immediate delivery. Watching the spread move tells you which way physical conditions are headed before flat prices catch up.

## Key mechanics and formulas

**Spread calculation:** `Cash/3M Spread = Cash Price − 3 Month Price`

**Interpretation:**
- Positive spread = backwardation (physical tightness)
- Negative spread = contango (comfortable supply)

**Contango carry economics:** `Maximum Contango ≈ LME Rent + Insurance + Financing Cost (3 months)`

Typical: $30 to $80/tonne for copper depending on rates and LME rent.

**Key signals:**
- Backwardation > $100/tonne (copper): significant tightness, potential squeeze
- Contango > $60/tonne (copper): very comfortable, carry trade profitable

## Prerequisites

- [[LME]]
- [[LME Prompt Date]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)

- [[LME Prompt Date]] because the Cash/3M spread is defined by the LME prompt date structure.
- [[Backwardation Squeeze]] because extreme Cash/3M backwardation signals squeeze conditions.
- [[Contango Carry Metals]] because contango width determines whether physical carry is profitable.
- [[LME Warehouse Stocks]] because inventory changes drive the spread.
- [[Cancelled Warrants]] because rising cancellations signal physical demand and backwardation pressure.
- [[Warrant]] because delivery on the Cash date involves warrant transfer.

## Common misconceptions

**"The Cash/3M spread is the same as the front month spread in oil."** Mechanics differ. LME has daily prompt dates, not monthly contracts. The Cash date is a specific rolling delivery date.

**"Backwardation always means prices will go up."** Backwardation signals tightness but flat price can decline if macro demand weakens, even while the spread stays backwardated.

**"Contango means the metal is cheap."** Contango reflects adequate supply and storage economics. Says nothing about whether the outright price is high or low vs fundamentals.

## Sources

- LME: Spread Trading Guide
- CRU Group: Base Metals Spread Analysis
- Neil Buxton, The London Metal Exchange
