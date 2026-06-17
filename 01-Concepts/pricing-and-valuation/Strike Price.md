---
aliases: [Exercise Price, Striking Price]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Strike Price

## Definition
The strike price is the fixed price at which the holder of an option may buy (for a [[Call Option]]) or sell (for a [[Put Option]]) the underlying. It is locked in when the contract is created and never changes over the life of the option. Plain English: it is the agreed price you can transact at no matter where the market goes, and it is the reference point everything else is measured against. Technically, the strike anchors the option on the [[Moneyness]] scale, determines how much of the [[Premium]] is [[Intrinsic Value]], and sets the threshold the underlying must cross before [[Exercise]] makes economic sense. Exchanges list strikes in standardized increments around the prevailing price.

## Why it matters (commodities and FX)
Picking the strike is the first real decision a commodities or FX trader makes after choosing direction. A strike near the money costs more premium but pays off sooner; a far OTM strike is cheap but needs a large move to matter. For a refiner hedging crude input costs or an exporter hedging EUR/USD receivables, the strike sets the protection level: it is the worst price you accept while keeping upside. The gap between where you place the strike and the forward price directly drives premium outlay, breakeven, and the leverage of the trade.

## Concrete example
**Concrete:** [[WTI Crude Oil]] front month trades at $80.00/bbl. You buy 1 December $85 call for a premium of $1.50/bbl. One CME crude option covers 1,000 barrels, so the premium paid is $1,500. The strike is $85: that is the price at which you can buy crude regardless of the market.
- Win case: at expiry WTI settles at $90.00. The $85 call is $5.00/bbl [[Intrinsic Value]] ($90 minus $85). You collect $5,000, subtract the $1,500 premium, net profit $3,500. Breakeven was $86.50 (strike plus premium), and the market cleared it.
- Fail case: at expiry WTI settles at $82.00. The $85 strike is above the market, so the call is worthless and you do not exercise. You lose the full $1,500 premium. Buying crude at $82 in the open market beats exercising at $85.

**Simplified:** The strike is the price you locked in. A call only has value if the market rises above the strike. Higher strike means cheaper option but a bigger move needed to pay off.

## Key mechanics and formulas
- Call intrinsic value = max(0, S - K), where S is the underlying spot or forward price and K is the strike.
- Put intrinsic value = max(0, K - S).
- Call breakeven = K + premium paid. Put breakeven = K - premium paid.
- Moneyness reference: for a call, S > K is in the money, S = K is at the money, S < K is out of the money. The reverse holds for puts.
- K (strike) is fixed at contract creation. S (underlying price) moves continuously. The distance between them drives both [[Intrinsic Value]] and the option's sensitivity to further moves.

## Prerequisites
- [[Call Option]]
- [[Put Option]]
- [[Premium]]
- [[Option]]

## Related concepts (learn next)
- [[Moneyness]] because the strike's position relative to spot defines whether the option is ITM, ATM, or OTM.
- [[Intrinsic Value]] because the strike is the exact threshold that determines how much intrinsic value an option holds.
- [[ATM]] because the at the money strike sits closest to spot and carries the most [[Time Value]].
- [[Exercise]] because the strike is the price you actually transact at when you exercise.
- [[Premium]] because moving the strike further from spot lowers the premium you pay.
- [[Delta]] because strike placement changes the option's delta and its probability of finishing in the money.
- [[Payoff Diagram]] because the kink in every option payoff graph sits exactly at the strike.

## Common misconceptions
- "A lower strike call is always better because you keep more upside." Wrong: a lower strike call costs more premium and has more intrinsic value, so it behaves more like the underlying and gives less leverage per dollar risked.
- "The strike changes if the market moves a lot." Wrong: the strike is fixed at creation. Only the underlying price moves, which changes [[Moneyness]], not the strike itself.
- "Reaching the strike means you make money." Wrong: you only profit once the underlying clears the strike plus the [[Premium]] paid. At the strike exactly, a long option holder is still down the full premium.

## Sources
- CME Group, "Options on Futures" educational guides.
- John C. Hull, "Options, Futures, and Other Derivatives," chapters on option mechanics.
- ICE, Energy and FX options contract specifications.
