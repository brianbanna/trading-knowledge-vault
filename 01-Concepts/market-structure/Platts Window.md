---
aliases: [Platts MOC, Market on Close, Platts assessment window]
tags:
  - "#energy/crude"
  - "#microstructure"
date-added: "2026-03-20"
---

# Platts Window

## Definition

The Platts Window is the daily price assessment process run by S&P Global Platts (formally Market on Close, MOC) where physical commodity traders submit bids, offers, and trades for benchmark cargoes. For crude, the window runs 4:00 to 4:30 PM London. During this 30 minute period, companies trade standardized parcels (600,000 barrel partials for Brent) under transparent rules, and Platts uses the activity to set benchmark assessments including [[Dated Brent]], physical product prices, and many differentials. The window extends to products, LPG, metals, and other commodities.

## Why it matters (commodities and FX)

The Platts Window determines benchmark physical prices underpinning global commodity contracts. Saudi Aramco OSPs, long term LNG contracts, refinery purchase agreements, and derivative settlements all reference Platts assessments. Because prices are set in a narrow 30 minute window, strategic trading during MOC influences the benchmark, giving large physical houses (Vitol, Trafigura, Shell, BP) disproportionate weight. For financial traders, monitoring window activity reveals real time physical tightness that futures may not fully capture.

## Concrete example

**Concrete:** During the 4:00 to 4:30 PM London window, Shell bids 3 Forties partials at $83.50 while Vitol offers 2 at $83.80. Trafigura sells to Shell at $83.50, and the assessed close for Forties is $83.65 (midpoint of the last traded range). This feeds the [[Dated Brent]] assessment. A financial trader watching the window sees unusually aggressive buy side interest, suggesting physical tightness. She goes long Brent futures expecting physical strength to pull the futures curve higher. Two days later, Dated firms by 60 cents, the futures spread reflects the move, and the trade pays.

**Simplified:** A 30 minute window where physical oil traders submit real bids and offers in public. Whatever trades and prints sets the benchmark price for hundreds of billions of dollars of contracts that reference it. Concentrated power: a handful of physical houses shape the prints every day.

## Key mechanics and formulas

**Window timing:** 4:00 to 4:30 PM London (16:00 to 16:30 GMT/BST).

**Parcel size:** 600,000 barrels for BFOET crude (25,000 barrel "partials" aggregating into full cargoes).

**Rules:**
- All bids, offers, and trades published in real time on Platts eWindow
- Participants must have physical delivery capability
- Convergence rules ensure partials aggregate into deliverable cargoes

**Assessment output:** Dated Brent, individual BFOET grade assessments, Brent CFDs, physical differentials.

## Prerequisites

- [[Dated Brent]]
- [[Brent Crude]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Dated Brent]]: the Platts Window is the mechanism that determines the Dated assessment
- [[CFD Crude]]: Dated/futures spread derived from window assessments
- [[Brent Crude]]: BFOET physical market assessed through the window
- [[Market Impact]]: large orders in the window move the benchmark
- [[Liquidity]]: narrow window concentrates liquidity into a short period
- [[EFS]]: Dubai swaps also assessed through a Platts process

## Common misconceptions

**"The Platts Window is just data collection."** It is an active trading venue where large physical houses compete for cargoes. Strategic dimension is significant.

**"Only oil companies participate."** Trading houses, banks (historically), and NOCs all participate. The base has evolved as banks exited physical commodity trading.

**"The window price always reflects true supply and demand."** Limited participation and a short window make it open to strategic behavior. This has triggered regulatory investigations and reforms.

## Sources

- S&P Global Platts: Market on Close Methodology Guide
- S&P Global Platts: eWindow User Guide
- Adi Imsirovic, Trading and Price Discovery for Crude Oils
