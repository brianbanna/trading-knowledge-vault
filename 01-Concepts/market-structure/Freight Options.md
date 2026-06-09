---
aliases: [freight options, ffa options, asian freight option, freight cap, freight floor]
tags:
  - "#freight/ffa"
date-added: "2026-06-09"
---
# Freight Options
## Definition
A freight option is the right, but not the obligation, to receive the difference between an agreed freight level and where the freight market actually settles, in exchange for a one off premium paid up front. Think of it as insurance on the price of shipping. You pay a small fee now, and if the market moves against you past a chosen level, the option pays you back the difference, while if the market stays friendly you simply let the fee lapse. Technically these are options written on a [[Forward Freight Agreement]] route, almost always Asian style, meaning they settle against the average Baltic assessment over a calendar period rather than a single closing price. A call pays off when freight rates rise above the strike, a put pays off when freight rates fall below the strike, and both settle in cash against the relevant Baltic index. The premium is driven by how far the strike sits from the forward, how long until expiry, and the [[Implied Volatility]] of the route.
## Why it matters (commodities and FX)
Freight is one of the most volatile cost components a commodity flow carries, and a freight option lets a trader cap or floor that exposure without locking in a fixed rate the way a plain [[Forward Freight Agreement]] does. A charterer who must move cargo in 3 months fears a rising market, so they buy a call (a cap) that pays out if rates spike, while still keeping the upside of a cheap spot fixture if the market falls. An owner with vessels to deploy fears a collapsing market, so they buy a put (a floor) that pays out if rates crater, while keeping the full benefit of a roaring market if rates rise. Unlike an FFA, an option costs only the premium and never produces a margin call against a favourable move, which is why physical players who want protection but not a locked rate gravitate toward them. They also let a trader express a pure view on [[Volatility]] itself, buying options when the route looks cheap to insure and selling them to collect premium when the market overpays for protection.
## Concrete example
**Concrete:** It is January and a Panamax owner controls a vessel that will open in the Atlantic in Q2. The Q2 Panamax FFA on the [[Baltic Route Codes]] P4TC time charter basket trades at 14,000 USD per day, and the owner is nervous that a weak grain season pushes spot rates down hard. Rather than sell the FFA outright and give up all upside, the owner buys a Q2 put struck at 13,000 USD per day for a premium of 700 USD per day, which over a 65 day quarter costs roughly 45,500 USD for the position. Case it works: the Atlantic market collapses and the Q2 average P4TC settles at 9,000 USD per day. The put pays the strike minus the settlement, 13,000 minus 9,000 equals 4,000 USD per day, or about 260,000 USD across the quarter. Net of the 45,500 premium the owner banks roughly 214,500 USD, which cushions the brutal spot earnings the physical vessel actually achieves. Case it fails: freight stays firm and the Q2 average settles at 16,000 USD per day. The put expires worthless because nobody exercises the right to sell at 13,000 when the market is 16,000, and the owner simply loses the 45,500 premium. That is the cost of the insurance, and it is more than covered by the strong rates the physical vessel earned. The premium is the maximum loss either way.
**Simplified:** The owner pays a fee to lock in a worst case daily rate of 13,000. If the market crashes below that, the option refunds the gap and the owner is protected. If the market stays strong, the fee is wasted but the owner is making good money anyway, so it stings little.
## Key mechanics and formulas
- Payoff of a freight call at expiry: `payoff = max(A - K, 0) x D` where `A` is the average Baltic assessment over the period, `K` is the strike rate, and `D` is the number of index days in the period. The buyer of the call (the charterer capping cost) receives this.
- Payoff of a freight put at expiry: `payoff = max(K - A, 0) x D` where the buyer of the put (the owner flooring earnings) receives this.
- Net result to the option buyer: `net = payoff - premium_total` where `premium_total = premium_per_day x D`, paid up front regardless of outcome.
- Asian settlement: the option settles against the arithmetic average of the daily Baltic assessment across the settlement period, not a single price, which lowers the effective [[Volatility]] seen by the option and therefore cheapens it versus a European option on a single fixing.
- Premium drivers: distance of strike from the forward (moneyness), time to expiry, and [[Implied Volatility]] of the route. Freight vol is high, often 40 to 80 percent annualised, so freight option premiums are rich relative to many commodity options.
- Charterer logic: buy calls to cap cost, because their pain is a rising market. Owner logic: buy puts to floor earnings, because their pain is a falling market. Either side can also sell the opposite leg to fund the premium, building a collar.
- Quoting: premiums quote in USD per day for dry routes (matching the per day FFA convention) and in Worldscale points or USD per tonne for tanker routes. See [[Freight]] for the rate conventions.
## Prerequisites
- [[Forward Freight Agreement]]
- [[Option]]
- [[Baltic Exchange and the Dry Indices]]
- [[Baltic Route Codes]]
- [[Freight]]
- [[Implied Volatility]]
## Related concepts (learn next)
- [[Vanilla Option]] explains the basic call and put structure that the freight option inherits before the Asian averaging is layered on.
- [[Implied Volatility]] is the single largest swing factor in a freight option premium, so understanding how it is backed out is essential to pricing.
- [[Forward Freight Agreement]] is the underlying instrument the option settles against, so its mechanics directly drive the option payoff.
- [[Volatility]] underpins why freight options are expensive and how realised versus implied vol decides whether buying or selling them pays.
- [[Hedging]] frames how a physical owner or charterer combines options with FFAs and the physical book to manage net exposure.
- [[Value at Risk]] shows how option positions reshape the tail of a freight book, since a bought option caps downside while a sold option opens it.
- [[Time Charter]] is the physical contract whose floating earnings an owner is often hedging with a put on the time charter basket.
- [[Voyage Charter]] is the physical contract whose cost a charterer is often capping with a call on the relevant voyage route.
## Common misconceptions
- **"A freight option settles against the spot rate on expiry day like a stock option."** Wrong. Freight options are Asian style and settle against the average Baltic assessment across the whole settlement period, usually a calendar month or quarter. A single bad day near expiry does not blow up or rescue the position, which dampens the payoff and lowers the premium versus a European single fixing option.
- **"Buying a freight option is the same as taking an FFA position."** Wrong. An FFA is a symmetric obligation that gains and loses linearly and can produce margin calls against you, whereas an option costs a fixed premium, has capped loss for the buyer, and never demands more cash once the premium is paid. The option buyer keeps favourable moves entirely while shedding the unfavourable tail.
- **"Owners buy calls and charterers buy puts."** Backwards. Owners fear falling rates so they buy puts (floors) to protect earnings, and charterers fear rising rates so they buy calls (caps) to protect cost. Reversing this leaves the hedge facing the wrong direction.
- **"If the option expires worthless the trade was a mistake."** Wrong. A worthless expiry means the market moved in your favour and the physical position prospered, so the premium was the price of insurance you ended up not needing. Judging an option only by whether it paid out ignores the protection it provided across the full range of outcomes.
## Sources
- Baltic Exchange, FFA and freight derivatives market guides, https://www.balticexchange.com
- Manolis G. Kavussanos and Ilias D. Visvikis, Derivatives and Risk Management in Shipping
- Amir H. Alizadeh and Nikos K. Nomikos, Shipping Derivatives and Risk Management
- FFABA (Forward Freight Agreement Brokers Association) standard terms and option contract templates
- John C. Hull, Options, Futures, and Other Derivatives, chapters on Asian options and average price options
