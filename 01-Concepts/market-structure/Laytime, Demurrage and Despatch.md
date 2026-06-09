---
aliases: [laytime, laycan, demurrage, despatch, dispatch, nor, notice of readiness]
tags:
  - "#freight/contracts"
date-added: "2026-06-09"
---
# Laytime, Demurrage and Despatch
## Definition
When you hire a ship to carry your cargo on a single trip, the shipowner gives you a fixed allowance of time to load the cargo and a fixed allowance to discharge it. That allowance is the laytime. If you take longer than the allowance, the ship sits idle while still costing the owner money, so you pay a daily penalty called demurrage. If you finish faster than the allowance, the owner gets the ship back early, so the owner pays you a smaller reward called despatch. The whole arrangement only exists under a [[Voyage Charter]], because there the owner carries the time risk and laytime is the line that splits whose time it is. Laytime starts counting only after the vessel has arrived, is physically ready, and the master has tendered a valid [[Notice of Readiness]], subject to the laycan window agreed in the [[Charter Party]].
## Why it matters (commodities and FX)
For a freight, commodities or FX trader this is where a clean paper position turns into a messy cash number. You can book a voyage at a great rate, then watch the profit evaporate because the discharge port is congested and you blow through laytime, with demurrage running at tens of thousands of USD per day. Demurrage is the single largest source of dispute and cash leakage on a voyage fixture, so anyone trading physical cargo or running a [[Voyage Charter]] book must model it as a real cost line, not a footnote. The laycan window matters just as much, because if your vessel cannot present within the agreed laydays the charterer can cancel the entire fixture, leaving you with an unfixed ship in a falling market. Demurrage exposure also feeds your hedging: it is one of the reasons traders pair a physical voyage with a [[Forward Freight Agreement]] or use [[Port Congestion and Waiting Time]] estimates to set buffers. For a commodity trader, demurrage is often invoiced in USD even when the underlying cargo or counterparty cash flow is in another currency, so it quietly creates FX exposure on the settlement.
## Concrete example
**Concrete:** You charter a [[Supramax]] of roughly 58,000 dwt under a [[Voyage Charter]] to carry a grain cargo from a US Gulf port to a discharge port, and the [[Charter Party]] grants 72 hours total laytime, demurrage at 20,000 USD per day, and despatch at half demurrage, so 10,000 USD per day. The laycan window is 10 to 15 June, and your vessel tenders a valid [[Notice of Readiness]] on 12 June, inside the window, so the fixture holds. Now the discharge port is congested. The vessel is held an extra 4 days beyond the 72 hour laytime allowance. Demurrage owed is `4 days x 20,000 USD/day = 80,000 USD` that the charterer pays the owner. That 80,000 USD is a direct hit to the charterer's voyage economics and a windfall to the owner. The opposite case: the port is empty and you discharge in 48 hours, finishing 24 hours, so 1 day, inside laytime. Despatch earned is `1 day x 10,000 USD/day = 10,000 USD` that the owner pays the charterer. Note the asymmetry. The penalty for being slow bites at 20,000 USD per day, but the reward for being fast pays only 10,000 USD per day, so the charterer is structurally short time. If your vessel had arrived on 17 June, outside the 10 to 15 June laycan, the charterer could have cancelled the fixture entirely and you would be left with an unfixed ship.
**Simplified:** You get a fixed number of free hours to load and unload. Go over and you pay the owner a daily fine. Come in under and the owner pays you a smaller daily bonus. Show up too late and the deal can be torn up before it starts.
## Key mechanics and formulas
- Demurrage: `demurrage = (time used - laytime allowed) x demurrage rate` where time used is counted laytime, laytime allowed is the hours granted in the [[Charter Party]], and the demurrage rate is the agreed USD per day. Once on demurrage, always on demurrage, meaning many laytime exceptions stop applying and the clock runs continuously.
- Despatch: `despatch = (laytime allowed - time used) x despatch rate` and the despatch rate is conventionally half the demurrage rate. Despatch may be payable on all laytime saved or only on working time saved, depending on the clause wording.
- Notice of Readiness, the NOR, is the master's formal notice that the vessel has arrived and is physically and legally ready to load or discharge. Laytime usually begins a set number of hours after a valid NOR is tendered and accepted, the turn time or notice time.
- Laycan is the laydays and cancelling pair. Laydays is the earliest date the charterer must accept the vessel, the cancelling date is the latest date by which the vessel must tender NOR or the charterer may cancel.
- Reversible laytime: load and discharge allowances are pooled into one combined figure, so hours saved at the load port can offset hours overrun at the discharge port. This favours the charterer because the two ports net against each other.
- Non reversible laytime: load and discharge each have a separate allowance counted independently, so an overrun at one port cannot be cancelled by speed at the other.
- Laytime is typically quoted in running hours, weather working days, or as a load and discharge rate in tonnes per day that implies an hour count given the cargo size.
- Demurrage claims are time barred, often 90 days from completion of discharge, so the supporting statement of facts and time logs must be filed promptly or the claim is lost.
## Prerequisites
- [[Voyage Charter]]
- [[Charter Party]]
- [[Freight]]
- [[Vessel Classes and Deadweight Tonnage]]
## Related concepts (learn next)
- [[Port Congestion and Waiting Time]] because congestion is the main driver of laytime overrun and demurrage in practice.
- [[Notice of Readiness]] because the validity and timing of the NOR is what starts the laytime clock and is the most litigated point.
- [[Time Charter]] because it is the alternative structure where the charterer pays for time directly and laytime and demurrage do not apply.
- [[Forward Freight Agreement]] because traders hedge voyage rate exposure on paper while demurrage stays as a residual physical risk.
- [[Baltic Exchange and the Dry Indices]] because published voyage rates and route assessments embed assumed laytime and port terms.
- [[Ballast Leg Economics]] because demurrage delays push back the next ballast and reshape the round voyage return.
- [[Baltic Route Codes]] because each benchmark route specifies standard load and discharge terms that anchor laytime negotiation.
- [[EEXI and CII Regulations]] because slow steaming for compliance can lengthen the voyage and interact with laycan presentation.
## Common misconceptions
- **"Demurrage is a fee for using the ship longer."** Wrong. Demurrage is liquidated damages for breach of the charterer's obligation to load or discharge within laytime, not a hire charge. The legal framing matters because, unlike hire, demurrage runs continuously once it starts and many laytime exceptions, such as weather or holidays, no longer interrupt the clock under the once on demurrage, always on demurrage rule.
- **"Despatch always equals the demurrage rate."** Wrong. Despatch is conventionally half the demurrage rate, so the owner pays out at a slower rate than the charterer pays in. The asymmetry exists because the owner suffers more from delay than it benefits from early redelivery, and it makes the charterer structurally short time on every fixture.
- **"Laytime starts when the vessel arrives at the port."** Wrong. Arrival alone is not enough. Laytime starts only after the vessel is an arrived ship at the agreed point, is physically and legally ready, and a valid [[Notice of Readiness]] has been tendered and the turn time has elapsed. A premature or invalid NOR can fail to start the clock entirely, costing the owner days of countable time.
- **"Laycan and laytime are the same thing."** Wrong. Laycan is the calendar window in which the vessel must present and the charterer may cancel if it does not. Laytime is the quantity of time, in hours or days, allowed for cargo operations once the vessel has presented. One governs whether the contract survives, the other governs the cash penalty inside a live contract.
## Sources
- Baltic Exchange, voyage charter and route definitions, https://www.balticexchange.com
- BIMCO, GENCON 1994 and 2022 standard voyage charter party forms and laytime clauses, https://www.bimco.org
- John Schofield, Laytime and Demurrage, Informa Law, standard practitioner reference
- Voylaw and Laytime Definitions for Charter Parties 2013, BIMCO, CMI, FONASBA and INTERCARGO joint definitions
- Stopford, Martin, Maritime Economics, 3rd edition, Routledge
