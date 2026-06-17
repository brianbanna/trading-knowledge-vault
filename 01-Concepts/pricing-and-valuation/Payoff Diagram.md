---
aliases: [Profit and Loss Diagram, P&L Diagram, Hockey Stick Chart]
tags:
  - "#quant"
date-added: "2026-06-18"
---

# Payoff Diagram

## Definition
A payoff diagram is a plot of a position's profit or loss against the underlying price at [[Expiration]]. In plain terms, it answers one question visually: if the underlying settles at price X, how much do I make or lose? The horizontal axis is the underlying price, the vertical axis is profit and loss, and the line shows the result at each possible settlement level. Linear instruments like futures plot as straight diagonals, while options plot as kinked lines that bend at the [[Strike Price]]. Reading these shapes lets you see breakeven, maximum gain, and maximum loss at a glance.

## Why it matters (commodities and FX)
Payoff diagrams make risk visible before you trade. A commodity desk hedging [[WTI Crude Oil]] exposure can instantly see whether a structure caps its loss or leaves an open tail. They are the building blocks for every multi leg strategy: spreads, collars, and straddles are just sums of the four basic shapes below. In FX and commodities, where moves can be violent, knowing whether your downside is capped at the [[Premium]] or unlimited is the difference between a defined risk trade and a blowup.

## The 4 building blocks
1. [[Long]] [[Futures Contract]]: a diagonal sloping up. You profit one for one as the price rises, lose one for one as it falls.
2. [[Short]] [[Futures Contract]]: a diagonal sloping down. You profit as the price falls, lose as it rises.
3. [[Long]] [[Call Option]]: flat at a loss equal to the [[Premium]] below the [[Strike Price]], then sloping up once price clears the strike. Maximum loss is capped at the premium paid.
4. [[Long]] [[Put Option]]: sloping down (profit) as price falls below the strike, then flat at a loss equal to the premium above the strike.

```
Long Future                         Short Future
P&L                                 P&L
 |        /                          |\
 |       /                           | \
 |      /                            |  \
-+-----/------- price               -+---\--------- price
 |    /                             |     \
 |   /                              |      \
```

```
Long Call (strike K)                Long Put (strike K)
P&L                                 P&L
 |          /                        |\
 |         /                         | \
 |        /                          |  \
-+-------+-K------ price            -+---+-K-------- price
 |_______|  (loss = premium)        |    |________  (loss = premium)
   flat                                    flat
```

## Concrete example
**Concrete:** You go [[Long]] a [[Call Option]] on [[WTI Crude Oil]] with [[Strike Price]] K = $80 per barrel and pay a [[Premium]] of $5 per barrel.

Breakeven. You only start making net money once the gain on the option covers the $5 you paid, so breakeven = strike + premium = 80 + 5 = $85.

Win case. WTI settles at $92. Gross payoff = max(92 - 80, 0) = $12. Subtract the $5 premium and net profit = $7 per barrel. On a 1,000 barrel contract that is $7,000. The payoff line slopes up one for one above $80.

Fail case. WTI settles at $76. Gross payoff = max(76 - 80, 0) = $0. You lose only the $5 premium, the maximum possible loss. The line is flat at minus $5 for every settlement below $80, so the position behaves identically whether oil ends at $76 or $40: your loss is capped at $5 per barrel, or $5,000 on the contract.

Mirror note. If instead you had sold (gone [[Short]]) that same call, your payoff diagram is the mirror image flipped across the horizontal axis: your gain is capped at the $5 premium collected, while your loss grows without limit as WTI rises far above $80. Short option payoffs always invert the long shape, swapping capped loss for capped gain and capped gain for large or unlimited loss.

**Simplified:** A payoff diagram draws your profit against where the market settles. A long $80 call is a flat $5 loss until oil reaches $80, then it climbs, breaking even at $85 and profiting above. Selling that call gives you the opposite picture: a small fixed gain and a large open risk.

## Key mechanics and formulas
- Long [[Call Option]] payoff: max(S - K, 0) - Premium.
- Long [[Put Option]] payoff: max(K - S, 0) - Premium.
- Long [[Futures Contract]] payoff: S - entry price (linear).
- Short [[Futures Contract]] payoff: entry price - S (linear).
- Long call breakeven: K + Premium. Long put breakeven: K - Premium.
- Short option payoff = minus (long option payoff): capped gain at premium collected, large or unlimited loss.
- Multi leg strategy payoff = sum of the individual leg payoffs at each price.

## Prerequisites
- [[Call Option]] and [[Put Option]] payoffs at expiry.
- [[Long]] and [[Short]] positions.
- [[Strike Price]] and [[Premium]].
- Basic understanding of a [[Futures Contract]].

## Related concepts (learn next)
- [[Call Option]]: the long version produces the flat then up shape you just read.
- [[Put Option]]: the long version produces the down then flat shape.
- [[Strike Price]]: the kink point where every option payoff line bends.
- [[Premium]]: sets the vertical offset and therefore the breakeven of each option leg.
- [[Long]]: the direction whose payoff shapes are the base case before mirroring.
- [[Short]]: the mirror direction that inverts each long payoff into capped gain and open risk.
- [[Futures Contract]]: the linear instrument whose diagonal payoff anchors hedging structures.

## Common misconceptions
- "Payoff diagrams show profit before expiration." Wrong. The standard payoff diagram is the value at [[Expiration]], when [[Time Value]] is gone. Before expiry the position's value follows a curved line that sits above the kinked expiry payoff.
- "A long call and a short call have the same risk just in opposite directions." Wrong. A long call caps loss at the [[Premium]] with open upside, while a short call caps gain at the premium with large or unlimited loss. The risk profiles are not symmetric in danger.
- "The breakeven of a long call is the strike price." Wrong. Breakeven is strike plus premium, because you must first recover what you paid before the position turns profitable.
- "Buying options is always safer than futures because loss is capped." Wrong. The capped loss is real, but [[Time Value]] decay means a long option can lose its entire premium even when the underlying barely moves, a failure mode a futures position does not have.

## Sources
- Hull, Options, Futures, and Other Derivatives.
- CME Group education materials on options strategy payoffs.
