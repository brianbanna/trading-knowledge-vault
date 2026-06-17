---
aliases: [Gearing, Leverage Ratio]
tags:
  - "#risk"
date-added: "2026-06-18"
---

# Leverage

## Definition
Leverage is controlling a large position with only a small amount of your own capital. In futures you do this through [[Margin]]: you post a fraction of the contract's value as a good faith deposit and control the full [[Notional]] exposure. In options you do it through the [[Premium]]: you pay a small price to control a much larger underlying value. The leverage ratio is simply the notional exposure divided by the capital you posted. Because your profit and loss is calculated on the full notional but funded by a sliver of capital, leverage amplifies both gains and losses in the same proportion. The hidden danger is that adverse moves trigger margin calls, which can force liquidation at the worst possible moment.

## Why it matters (commodities and FX)
Commodity and FX futures are inherently high leverage instruments because exchange margins are small relative to contract value. This is what lets a producer hedge millions of barrels or a trader express a macro view with modest capital. But it is also the single fastest way to blow up an account. A move that looks tiny in percentage terms on the underlying can wipe out the entire margin posted. Understanding your true leverage ratio, not just the dollar size, is the difference between sizing a [[Position]] you can hold through volatility and one that gets stopped out by routine noise.

## Concrete example
**Concrete:** Take 1 [[WTI Crude Oil]] futures contract. Contract size is 1,000 barrels. At $80 per barrel the [[Notional]] exposure is 1,000 x $80 = $80,000. The exchange initial [[Margin]] is roughly $6,000. So your leverage ratio is $80,000 / $6,000 = roughly 13x. Each $1 move in oil equals 1,000 x $1 = $1,000 of profit or loss, which is about 17% of your $6,000 margin from a 1.25% move in the underlying.

Win case: you go [[Long]] at $80 and oil rises $5 to $85. Profit is 1,000 x $5 = $5,000. On $6,000 posted that is an 83% gain from a 6.25% move in oil. [[Mark to Market]] credits the $5,000 to your account daily as the price climbs.

Fail case: you go long at $80 and oil falls $5 to $75. Loss is 1,000 x $5 = $5,000. Your $6,000 margin is now nearly gone. The daily mark to market debits the loss, your equity drops below the maintenance margin, and the broker issues a margin call. If you cannot post more cash, the position is force liquidated at $75, locking in the $5,000 loss even if oil rebounds the next day.

**Simplified:** Leverage lets $6,000 control $80,000 of oil, about 13 times your money. A small move in oil becomes a huge move in your account. Up $5 and you make $5,000. Down $5 and you lose $5,000 and likely get force sold. Same tool, both directions.

## Key mechanics and formulas
- Leverage ratio = [[Notional]] exposure / capital posted.
- Notional = contract size x price x number of contracts.
- P&L per unit move = contract size x price change x number of contracts.
- Return on margin = P&L / capital posted, which is the underlying return multiplied by the leverage ratio.
- Margin call triggers when equity falls below maintenance margin; failure to top up leads to forced liquidation.
- Options leverage runs through the [[Premium]]: a small premium controls a large underlying, but the position can decay to 0.

## Prerequisites
- [[Margin]]
- [[Notional]]
- [[Futures Contract]]
- [[Long]] and [[Short]]
- [[Mark to Market]]

## Related concepts (learn next)
- [[Margin]] because it is the mechanism that creates futures leverage, and maintenance levels define when you get force liquidated.
- [[Notional]] because the leverage ratio is built directly from notional exposure over capital.
- [[Mark to Market]] because daily settlement is what turns a paper loss into a margin call that can force you out.
- [[Premium]] because options deliver leverage through a small upfront cost rather than margin, with a different risk profile.
- [[Futures Contract]] because contract size and exchange margin set the baseline leverage you start with.
- [[Position]] because correct position sizing relative to leverage is the core discipline that keeps leverage survivable.

## Common misconceptions
- "More leverage means more profit." Wrong. Leverage scales both profit and loss equally. Higher leverage also tightens the move that triggers a margin call, so it raises the probability of being force liquidated before your thesis plays out.
- "I only risk the margin I posted." Wrong. Futures losses can exceed the initial margin. If the market gaps past your stop, you owe the full loss, not just the deposit, and the broker can demand more.
- "Low underlying volatility makes high leverage safe." Wrong. Even calm markets gap on news. At 13x, a routine 8% adverse move in oil wipes out the entire margin, so the safety of leverage depends on tail risk, not the average day.

## Sources
- CME Group, performance bond (margin) and contract specifications for WTI Crude Oil.
- CFTC, customer education on the risks of leveraged futures trading.
