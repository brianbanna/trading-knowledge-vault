---
aliases: [Expiration, Expiry, Maturity Date]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Expiration

## Definition
In plain English, expiration is the day a derivative contract dies. After it, the contract no longer exists and carries no further rights or obligations. For a [[Futures Contract]], reaching expiry triggers either [[Delivery]] of the underlying or [[Cash Settlement]], depending on the contract. For an [[Option]], the holder must exercise it or let it lapse, and at that point its [[Time Value]] is exactly zero, leaving only any intrinsic value. Trading does not run all the way to the expiry instant; it stops on the Last Trading Day, after which positions are settled or assigned.

## Why it matters (commodities and FX)
Expiration is where positions are forced to resolve, so it shapes both risk and behaviour. A trader who wants continuous exposure cannot simply hold one contract forever; they must roll to the next [[Front Month]] before expiry to avoid unwanted [[Delivery]]. That roll has a cost or benefit set by the shape of the curve, which directly affects the return of any rolling strategy or commodity index. Expiry also concentrates flows: many participants roll or settle in the same window, producing expiry related volatility and sometimes squeezes. Mismanaging expiry, for example forgetting to roll a physically settled crude position, can mean an obligation to take real barrels.

## Concrete example
**Concrete:** A trader is [[Long]] 1 July [[WTI Crude Oil]] future (NYMEX CL, 1,000 bbl) and wants to keep oil exposure past July expiry. CL is physically delivered, so holding into expiry would obligate them to take 1,000 barrels at Cushing. To avoid that they roll: sell the July contract and buy August, executed as a [[Calendar Spread]]. The roll cost depends on the curve. Contango case (loss): July is 78.00 and August is 78.90, so rolling means selling low and buying high, a roll cost of 0.90/bbl, or 900 USD, that drags on the position. Backwardation case (gain): July is 78.00 and August is 77.20, so rolling sells high and buys low, a roll gain of 0.80/bbl, or 800 USD. Same mechanical roll, opposite sign, set entirely by [[Contango]] versus [[Backwardation]].

**Simplified:** Near expiry you either take delivery or roll to the next month to stay in the trade. If the next month is more expensive (contango), rolling costs you. If it is cheaper (backwardation), rolling pays you.

## Key mechanics and formulas
Last Trading Day is the final session a contract can be traded; settlement or delivery follows. Roll PnL on a [[Long]] = near month price minus deferred month price, per unit (positive in [[Backwardation]], negative in [[Contango]]). For an [[Option]] at expiry, value = intrinsic only, since [[Time Value]] decays to zero: a call is worth max(S minus K, 0) and a put max(K minus S, 0). Settlement style matters: physically settled contracts (CL) require [[Delivery]] logistics, while cash settled contracts close to a reference price and avoid [[Delivery]] entirely.

## Prerequisites
- [[Futures Contract]]
- [[Option]]
- [[Front Month]]
- [[Delivery]]

## Related concepts (learn next)
- [[Time Value]]: understand why it collapses to zero exactly at expiry.
- [[Option]]: the [[Exercise]] versus lapse decision lives at expiration.
- [[Futures Contract]]: expiry forces settlement, so know the contract's settlement type.
- [[Front Month]]: the contract you roll into to maintain exposure.
- [[Delivery]]: the physical outcome to avoid or plan for if you hold to expiry.
- [[Cash Settlement]]: the alternative resolution that sidesteps physical delivery.
- [[Calendar Spread]]: the structure used to execute a roll in one trade.
- [[Exercise]]: the act that converts an in the money option at expiry.

## Common misconceptions
- "Expiry and Last Trading Day are the same." Wrong, because trading stops on the Last Trading Day while settlement or delivery is processed afterward; conflating them causes missed rolls.
- "Rolling is free." Wrong, because the roll captures the spread between expiries, which is a real cost in [[Contango]] and a real gain in [[Backwardation]].
- "An out of the money option keeps some value at expiry." Wrong, because [[Time Value]] is zero at expiry, so without intrinsic value it expires worthless.
- "Cash settled and physically settled contracts behave identically into expiry." Wrong, because only physically settled contracts can force [[Delivery]], which changes squeeze risk and how late you can safely hold.

## Sources
- NYMEX, Light Sweet Crude Oil (CL) contract specifications and Last Trading Day rules
- Hull, Options, Futures, and Other Derivatives, expiration, exercise, and settlement
- CME Group education, contract roll dates and calendar spreads
