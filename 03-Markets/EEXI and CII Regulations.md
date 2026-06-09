---
aliases: [eexi, cii, energy efficiency existing ship index, carbon intensity indicator, imo decarbonisation, imo carbon rules]
tags:
  - "#freight"
  - "#regulation"
date-added: "2026-06-09"
---

# EEXI and CII Regulations

## Definition
These are two rules from the International Maritime Organisation (the United Nations body that regulates shipping) designed to cut the carbon emissions of the world fleet. Think of a car: EEXI is like a one time inspection that says your engine is too thirsty, so you fit a governor that caps its top speed. CII is like an annual report card that grades how much fuel you actually burned per mile of useful work, from A (best) to E (worst). EEXI (Energy Efficiency Existing Ship Index) is a technical, one time standard applied to existing ships that compares a vessel's designed efficiency against a required baseline; the cheapest way to pass is usually engine power limitation, which physically caps the maximum power the engine can draw. CII (Carbon Intensity Indicator) is an operational, annual measure of grams of CO2 emitted per cargo carrying capacity per nautical mile, and it produces a yearly letter grade. A ship that scores D for 3 consecutive years, or E in a single year, must file a corrective action plan with its flag state before it can keep trading.

## Why it matters (commodities and FX)
A freight trader cares because these rules directly remove effective tonnage from the market without scrapping a single ship. EEXI engine power limits and CII pressure both push owners toward slow steaming, and a fleet that sails slower delivers fewer voyages per year, which tightens supply and supports rates exactly when you might expect surplus tonnage. When you price a [[Time Charter]] or build a voyage P and L for a [[Voyage Charter]], you must now ask whether the vessel can physically hit the speed in your model or whether its CII budget forces it to crawl. The rules also reshape the [[Forward Curve]] for freight: if traders expect tightening supply from compliance, [[Forward Freight Agreement]] curves can move into [[Backwardation]] or steepen. CII risk has become a clause in the [[Charter Party]], so a charterer who pushes a ship hard can be blamed for wrecking its annual rating, creating a new dimension of counterparty negotiation.

## Concrete example
**Concrete:** Consider a fleet of [[Vessel Classes and Deadweight Tonnage|Capesize bulkers]] of roughly 180,000 dwt running iron ore on the [[Baltic Route Codes|C5 route]] from West Australia to Qingdao. Designed service speed is 14.5 knots, but at that pace the ships project to a CII grade of D, heading for the consecutive D trap. A trader at the owner reduces laden speed to 11.5 knots to hold a C rating. The round voyage that took 35 days now takes 42, so each ship completes roughly 8.7 round trips a year instead of 10.4, cutting that ship's annual delivered cargo by about 16 percent. Across a 200 ship pool that is the equivalent of withdrawing 32 ships of supply. If the market is balanced, this tightening WORKS in the owner's favour: spot Capesize [[Freight]] rates climb from 18,000 USD per day to 26,000 USD per day, and the owner's [[Forward Freight Agreement]] longs print a profit. If instead Chinese steel demand collapses at the same time, the slow steaming FAILS to support the market: rates fall to 9,000 USD per day anyway, the owner has locked in slower asset turns, and ships idling in [[Port Congestion and Waiting Time|congestion]] still burn their CII budget while earning nothing, so they limp into the next year already rated D.

**Simplified:** The rules make ships sail slower to pass their carbon report card. Slower ships do fewer trips, so there is less shipping capacity, which normally pushes freight prices up. But if cargo demand crashes at the same time, slow steaming cannot rescue rates, and the owner is just stuck moving cargo more slowly for less money.

## Key mechanics and formulas
- EEXI attained value vs required value: `attained_EEXI <= required_EEXI`, where attained EEXI is the ship's calculated grams of CO2 per tonne mile from engine, fuel and design data, and required EEXI is the IMO baseline for that ship type and size, set as a percentage reduction from a 2008 era reference line.
- Engine power limitation (EPL): `P_limit = P_MCR * reduction_factor`, where P_MCR is maximum continuous rating of the engine and reduction_factor is the cut needed to bring attained EEXI under the required value. EPL caps power and therefore top speed; it can be overridden in emergencies but the override is logged.
- Attained CII: `CII = total_CO2_grams / (capacity_dwt * distance_nm)`, the carbon emitted per unit of transport work over a calendar year. Lower is better.
- CII rating boundaries: the attained CII is compared against a required CII for the ship's type and size, and 4 boundary lines split the result into grades A, B, C, D, E. The required CII tightens roughly 2 percent per year, so a ship that does nothing drifts toward worse grades over time.
- Corrective action trigger: 3 consecutive years at D, or a single year at E, forces a corrective action plan inside the ship's SEEMP (Ship Energy Efficiency Management Plan) before continued trading.
- Fuel choice interacts with both rules: switching toward cleaner fuel or hedging the spread between heavy and distillate grades affects emitted CO2, see [[Bunkers, IFO versus MGO, and the Bunker Hedge]].
- Levers to improve CII: slow steaming, hull and propeller cleaning, energy saving devices, route optimisation to cut [[Ballast Leg Economics|ballast]] miles, and avoiding idle time in [[Port Congestion and Waiting Time|congestion]].

## Prerequisites
- [[Vessel Classes and Deadweight Tonnage]]
- [[Dry Bulk versus Wet Bulk]]
- [[Freight]]
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]]

## Related concepts (learn next)
- [[Forward Freight Agreement]] because tightening supply from compliance is one of the main fundamental drivers traders price into the freight forward curve.
- [[Time Charter]] because CII responsibility and the ship's achievable speed are now negotiated terms in modern charter contracts.
- [[Charter Party]] because new CII clauses allocate the blame and cost of a poor rating between owner and charterer.
- [[Port Congestion and Waiting Time]] because time spent idling at anchor burns fuel and damages the annual CII rating without earning revenue.
- [[Ballast Leg Economics]] because empty repositioning legs add CO2 and distance with zero cargo, hurting CII directly.
- [[Bunkers, IFO versus MGO, and the Bunker Hedge]] because the fuel a ship burns determines its emitted CO2 and therefore its rating and hedging needs.
- [[Seasonality]] because slow steaming reshapes how quickly tonnage can respond to seasonal demand peaks, changing the rate cycle.
- [[Freight Options]] because the supply uncertainty created by these rules feeds directly into freight volatility and option pricing.

## Common misconceptions
- **"EEXI and CII are the same rule with different names."** Wrong. EEXI is a one time technical certification of the ship's design efficiency, judged once and usually satisfied by an engine power limit. CII is an annual operational measure of how the ship was actually run that year, producing a fresh letter grade every year. A ship can pass EEXI on paper and still earn a failing CII grade if it is operated inefficiently.
- **"A bad CII grade means the ship is banned from trading."** Wrong. A single D, or even an E, does not immediately stop a ship. The enforcement trigger is 3 consecutive years at D or one year at E, and the consequence is a mandatory corrective action plan, not an outright ban. The commercial pressure comes from charterers preferring better rated ships and from owners acting pre emptively, not from a legal prohibition on a single bad year.
- **"Carbon rules are bearish for freight rates because they raise costs."** Wrong, or at least incomplete. Higher fuel and compliance costs do raise the breakeven, but the dominant near term market effect is the removal of effective tonnage supply through slow steaming and retrofitting, which is bullish for rates. Many freight desks treat IMO decarbonisation as a structural supply constraint rather than a simple cost drag.
- **"CII rewards a fully loaded ship the same as an empty one."** Wrong. CII divides emissions by the ship's capacity in deadweight times the distance sailed, so the denominator uses capacity, not actual cargo on board. This means sailing many [[Ballast Leg Economics|ballast]] miles with no cargo still counts the full capacity in the denominator while adding CO2 in the numerator, so empty repositioning legs and idle steaming actively worsen the rating.

## Sources
- IMO, Marine Environment Protection Committee (MEPC), Resolutions on EEXI and CII guidelines (MEPC.333 and MEPC.354 series): https://www.imo.org/en/MediaCentre/HotTopics/Pages/EEXI-CII-FAQ.aspx
- IMO, MARPOL Annex VI, Chapter 4 on energy efficiency of ships.
- Baltic Exchange, market commentary on tonnage supply and the freight impact of decarbonisation rules: https://www.balticexchange.com
- Clarksons Research, fleet efficiency and CII rating distribution reports.
- DNV and Lloyd's Register technical guidance on EEXI compliance and engine power limitation.
