---
aliases: [tanker classes, tanker ladder, mr, lr1, lr2, aframax, suezmax, vlcc, ulcc, product tankers, crude tankers]
tags:
  - "#freight/wet"
date-added: "2026-06-09"
---

# Wet Tanker Classes

## Definition
A wet tanker is a ship that carries liquid cargo in bulk, almost always petroleum: crude oil, refined products like gasoline and diesel, or heavy fuel oil. Just as dry bulk ships come in standard size bands, tankers fall into a recognised ladder of classes defined mainly by deadweight tonnage and by the kind of oil they carry. The ladder runs from the small MR product carrier of about 45,000 deadweight tonnes up through Aframax, Suezmax, and the giant VLCC of about 320,000 deadweight tonnes that hauls roughly 2,000,000 barrels of crude. The other axis is dirty versus clean service: dirty tankers move crude and fuel oil, clean tankers move refined products and need coated tanks to keep the cargo pure. A trader needs both axes because a ship's size and its dirty or clean status together fix which cargoes it can lift, which routes it sails, and which freight index prices it.

## Why it matters (commodities and FX)
Each class trades as its own freight market with its own [[Forward Curve]], its own [[Baltic Exchange and the Dry Indices]] equivalent on the tanker side, and its own supply and demand balance. A glut of VLCCs does not relieve a tight MR market because the ships cannot substitute: you cannot load 2,000,000 barrels of gasoline onto a refinery jetty built for a 350,000 barrel product parcel. Knowing the ladder lets a trader pick the right ship for a cargo, read which class is bidding up [[Freight]] when crude flows shift, and position the correct contract on the [[Forward Freight Agreement]] curve. Class also drives route geography: a Suezmax is sized to transit the Suez Canal laden, a VLCC often cannot and must route around the Cape, and that routing choice changes voyage days, [[Bunkers, IFO versus MGO, and the Bunker Hedge]] cost, and [[Ballast Leg Economics]]. The dirty versus clean split matters for FX and crack spread traders too, because clean product arbitrage from Middle East refineries to Europe rides on LR2 economics while dirty crude arbitrage from the Arabian Gulf to Asia rides on VLCC economics.

## Concrete example
**Concrete:** A trader needs to move 270,000 tonnes of Arabian Gulf crude to Ningbo, China. The natural ship is a [[VLCC]] at about 300,000 deadweight tonnes carrying roughly 2,000,000 barrels. The voyage route TD3C (Ras Tanura to Ningbo) is quoted on the Baltic at Worldscale 55, which at the published flat rate works out to about 18 dollars per tonne, so the freight bill is about 4,860,000 dollars. If the trade WORKS, the trader booked the VLCC before an OPEC export surge pushed TD3C to Worldscale 80, and the position on the [[Forward Freight Agreement]] gains because spot freight rose above the fixed level. If it FAILS, a wave of newbuilding VLCCs delivers into a soft market, TD3C collapses to Worldscale 35, the chartered-in ship now costs more than the market, and the trader bleeds the difference on every laden day plus idle [[Ballast Leg Economics]] sailing back empty to the Gulf. Contrast the clean side: the same trader moving a 35,000 tonne gasoline parcel from Jubail to Rotterdam uses an [[MR]] tanker on a coated-tank route, an entirely separate freight market that did not move when crude freight crashed.

**Simplified:** Big crude ships and small product ships live in different worlds. Pick the wrong size or the wrong dirty-or-clean ship and your cargo will not fit the terminal or your freight bet will track a market that has nothing to do with your cargo.

## Key mechanics and formulas
- Approximate size bands by deadweight tonnage (dwt) and typical service:
  - MR (Medium Range): about 45,000 to 55,000 dwt, clean products, gasoline, diesel, jet fuel, coated tanks.
  - LR1 (Long Range 1): about 55,000 to 80,000 dwt, clean products on longer hauls, often Panamax-derived hull.
  - LR2 (Long Range 2): about 80,000 to 120,000 dwt, long-range clean products, same hull size as Aframax but coated for products.
  - Aframax: about 80,000 to 120,000 dwt, crude on short and medium haul, dirty service.
  - Suezmax: about 120,000 to 200,000 dwt, crude, sized to transit the Suez Canal laden.
  - VLCC (Very Large Crude Carrier): about 200,000 to 320,000 dwt, roughly 2,000,000 barrels, long-haul crude, Middle East to Asia.
  - ULCC (Ultra Large Crude Carrier): above 320,000 dwt, rare today, very few in service due to port and draft limits.
- Dirty versus clean is the second axis and decides tank lining:
  - Dirty service carries crude oil and residual fuel oil. Tanks are bare steel because the cargo is already dark and viscous and a little residue does not contaminate the next dirty cargo.
  - Clean service carries refined products: gasoline, diesel, jet, naphtha. Tanks are epoxy or zinc coated so the cargo stays on-spec and the steel does not rust into a bright product.
  - A ship can switch from clean to dirty trade but the reverse requires expensive tank cleaning and the coating, once degraded by dirty cargo, may no longer guarantee product purity.
- Barrel-to-tonne conversion is grade dependent. A common rule for crude: `barrels = dwt * 7.3` approximately, where 7.3 is the barrels-per-tonne factor for medium crude. This gives a 300,000 dwt VLCC roughly 2,190,000 barrels of nominal capacity, trimmed by bunkers, stores, and reserve.
- Freight for tankers is quoted in Worldscale, a percentage of a published flat rate per route, covered in the [[Freight]] note. `freight per tonne = WS quoted / 100 * flat rate`, where WS quoted is the agreed Worldscale points and flat rate is the annual Worldscale schedule dollar-per-tonne benchmark for that route.

## Prerequisites
- [[Vessel Classes and Deadweight Tonnage]]
- [[Dry Bulk versus Wet Bulk]]
- [[Freight]]

## Related concepts (learn next)
- [[Baltic Route Codes]] because tanker routes like TD3C and TC2 are how each class's freight is actually quoted and tracked.
- [[Forward Freight Agreement]] because hedging or speculating on tanker freight uses per-route FFAs tied to these classes.
- [[Freight Options]] because the next step beyond linear freight exposure is buying optionality on a route.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because fuel is the largest variable voyage cost and scales with ship size and route length.
- [[Ballast Leg Economics]] because a tanker often sails empty back to the load region, and that cost is baked into the freight a class can earn.
- [[EEXI and CII Regulations]] because emissions rules cap speed and effective supply differently across the size bands.
- [[Voyage Charter]] because most spot tanker fixtures are voyage charters priced in Worldscale per route.
- [[Floating Storage]] because VLCCs and Suezmaxes in [[Contango]] markets get hired to store crude at sea, tightening freight supply.

## Common misconceptions
- **"A bigger tanker is always cheaper because it carries more oil."** Wrong as a blanket rule. Larger ships do give a lower cost per tonne when full on a long haul, but they are useless when the cargo parcel, the terminal draft, or the canal will not accommodate them. A 35,000 tonne gasoline parcel for a small European port cannot ride a VLCC, so the relevant comparison is cost per delivered cargo within the size the trade actually permits, not raw capacity.
- **"Aframax and LR2 are the same ship so they trade the same."** Wrong. They share a hull size of roughly 80,000 to 120,000 dwt, but the Aframax runs dirty crude in bare-steel tanks while the LR2 runs clean products in coated tanks. They sit in different freight markets, respond to different supply and demand, and a clean LR2 only crosses into dirty crude trade at the cost of decoating its product capability.
- **"Suezmax means it is the biggest ship that uses the Suez Canal."** Wrong. The name means the ship is sized to transit Suez laden, but the canal has been deepened and widened over time and now passes laden VLCCs in many cases. Suezmax is a market size convention of roughly 120,000 to 200,000 dwt, not a hard physical ceiling on canal transit.
- **"Clean and dirty is about how new or clean the ship looks."** Wrong. It refers entirely to cargo grade and tank lining. A dirty tanker carries crude and fuel oil in bare steel tanks by design, a clean tanker carries refined products in coated tanks, and the label says nothing about the vessel's age or condition.

## Sources
- Baltic Exchange tanker route definitions and Worldscale guidance, https://www.balticexchange.com
- Worldscale Association, New Worldwide Tanker Nominal Freight Scale, annual flat rate schedule, https://www.worldscale.co.uk
- Martin Stopford, Maritime Economics, 3rd edition, chapters on the tanker market and ship size economics.
- Clarksons Research, tanker fleet and size band statistics, https://www.clarksons.com
- BIMCO and Intertanko fleet and classification references on crude versus product tanker trades.
