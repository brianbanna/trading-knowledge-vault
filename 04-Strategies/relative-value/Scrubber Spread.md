---
aliases: [scrubber spread, hi5 spread, hi-5 spread, vlsfo hsfo spread, hsfo vlsfo spread, sulphur spread]
tags:
  - "#freight/wet"
  - "#energy/refined"
date-added: "2026-06-17"
---

# Scrubber Spread

## Definition
The scrubber spread is the price difference between two marine fuels: compliant low sulphur fuel oil (VLSFO, 0.5 percent sulphur) minus the dirty, cheap high sulphur fuel oil (HSFO, 3.5 percent sulphur). Think of it as the toll a ship pays for burning clean fuel instead of dirty fuel. Since the IMO 2020 sulphur cap, a ship may only burn HSFO if it is fitted with a scrubber (an exhaust gas cleaning system that washes sulphur out of the flue gas), so the spread is exactly the per tonne saving that a scrubber captures. In Singapore the spread is quoted as the "Hi5" (high sulphur 380 CST versus VLSFO). Technically, `scrubber_spread = price_VLSFO - price_HSFO`, expressed in USD per tonne, and it is the economic input that decides whether a scrubber is a money making asset or a stranded cost.

## Why it matters (commodities and FX)
For a freight or shipping trader the scrubber spread is two things at once. First, it is a directly tradeable fuel switching spread: refiners, bunker desks, and shipowners express views on it through HSFO and VLSFO swaps and futures, and it drives the residual fuel complex. Second, it is the single number that determines the return on a multi million dollar capital decision, namely whether to retrofit a vessel with a scrubber. A wide spread means a scrubber fitted ship burns cheap HSFO and pockets the difference, improving its [[Time Charter Equivalent|TCE]] versus a non scrubber sister ship on the same route. A narrow spread strands that capex. The spread is volatile and regime dependent: it blew out around the 2020 cap as the market scrambled for compliant fuel, collapsed when demand fell and refiners ramped VLSFO supply, then reflated whenever refining capacity tightened. Because it mean reverts around refinery economics and regulatory enforcement, it is a classic relative value play rather than a simple directional bet on crude.

## Concrete example
**Concrete:** A handysize tanker owner is deciding whether to fit a scrubber. Capex is 3,000,000 USD installed, the vessel burns 10,000 tonnes of fuel per year, and it has roughly 8 years of economic life left. At the time of the decision the Hi5 spread is 150 USD/t (VLSFO at 600, HSFO at 450). With a scrubber the ship burns HSFO and saves the full spread, so the annual saving is `10,000 t x 150 USD/t = 1,500,000 USD`. Payback is `3,000,000 / 1,500,000 = 2.0 years`, comfortably inside the 8 year window, so the scrubber is a strong asset. Now run the downside. Suppose 18 months later refiners have flooded the market with VLSFO and HSFO demand recovers; the spread compresses to 50 USD/t. The annual saving falls to `10,000 x 50 = 500,000 USD` and remaining payback on the unrecovered capex stretches toward 6 years, near or beyond the economic window. The scrubber now carries maintenance and downtime cost without recovering its capital, so it is dead weight. A trader who wanted to express a view rather than own steel would trade the paper spread instead. Going long the spread (long VLSFO swap, short HSFO swap) at 150 USD/t and seeing it widen to 250 USD/t on a refining outage earns 100 USD/t on the notional. Going long at 150 and watching it collapse to 40 USD/t as HSFO demand returns loses 110 USD/t. The same spread move that vindicates the scrubber retrofit also pays the paper long, and vice versa.

**Simplified:** Clean fuel costs more than dirty fuel. A scrubber lets your ship burn the cheap dirty fuel legally, so it saves you the price gap on every tonne. If the gap is big (150 USD/t), the scrubber pays for itself in about 2 years and prints money after that. If the gap shrinks to 50 USD/t, the saving is small, the scrubber takes 6 years to pay back, and you may have wasted the money. You can also just bet on the gap directly: bet it widens and win if clean fuel gets scarcer, bet it narrows and win if dirty fuel demand comes back.

## Key mechanics and formulas
- `scrubber_spread = price_VLSFO - price_HSFO` where `price_VLSFO` is the 0.5 percent compliant fuel price in USD/t and `price_HSFO` is the 3.5 percent high sulphur fuel price in USD/t. A positive spread is normal; VLSFO trades at a premium because it is the compliant default.
- `annual_saving = annual_consumption_tonnes x scrubber_spread` where `annual_consumption_tonnes` is the vessel's yearly fuel burn. This is the gross cash a scrubber generates.
- `scrubber_payback_years = capex / (annual_consumption_tonnes x scrubber_spread)` where `capex` is the installed cost of the exhaust gas cleaning system. A wider spread shortens payback; a narrower spread lengthens it, and if payback exceeds remaining economic life the capex is stranded.
- `pnl_paper_long = (spread_exit - spread_entry) x notional_tonnes` for a long VLSFO / short HSFO position. The trade is long the spread when you expect the compliant premium to widen.
- Quoting note: in Singapore the spread is the "Hi5" (VLSFO minus 380 CST HSFO). In Rotterdam and the Gulf the underlying grades differ slightly but the logic is identical.

## Prerequisites
[[Bunkers, IFO versus MGO, and the Bunker Hedge]]
[[Spread Trade]]
[[Bunker Risk]]

## Related concepts (learn next)
- [[Bunker Risk]] — the scrubber spread is the specific risk that decides whether a scrubber retrofit hedges or amplifies your fuel exposure.
- [[Basis Risk]] — a scrubber spread hedge can drift from your actual port and grade, leaving residual basis between the swap and the physical bunker bill.
- [[EEXI and CII Regulations]] — emissions rules interact with scrubber economics because wash water bans and carbon intensity scoring change where and whether a scrubber helps.
- [[Freight Rate Risk]] — scrubber savings flow into the vessel's earnings, so the spread feeds directly into freight and [[Time Charter Equivalent|TCE]] competitiveness.
- [[Hedging]] — owners lock in the spread with HSFO and VLSFO swaps to protect a scrubber investment thesis against compression.
- [[Forward Curve]] — the term structure of HSFO and VLSFO tells you whether the market expects the spread to hold, widen, or collapse over the retrofit horizon.
- [[Voyage Charter]] — under a voyage charter the owner pays bunkers, so a scrubber fitted ship on voyage business captures the spread directly.
- [[Time Charter]] — under a time charter the charterer pays bunkers, so the spread benefit and any scrubber premium must be negotiated into the hire or fuel terms.

## Common misconceptions
- "A scrubber always pays because HSFO is cheaper." Wrong. The scrubber only pays if the spread stays wide enough to recover capex plus maintenance over the vessel's remaining life. A compressed spread of 50 USD/t can push payback past the economic window, turning the scrubber into a sunk cost that still incurs maintenance and downtime.
- "The spread is stable so the saving is predictable." Wrong. The spread is one of the most volatile relationships in the residual complex. It is driven by refinery configuration, crude slate, regulatory enforcement, and the HSFO demand created by the scrubber fleet itself, so it swings across regimes and mean reverts unpredictably.
- "VLSFO and HSFO are basically the same fuel now." Wrong. They differ in sulphur content, price, blend composition, and they trade on separate futures and swap curves. Treating them as interchangeable destroys the entire economic logic of the spread and of the scrubber decision.
- "If I fit a scrubber I no longer have fuel price risk." Wrong. You swap absolute fuel price risk for spread risk. Your saving depends on VLSFO minus HSFO, so a parallel move in both prices leaves your scrubber payback unchanged while a spread compression hurts you even if outright fuel prices fall.

## Sources
- IMO 2020 sulphur cap (MARPOL Annex VI) and exhaust gas cleaning system guidance.
- Ship and Bunker, daily VLSFO and HSFO prices and the Singapore Hi5 spread.
- Platts and Argus bunker fuel methodology, residual fuel oil assessments (0.5 percent and 3.5 percent grades).
- Alizadeh and Nomikos, Shipping Derivatives and Risk Management, on fuel and freight hedging.
- Kavussanos and Visvikis, The International Handbook of Shipping Finance, on vessel capex and operating economics.
- Stopford, Maritime Economics, on bunker costs and vessel operating expense structure.
- Clarksons SIN and ICE/CME fuel oil swap and futures specifications.
