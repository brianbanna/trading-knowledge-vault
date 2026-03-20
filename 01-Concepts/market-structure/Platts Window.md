---
aliases: [Platts MOC, Market on Close, Platts assessment window]
tags:
  - "#energy/crude"
  - "#microstructure"
date-added: "2026-03-20"
---

# Platts Window

## Definition

The Platts Window is a daily price assessment process run by S&P Global Platts (formally called Market on Close, or MOC) during which physical commodity traders submit bids, offers, and trades for benchmark cargoes. For crude oil, the window runs from 4:00 to 4:30 PM London time. During this 30 minute period, companies trade standardized parcels (typically 600,000 barrel partials for Brent) under transparent rules, and Platts uses this activity to set benchmark assessments including [[Dated Brent]], physical product prices, and numerous differential assessments. The window process extends beyond oil to products, LPG, metals, and other commodities.

## Why it matters (commodities and FX)

The Platts Window determines the benchmark physical prices that underpin global commodity contracts. Saudi Aramco's Official Selling Prices, long term LNG contracts, refinery purchase agreements, and derivative settlements all reference Platts assessments. Because these prices are set in a narrow 30 minute window, strategic trading during the MOC period can influence the benchmark, giving large physical houses (Vitol, Trafigura, Shell, BP) disproportionate influence. For financial traders, monitoring window activity provides real time insight into physical market tightness that futures prices may not fully capture.

## Concrete example

During the 4:00 to 4:30 PM London window, Shell bids for 3 Forties partials at $83.50 while Vitol offers 2 partials at $83.80. Trafigura sells to Shell at $83.50, and the closing assessed level for Forties is $83.65 (midpoint of the last traded range). This becomes part of the [[Dated Brent]] assessment. A financial trader watching the window notices that buy side interest is unusually aggressive, suggesting physical tightness. She goes long Brent futures anticipating the physical strength will pull futures higher.

## Key mechanics and formulas

**Window timing:** 4:00 to 4:30 PM London time (16:00 to 16:30 GMT/BST).

**Parcel size:** 600,000 barrels for BFOET crude (25,000 barrel "partials" that aggregate into full cargoes).

**Rules:**
- All bids, offers, and trades are published in real time on Platts' eWindow platform
- Participants must have physical delivery capability
- Convergence rules ensure partials aggregate into deliverable cargoes

**Assessment output:** Dated Brent, individual BFOET grade assessments, Brent CFDs, physical differentials.

## Prerequisites

- [[Dated Brent]]
- [[Brent Crude]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Dated Brent]] because the Platts Window is the mechanism that determines the Dated Brent assessment.
- [[CFD Crude]] because the Dated/futures spread is directly derived from window assessments.
- [[Brent Crude]] because the BFOET physical market is assessed through the window.
- [[Market Impact]] because large orders in the window can move the benchmark.
- [[Liquidity]] because the narrow window concentrates liquidity into a short time period.
- [[EFS]] because Dubai swaps assessments are also set through a Platts process.

## Common misconceptions

**"The Platts Window is just a data collection exercise."** It is an active trading venue where large physical houses compete for cargoes. The strategic dimension is significant.

**"Only oil companies participate."** Trading houses, banks (historically), and national oil companies all participate in the window. The participant base has evolved as banks have exited physical commodity trading.

**"The window price always reflects true supply and demand."** Because participation is limited and the window is short, it can be influenced by strategic behavior. This has led to regulatory investigations and reforms.

## Sources

- S&P Global Platts: Market on Close Methodology Guide
- S&P Global Platts: eWindow User Guide
- Adi Imsirovic, Trading and Price Discovery for Crude Oils
