---
aliases: [CFD, contract for differences, Brent CFD, cargo CFD]
tags:
  - "#energy/crude/brent"
date-added: "2026-03-20"
---

# CFD Crude

## Definition

In crude oil markets, a CFD (Contract for Differences) is the spread between [[Dated Brent]] (the physical spot price for North Sea crude) and the front month [[Brent Crude]] futures contract. Not the same as a retail FX CFD. The oil CFD captures short term divergence between physical and paper markets. It trades as a series of weekly contracts, each settling against the Platts Dated Brent assessment for that week minus the relevant Brent futures month. CFDs are heavily traded by physical houses, prop desks, and hedge funds focused on short term oil dynamics.

## Why it matters (commodities and FX)

The CFD is the most sensitive real time indicator of physical crude tightness. Positive CFD (Dated above futures): physical market is tight, cargoes scarce. Negative CFD: physical loose, cargoes easy to source. Physical traders use CFDs to manage basis risk between cargo purchases (priced off Dated) and futures hedges (ICE Brent). Prop traders use CFDs as a high frequency directional signal: persistent positive CFDs precede futures curve tightening.

## Concrete example

**Concrete:** Physical trader buys a Forties cargo at Dated + $0.20 differential for 2 week delivery, hedged by selling Brent futures. Exposure: CFD + $0.20 differential. CFD at +$0.80 when she prices → effective sell vs futures = $1.00 above the flat hedge. If physical loosens and CFD drops to −$0.30, Dated realization sits $0.30 below futures instead of above. Basis loss on the cargo. CFD volatility is the primary risk she manages.

**Simplified:** The CFD measures the gap between today's physical crude price and the front month futures price. Cash above futures means physical is tight: someone needs a cargo now and pays up. Cash below futures means the market is awash in oil. The number moves around constantly with cargo flows, refinery demand, and pipeline outages, which is why it is the cleanest real time read on physical conditions.

## Key mechanics and formulas

**CFD calculation:** `CFD = Dated Brent Assessment − Brent Front Month Futures`

**Contract structure:** Weekly CFDs settle against the average Platts Dated Brent assessment for each week of the month, minus the corresponding Brent futures month.

**Typical range:** −$1.50 to +$2.00, spiking to +$3 or more during acute physical tightness.

**Traded on:** OTC, brokered by Tullett Prebon, ICAP, and others. ICE also lists Brent CFD swaps.

## Prerequisites

- [[Dated Brent]]
- [[Brent Crude]]
- [[Platts Window]]
- [[Backwardation]]

## Related concepts (learn next)

- [[Dated Brent]] because the CFD is the spread between Dated and futures.
- [[Platts Window]] because the Dated assessment driving CFD settlement is set in the window.
- [[Brent Crude]] because the futures leg anchors the CFD.
- [[Convenience Yield]] because the CFD reflects the premium the market places on having physical oil.
- [[Backwardation]] because persistent positive CFDs coincide with curve backwardation.
- [[Floating Storage]] because physical storage economics are priced vs the CFD and curve shape.

## Common misconceptions

**"CFD in oil means the same as CFD in FX/equities."** Completely different. In oil, CFD = specific physical/paper basis spread. In retail trading, CFD = leveraged derivative on price.

**"The CFD is always near zero."** Can be significantly positive or negative. During the 2020 oversupply, CFDs went deeply negative as physical crude went unsold. During supply crises they spike sharply positive.

**"Only physical traders need to watch CFDs."** Financial traders use CFDs as a leading indicator for curve shape changes. Persistent positive CFDs signal the futures curve is about to tighten.

## Sources

- S&P Global Platts: Brent CFD Assessment Methodology
- ICE: Brent CFD Swap Specifications
- Adi Imsirovic, Trading and Price Discovery for Crude Oils
