---
aliases: [CFD, contract for differences, Brent CFD, cargo CFD]
tags:
  - "#energy/crude/brent"
date-added: "2026-03-20"
---

# CFD Crude

## Definition

In crude oil markets, a CFD (Contract for Differences) is the spread between [[Dated Brent]] (the physical spot price for North Sea crude) and the front month [[Brent Crude]] futures contract. It is not the same as a retail FX CFD. The oil CFD captures the short term divergence between the physical and paper markets. It trades as a series of weekly contracts, each settling against the Platts Dated Brent assessment for that week minus the relevant Brent futures month. CFDs are one of the most actively traded instruments among physical trading houses, prop desks, and hedge funds focused on short term oil market dynamics.

## Why it matters (commodities and FX)

The CFD is the most sensitive real time indicator of physical crude oil market tightness. When the CFD is positive (Dated Brent above futures), the physical market is tight and cargoes are scarce. When the CFD is negative, the physical market is loose and cargoes are easy to source. Physical traders use CFDs to manage the basis risk between their cargo purchases (priced off Dated Brent) and their futures hedges (ICE Brent). Prop traders use CFDs as a high frequency directional signal: persistent positive CFDs typically precede futures curve tightening.

## Concrete example

A physical trader buys a Forties cargo at Dated Brent + $0.20 differential for delivery in 2 weeks. She hedges by selling Brent futures. Her exposure is now the CFD plus the $0.20 differential. If the CFD is at +$0.80 when she prices, her effective sell price relative to futures is $1.00 above the flat price hedge. If the physical market loosens and the CFD drops to minus $0.30, her Dated Brent realization would be $0.30 below futures instead of above, and the cargo trade loses on the basis. The CFD volatility is the primary risk she manages.

## Key mechanics and formulas

**CFD calculation:** `CFD = Dated Brent Assessment - Brent Front Month Futures`

**Contract structure:** Weekly CFDs settle against the average Platts Dated Brent assessment for each week of the month, minus the corresponding Brent futures month.

**Typical range:** minus $1.50 to plus $2.00, but can spike to +$3 or more during acute physical tightness.

**Traded on:** OTC, brokered by Tullett Prebon, ICAP, and others. ICE also lists Brent CFD swaps.

## Prerequisites

- [[Dated Brent]]
- [[Brent Crude]]
- [[Platts Window]]
- [[Backwardation]]

## Related concepts (learn next)

- [[Dated Brent]] because the CFD is defined as the spread between Dated Brent and futures.
- [[Platts Window]] because the Dated Brent assessment that determines CFD settlement is set in the window.
- [[Brent Crude]] because the futures leg anchors the CFD.
- [[Convenience Yield]] because the CFD reflects the premium the market places on having physical oil.
- [[Backwardation]] because persistent positive CFDs typically coincide with curve backwardation.
- [[Floating Storage]] because physical storage economics are priced relative to the CFD and curve shape.

## Common misconceptions

**"CFD in oil means the same as CFD in FX/equities."** Completely different instruments. In oil, a CFD is a specific physical/paper basis spread. In retail trading, CFD refers to leveraged derivatives on price.

**"The CFD is always near zero."** It can be significantly positive or negative. During the 2020 oversupply, CFDs were deeply negative as physical crude went unsold. During supply crises, they spike sharply positive.

**"Only physical traders need to watch CFDs."** Financial traders use CFDs as a leading indicator for curve shape changes. Persistent positive CFDs often signal that the futures curve is about to tighten.

## Sources

- S&P Global Platts: Brent CFD Assessment Methodology
- ICE: Brent CFD Swap Specifications
- Adi Imsirovic, Trading and Price Discovery for Crude Oils
