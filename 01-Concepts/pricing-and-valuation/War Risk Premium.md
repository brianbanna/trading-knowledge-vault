---
aliases: [war risk premium, war risk insurance, WRP, additional war risk premium, AWRP]
tags:
  - "#freight/wet"
  - "#energy/crude"
  - "#risk"
date-added: "2026-07-03"
---

# War Risk Premium

## Definition

The war risk premium is the extra marine insurance you pay to send a ship through a conflict zone. Standard hull cover excludes acts of war, so when a vessel wants to transit contested water it buys a separate additional war risk premium, quoted as a percentage of the ship's hull value for that single voyage. In plain terms, it is the danger money the insurer charges to cover a tanker that might get hit, mined, or seized.

By extension, traders use the same term for the premium embedded in delivered crude when a [[Chokepoint]] is contested. The higher insurance cost is a real, quantifiable per barrel toll that raises the landed price of every cargo forced through the danger zone. So the war risk premium lives in two places at once: as an explicit line item on the [[Freight]] bill, and as a wedge inside the [[Brent Crude]] price and its [[Forward Curve]].

Context from the tape: with the [[Strait of Hormuz]] contested, Iran was charging up to 2 million USD per voyage in transit tolls, Hormuz transits ran about 70% below the prewar level of 130 vessels per day, and the war risk premium kept the Brent forward curve elevated even as flat price drifted lower. The premium held the curve up because the danger was priced into every future transit, not just the barrel loading today.

## Why it matters (commodities and FX)

War risk premium is the channel that turns a [[Geopolitical Risk]] headline into a hard cost on the barrel. It is not sentiment; it is an insurance quote with underwriter capital behind it. That makes it one of the most reliable confirmation signals in the [[Geopolitical Repricing Sequence]]. When war risk premiums reprice 4 to 6 times higher on a specific route, someone is putting real money behind the assessment that a vessel might not make it. That sits well above implied vol on the evidence ladder, because vol can spike on rumor alone while an insurer only moves when it is willing to wear the loss.

For a crude trader the premium raises landed cost and freight simultaneously. Higher war risk premium lifts the delivered price of Gulf grades, widens sour differentials, and supports the [[Brent Crude]] curve, especially the front, because the danger is priced per transit. Crucially, the premium can keep the curve elevated even while flat price fades, because flat price reflects whether a barrel actually stopped while the premium reflects the standing cost of the danger. When the two disagree, the premium tells you the market still fears the transit even if nothing has failed yet.

The premium also drives routing and the [[Shadow Fleet]]. When war risk cover gets prohibitively expensive or unavailable, owners divert, slow steam, or refuse the voyage, and aging uninsured tonnage becomes the marginal carrier. For FX, sustained high premiums on a key export route raise the cost of that country's oil to buyers and can pressure importer currencies through a wider energy import bill.

## Concrete example

**Concrete:** A [[VLCC]] worth 100 million USD wants to transit the [[Strait of Hormuz]]. In calm times the additional war risk premium might be 0.05% of hull value, or 50,000 USD per transit. With the strait contested, underwriters reprice it to 0.5%, so the premium jumps to 500,000 USD for the single voyage. Add an Iranian transit toll of up to 2 million USD, Kharg or Hormuz style, and the vessel faces roughly 2.5 million USD of war related cost before it carries a barrel. Spread across a 2 million barrel cargo, that is about 1.25 USD per barrel of pure war risk, on top of the base [[Freight]] rate, which itself rises as owners demand danger compensation. That per barrel toll is why the [[Brent Crude]] forward curve stayed elevated even as the flat price drifted down toward 77 USD. The counter case: a ceasefire holds, transit counts recover toward the prewar 130 vessels per day, underwriters cut the premium back to 0.05%, the Iranian toll disappears, and the whole 1.25 USD per barrel wedge unwinds within weeks. The trade was to be long the curve and the premium before the escalation and to unwind into normalization, not to chase flat price at the peak.

**Simplified:** Sending a tanker through a war zone means buying special insurance priced as a slice of the ship's value. When the danger rises, that slice jumps from tiny to large, and the extra cost gets spread across every barrel on board, making delivered oil more expensive. Because the danger applies to every future trip, the premium props up the whole forward price of oil, not just today's. When the fighting stops and ships start moving normally again, the premium collapses and that extra cost drains out of the price.

## Key mechanics and formulas

Additional war risk premium as a per voyage cost:

`AWRP = hull value × AWRP rate`

Example: hull value 100 million USD, AWRP rate 0.5% → AWRP = 500,000 USD per transit.

Total war related cost per transit, adding a chokepoint toll:

`War cost per transit = (hull value × AWRP rate) + transit toll`

Example: 500,000 USD AWRP + up to 2,000,000 USD Iranian toll ≈ 2.5 million USD per transit.

Per barrel war risk toll:

`War risk per barrel = war cost per transit / cargo size`

Example: 2.5 million USD / 2 million bbl ≈ 1.25 USD per barrel.

Why the premium supports the curve: the AWRP applies to every future transit, so it lifts the delivered cost of deferred barrels, not just prompt ones. That is why the [[Forward Curve]] can stay elevated while flat price fades, and why the premium unwinds only when transit counts normalize and underwriters cut rates. Rough drivers of the AWRP rate: probability of a vessel being hit or seized, expected loss given a hit, and available underwriter capacity, which shrinks and raises rates when many owners want cover at once.

## Prerequisites

- [[Freight]]
- [[Chokepoint]]
- [[Forward Curve]]
- [[Brent Crude]]

## Related concepts (learn next)

- [[Strait of Hormuz]] — the chokepoint whose contestation drove the 2026 war risk repricing.
- [[Geopolitical Repricing Sequence]] — the timing model that ranks war risk insurance above vol as confirmation.
- [[Chokepoint]] — the geography that concentrates transit danger and therefore premium.
- [[Shadow Fleet]] — where cargoes go when war risk cover becomes too expensive or unavailable.
- [[Weather Premium]] — a parallel embedded premium, driven by weather risk rather than conflict.
- [[Geopolitical Risk]] — the broader driver that war risk premium prices into a hard cost.
- [[Forward Curve]] — the structure the premium supports, front more than back, per transit.

## Common misconceptions

**"War risk premium is just fear pricing."** It is an insurance quote with underwriter capital behind it, so it sits above implied vol on the evidence ladder. Vol reprices on rumor; a war risk premium moves when someone is willing to pay a real claim.

**"If flat price is falling, the war premium is gone."** Not necessarily. Flat price reflects whether a barrel actually failed to move, while the premium reflects the standing cost of the danger on every future transit. The premium can hold the curve up while flat price drifts down.

**"The premium is a fixed surcharge."** It is a percentage of hull value that reprices continuously with assessed danger and underwriter capacity. It can move 4 to 6 times within days on a credible escalation and collapse just as fast on a ceasefire.

**"War risk only affects the shipowner."** The cost passes through to the barrel. Spread across the cargo it becomes a per barrel toll that raises landed crude cost, widens sour differentials, and supports the benchmark curve that unrelated positions are marked against.

## Sources

- Lloyd's of London and the Joint War Committee, listed areas and war risk guidance
- BIMCO, war risk clauses for time and voyage charters (CONWARTIME, VOYWAR)
- International Group of P and I Clubs, war risk cover structure
- Platts and TradeWinds, coverage of Gulf war risk premium repricing and Hormuz transit counts
