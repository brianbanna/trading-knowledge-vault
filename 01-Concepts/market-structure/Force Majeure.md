---
aliases: [force majeure, FM, act of god clause]
tags:
  - "#regulation"
date-added: "2026-07-03"
---

# Force Majeure

## Definition

Force majeure is a contract clause that lets a party walk away from its delivery or performance obligation when an extraordinary event beyond its control makes performance impossible. War, natural disaster, accident, sabotage, or a government order can all qualify. The party declaring it is not in breach; the clause treats the failure as no one's fault. In plain terms, it is the "the thing we promised became impossible through no fault of ours" escape hatch written into the contract.

In commodities the clause has a market consequence that the legal language hides: a declared force majeure removes contracted supply from the market at short notice. A producer, liquefaction plant, pipeline, or terminal that declares FM stops delivering barrels or cargoes it was obligated to ship, and the buyer has to replace that volume from the spot market. That sudden replacement demand tightens prompt supply and lifts the relevant regional spread, even though the flat price benchmark may barely move.

Context from the tape: [[QatarEnergy]] declared force majeure covering 21 cancelled LNG cargoes through mid September, roughly 2.7 bcm of gas lost to the buyer ([[Edison]]). Those cargoes were contracted supply that vanished from the Atlantic Basin at short notice. The buyer had to cover from the spot market, which tightened Atlantic Basin LNG and kept [[JKM]] elevated versus prewar. That is a clean example of a contract clause feeding straight into a physical [[Supply Shock]].

## Why it matters (commodities and FX)

Force majeure is one of the few events that removes real, contracted supply instantly and without warning. Unlike a demand forecast that markets can lean into over weeks, an FM declaration is a step change. The buyer who was counting on those volumes is suddenly short and must cover in the prompt market, which is exactly where liquidity is thinnest and price impact is largest. That is why FM declarations tighten front spreads and support regional gas and oil benchmarks even when the far curve is calm.

For a trader the signal is in the spread, not the flat price. A declared FM on Atlantic Basin LNG supports [[TTF Natural Gas]] and [[JKM]] relative to the rest of the curve because it is a prompt, regional tightness, not a permanent change in the global balance. It also raises [[Convenience Yield]]: with contracted supply pulled, holding physical inventory now becomes more valuable because the buyer cannot rely on the contract to deliver.

Force majeure also interacts with the freight and chartering chain. When a cargo is cancelled under FM, the [[Charter Party]] and any [[Forward Freight Agreement]] hedges around that voyage unwind, and demurrage and laytime obligations shift. For FX, a sustained FM on a major export stream cuts the exporter's hard currency earnings and can pressure its currency and fiscal balance.

## Concrete example

**Concrete:** [[Edison]] has 21 LNG cargoes contracted from [[QatarEnergy]] for delivery through mid September, about 2.7 bcm of gas. QatarEnergy declares force majeure and cancels them. Edison is now short 2.7 bcm of prompt supply it had already sold on to European utilities, so it must buy replacement cargoes in the spot market during a tight summer injection season. That replacement demand pushes [[TTF Natural Gas]] up 3 EUR per MWh and widens the prompt versus winter spread as buyers scramble for August and September molecules. [[JKM]] stays elevated versus prewar because Atlantic Basin cargoes that might have relieved Asia are now spoken for. The counter case: the FM covers cargoes six months out into a well supplied shoulder season, buyers have ample time to source alternatives, storage is comfortable, and the prompt spread barely reacts. Same clause, very different price impact, because the tightness that matters is prompt and regional.

**Simplified:** A seller invokes a clause that lets it legally cancel deliveries it promised, because something extraordinary made them impossible. The buyer still needs the gas, so it rushes into the spot market to replace it. That sudden buying tightens supply right now and pushes up the regional price, even if the long term price hardly moves. The closer the cancelled cargoes are to today, and the tighter the market already is, the bigger the jump.

## Key mechanics and formulas

Force majeure is mostly a legal and logistical mechanism, but the market impact follows the size and timing of the removed volume:

`Prompt price impact ≈ (cancelled volume / prompt market depth) × prompt supply elasticity`

The impact concentrates on the front of the curve, so the observable is the spread:

`Δ (prompt − deferred spread) > 0` when the FM removes prompt supply into an already tight market.

What separates a market moving FM from a benign one:
- Prompt versus deferred: cancelled cargoes near the front hit thin prompt liquidity hardest
- Market state: an already tight, low storage market amplifies the impact; a well supplied one absorbs it
- Volume relative to regional balance: 2.7 bcm matters in a tight Atlantic Basin, less in a glut
- Replaceability: grades and delivery windows with few substitutes see larger spread moves

Legal test for a valid declaration, generally: the event must be unforeseeable, beyond the party's control, and must genuinely make performance impossible rather than merely more expensive. Price moving against the seller is not force majeure.

## Prerequisites

- [[Supply Shock]]
- [[Charter Party]]
- [[TTF Natural Gas]]

## Related concepts (learn next)

- [[Supply Shock]] — force majeure is one of the cleanest triggers of a sudden, involuntary supply loss.
- [[Convenience Yield]] — pulled contracted supply raises the value of holding physical now, which the curve prices as convenience yield.
- [[TTF Natural Gas]] — the European gas benchmark most directly supported by Atlantic Basin LNG force majeure.
- [[Charter Party]] — the shipping contract whose obligations and demurrage shift when a cargo is cancelled under FM.
- [[Forward Freight Agreement]] — the freight hedge that unwinds around a cancelled voyage.
- [[Laytime, Demurrage and Despatch]] — the port time accounting that FM declarations disrupt.
- [[Geopolitical Risk]] — war and sabotage are frequent triggers of force majeure on export infrastructure.

## Common misconceptions

**"Force majeure means the price went the wrong way."** No. A bad market is not force majeure. The event must make performance genuinely impossible, not merely unprofitable. Courts reject FM claims that are really just buyer's or seller's remorse.

**"An FM declaration is automatically valid."** It is a claim that can be contested. The counterparty can dispute whether the event was truly unforeseeable, beyond control, and performance ending. Disputes often go to arbitration.

**"Force majeure moves the flat price."** Usually it moves the prompt spread more than the flat price. The tightness is local and immediate, so the front of the curve reprices while the far curve, which reflects the long run balance, stays put.

**"FM only matters to the two parties on the contract."** The replacement buying spills into the whole regional market. One large declaration can move a benchmark that thousands of unrelated positions are marked against.

## Sources

- International Chamber of Commerce, ICC Force Majeure Clause guidance
- GIIGNL, "The LNG Industry Annual Report" on contract structures
- Platts and ICIS, coverage of LNG force majeure declarations and spread impact
- Standard shipping contract forms (GENCON, SHELLTIME) force majeure provisions
