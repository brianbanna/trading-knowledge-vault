---
aliases: [Dated Brent assessment, physical Brent, BFOET]
tags:
  - "#energy/crude/brent"
date-added: "2026-03-20"
---

# Dated Brent

## Definition

Dated Brent is the spot price assessment for physical North Sea crude oil (the BFOET basket: Brent, Forties, Oseberg, Ekofisk, Troll) with a specific delivery window, typically 10 to 25 days forward. It is assessed daily by S&P Global Platts through the [[Platts Window]] (Market on Close process). Dated Brent is the foundational physical price in global oil markets: it is the "cash" price that anchors the Brent futures complex to physical reality. The relationship between Dated Brent and the front month ICE Brent futures is the CFD (Contract for Differences), which captures the short term physical/paper spread.

## Why it matters (commodities and FX)

Dated Brent is the price that actually matters for physical oil trading. While ICE Brent futures provide liquidity and price discovery, it is Dated Brent that determines the actual cost of buying or selling a physical cargo of North Sea crude. Approximately 2/3 of global crude oil is priced directly or indirectly off Dated Brent through formulas and differentials. For traders, the spread between Dated Brent and Brent futures ([[CFD Crude]]) is one of the most actively traded short term indicators. When Dated Brent trades at a premium to futures (strong physical market), it signals near term tightness that futures may not yet fully reflect.

## Concrete example

A physical trading house is offered a cargo of Forties crude loading in 15 days. The Platts Dated Brent assessment is $83.20/bbl, while ICE Brent front month futures are at $82.50. The [[CFD Crude|CFD]] is $0.70 (Dated premium). The trader buys the cargo at Dated Brent flat ($83.20) and simultaneously sells ICE Brent futures at $82.50, locking in a $0.70/bbl cost that he expects to recover through his offtake contract. If physical demand strengthens and the CFD widens to $1.50, the cargo appreciates relative to the hedge. If the physical market softens and the CFD flips to minus $0.30, the cargo loses value.

## Key mechanics and formulas

**Dated Brent assessment:** Set daily by Platts based on trading activity in the [[Platts Window]] for BFOET cargoes (600,000 barrel partials) loading 10 to 25 days forward.

**CFD:** `CFD = Dated Brent - ICE Brent Front Month Futures`

**Dated to front month (DFL):** Same as CFD. Positive = physical premium. Negative = physical discount.

**BFOET basket:** The 5 grades (Brent, Forties, Oseberg, Ekofisk, Troll) are assessed, and the cheapest to deliver grade sets the Dated Brent level.

## Prerequisites

- [[Brent Crude]]
- [[Platts Window]]
- [[Forward Curve]]
- [[Contango]]
- [[Backwardation]]

## Related concepts (learn next)

- [[Platts Window]] because the MOC process is how Dated Brent is assessed daily.
- [[CFD Crude]] because the Dated/futures spread is the most active short term physical indicator.
- [[Brent Crude]] because ICE Brent futures derive their relevance from the link to Dated Brent.
- [[EFS]] because the Brent/Dubai spread ultimately depends on the physical Dated Brent assessment.
- [[Convenience Yield]] because the Dated premium over futures reflects the value of physical oil.
- [[Floating Storage]] because physical crude storage economics are priced relative to Dated Brent.

## Common misconceptions

**"Brent futures and Dated Brent are the same thing."** They are related but distinct. Futures are financial instruments with standardized expiry. Dated Brent is a physical price with a specific delivery window. The spread between them (CFD) fluctuates significantly.

**"Dated Brent is set by supply and demand alone."** The assessment is based on activity in the Platts window, which is a specific 30 minute trading period. Strategic trading behavior in the window can influence the assessment, leading to regulatory scrutiny.

**"Dated Brent is a single grade."** It is a basket of 5 North Sea grades. The cheapest to deliver principle means that changes in relative supply of individual grades can shift which one sets the Dated Brent level.

## Sources

- S&P Global Platts: Dated Brent Assessment Methodology
- ICE: Brent Crude Oil Index Methodology
- Adi Imsirovic, Trading and Price Discovery for Crude Oils
