---
aliases: [last look, last look window, trade rejection]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Last Look

## Definition
Last look is a practice in FX markets where a liquidity provider (typically a bank on a [[Single Dealer Platform]]) retains the right to accept or reject a client's trade request for a brief window after the client submits the order. This window typically lasts 50 to 200 milliseconds. During that time, the dealer checks whether the market has moved against them; if it has moved beyond a threshold, the trade is rejected and the client must re-submit at a new (worse) price. Last look was originally designed to protect dealers from latency arbitrage by high-frequency traders who could exploit stale quotes. However, it has become controversial because some dealers use it asymmetrically: rejecting trades that would be unprofitable while accepting trades that have moved in the dealer's favor (a practice called "asymmetric last look" or "last look with price improvement skew"). Regulators and industry codes (notably the FX Global Code of 2017) have pushed for greater transparency around last look practices.

## Why it matters (commodities and FX)
Last look is one of the largest hidden costs in FX execution, and failing to account for it leads to systematically underestimating [[transaction costs]]. For commodity hedge funds that execute large FX hedges through bank [[Single Dealer Platform]]s, last look rejection can add 0.5 to 2 pips to effective execution cost. The issue compounds for momentum or trend-following strategies (like those run by [[CTA]]s) because these strategies tend to trade in the direction of recent price moves, which means their orders are more likely to be moving in the same direction as the market during the last look window and thus more likely to be rejected. In commodities OTC markets, analogous "firm vs. indicative" pricing distinctions exist, where dealers quote indicative prices on metals or energy swaps that they can withdraw before execution.

## Concrete example
A systematic macro fund running a [[momentum]] strategy detects a GBPUSD breakout and sends a buy order for 50 million to a bank's SDP at 1.26500. The bank applies a 100 millisecond last look window. During those 100 milliseconds, GBPUSD moves up 0.8 pips to 1.26508. The bank's algorithm rejects the trade because the price moved in the client's favor (i.e., against the bank) by more than the 0.5 pip threshold. The fund re-submits and gets filled at 1.26510, paying 1 pip more than the original price. Over a year, the fund's [[transaction cost analysis]] reveals a 15% rejection rate and an average post-rejection slippage of 0.7 pips, adding an annualized drag of approximately 12 basis points to strategy performance. Meanwhile, a corporate treasurer hedging a known receivable (uninformed, non-directional flow) experiences a 2% rejection rate on the same platform because the bank classifies this flow as low-[[toxicity]].

## Key mechanics and formulas
- **Last look window**: typically 50 to 200 milliseconds (some venues allow up to 500 ms)
- **Rejection threshold**: the minimum adverse price movement (in pips) that triggers rejection; set by the dealer
- **Asymmetric last look cost**: Cost = rejection rate x average slippage on rejected trades
- **Effective spread with last look**: Effective spread = displayed spread + (rejection rate x post-rejection slippage) + (hold time cost if dealer delays acceptance)
- **Symmetry test**: Compare fill rate when price moves in client's favor vs. fill rate when price moves in dealer's favor. Equal rates = symmetric last look. Unequal rates = asymmetric (potentially predatory).
- **Hold time**: some dealers delay acceptance (not just rejection) to capture additional favorable price movement; this "hold time" adds implicit cost even on accepted trades

## Prerequisites
- [[Single Dealer Platform]]
- [[Bid-Ask Spread]]
- [[Latency]]
- [[Market Making]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: the primary venue where last look is applied.
- [[Internalization]]: banks that internalize flow may apply last look less aggressively since they profit from the spread rather than hedging.
- [[ECN]]: most ECNs operate on a firm-quote basis without last look, though some ECN-style platforms have introduced "speed bumps."
- [[Flow Signals]]: last look gives dealers a free option on client flow information during the rejection window.
- [[Toxicity]]: the classification that determines how aggressively last look is applied to a given client.
- [[Transaction Cost Analysis]]: proper TCA must measure rejection rates and post-rejection slippage.
- [[Sweep]]: aggressive orders are more likely to face last look rejection because they signal informed directional intent.

## Common misconceptions
1. **"Last look only protects against stale quotes"**: While the original justification was latency protection, in practice last look gives dealers an informational advantage. They observe the client's order, see how the market moves, and then decide whether to accept. This is economically equivalent to a free option on the client's flow.
2. **"Low rejection rates mean fair execution"**: A dealer can accept all trades but systematically delay fills when the price is moving in the client's favor and execute immediately when the price is moving in the dealer's favor. The rejection rate is 0%, but the execution is still asymmetric.
3. **"The FX Global Code eliminated last look abuse"**: The 2017 FX Global Code discourages asymmetric last look but is voluntary and not legally binding. Enforcement relies on market participants refusing to trade with non-compliant dealers.

## Sources
- Global Foreign Exchange Committee, "FX Global Code" (2017, updated 2021)
- Oomen, Roel, "Last Look," Working Paper, Deutsche Bank (2017)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- Financial Conduct Authority, "FX Market Study: Final Report" (2015)
