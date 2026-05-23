---
aliases: [last look, last look window, trade rejection]
tags:
  - "#fx"
  - "#microstructure"
date-added: "2026-03-20"
---

# Last Look

## Definition
Last look is the dealer's right to accept or reject a client trade request during a brief window (50 to 200 ms) after submission. During that window the dealer checks if the market moved against them; if it crossed a threshold, the trade is rejected and the client must resubmit at a worse price. Originally designed to protect dealers from latency arbitrage by HFTs exploiting stale quotes, the practice became controversial because some dealers apply it asymmetrically: rejecting losing trades while accepting winning ones. The FX Global Code (2017) pushed for transparency.

## Why it matters (commodities and FX)
Last look is one of the largest hidden costs in FX execution. Ignoring it understates [[transaction costs]] systematically. For commodity funds executing large FX hedges through [[Single Dealer Platform]]s, rejections add 0.5 to 2 pips to effective cost. The drag compounds for momentum strategies and [[CTA]]s: their orders trade with recent moves, so the market is more likely to be running against the dealer during the last look window, raising rejection rates. In commodities OTC, the analogous distinction is "firm vs indicative" pricing, where dealers can withdraw indicative metals or energy swap quotes before execution.

## Concrete example

**Concrete:** A systematic macro fund running [[momentum]] detects a GBPUSD breakout and sends a 50M buy to a bank SDP at 1.26500. The bank applies a 100 ms last look. During those 100 ms, GBPUSD ticks up 0.8 pips to 1.26508. The bank rejects because the price moved against them past the 0.5 pip threshold. The fund resubmits and fills at 1.26510, paying 1 pip more. Over a year, TCA shows a 15% rejection rate and 0.7 pips average post rejection slippage, dragging strategy performance by 12 bps annualized. A corporate treasurer hedging a known receivable on the same platform sees a 2% rejection rate: the bank flags that flow as low [[toxicity]].

**Simplified:** You send the bank an order. The bank waits 100 ms before saying yes or no. If the price moved in your favor in that window, the bank says no and you must trade again at a worse price. If the price moved their way, they say yes. Either way, the bank wins the optionality during the wait. That free option is the hidden cost.

## Key mechanics and formulas
- **Last look window:** 50 to 200 ms (some venues up to 500 ms)
- **Rejection threshold:** minimum adverse move (pips) that triggers rejection
- **Asymmetric last look cost:** Cost = rejection rate × average slippage on rejected trades
- **Effective spread:** displayed spread + (rejection rate × post rejection slippage) + hold time cost
- **Symmetry test:** compare fill rate when price moves client favor vs dealer favor. Equal = symmetric. Unequal = asymmetric (potentially predatory).
- **Hold time:** some dealers delay acceptance (not just rejection) to capture additional favorable movement, an implicit cost on accepted trades

## Prerequisites
- [[Single Dealer Platform]]
- [[Bid-Ask Spread]]
- [[Latency]]
- [[Market Making]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: the primary venue where last look applies.
- [[Internalization]]: banks that internalize flow apply last look less aggressively since they profit from spread.
- [[ECN]]: most ECNs operate firm quote without last look, though some use speed bumps.
- [[Flow Signals]]: last look gives dealers a free option on client flow information.
- [[Toxicity]]: the classification that determines how aggressively last look applies to a client.
- [[Transaction Cost Analysis]]: proper TCA must measure rejection rates and post rejection slippage.
- [[Sweep]]: aggressive orders face more rejection because they signal informed intent.

## Common misconceptions

**"Last look only protects against stale quotes."** Original justification was latency, but in practice the dealer observes the order, watches the market move, then decides. That is a free option on client flow.

**"Low rejection rates mean fair execution."** A dealer can accept all trades but delay favorable fills and accelerate unfavorable ones. Rejection rate 0%, execution still asymmetric.

**"The FX Global Code eliminated last look abuse."** The 2017 Code discourages asymmetry but is voluntary and not legally binding. Enforcement relies on participants refusing non compliant dealers.

## Sources
- Global Foreign Exchange Committee, "FX Global Code" (2017, updated 2021)
- Oomen, Roel, "Last Look," Working Paper, Deutsche Bank (2017)
- Cartea, Alvaro et al., "Algorithmic and High-Frequency Trading," Cambridge University Press (2015)
- Financial Conduct Authority, "FX Market Study: Final Report" (2015)
