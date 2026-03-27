---
aliases: [multi dealer platform, MDP, multi-dealer platform, multi-bank platform]
tags:
  - "#microstructure"
  - "#fx/structure"
date-added: "2026-03-27"
---

# Multi Dealer Platform

## Definition
A Multi Dealer Platform (MDP) is an electronic trading venue where clients can simultaneously view and compare prices streamed by multiple banks or liquidity providers. The client selects the best price from a competitive panel rather than relying on a single dealer's quote. Major MDPs in FX include Bloomberg FXGO, 360T, FXall (now part of Refinitiv), and Currenex. MDPs differ from [[ECN]]s because prices are typically bilateral (each bank streams its own price to the client) rather than consolidated into a single anonymous [[Central Limit Order Book]]. The key advantage is competitive tension: banks know they are being compared, which tightens [[bid-ask spread]]s for the client.

## Why it matters (commodities and FX)
MDPs are the primary execution venue for corporate and institutional FX hedging. When a commodities firm needs to convert USD revenues from an oil sale into EUR, it will typically execute on an MDP to get competitive pricing from 5 to 15 banks simultaneously. The MDP model also extends to commodity [[swap]]s and [[forward contract]]s traded OTC, where platforms like Bloomberg and ICE allow clients to request prices from multiple dealers. Understanding MDP dynamics is essential because the pricing a client sees on an MDP is not the same as the interbank price on [[EBS]] or [[Reuters Matching]]. Banks apply [[skew]] and [[spread]] adjustments based on client profitability, flow toxicity, and inventory. A trader who does not understand this will misjudge execution quality.

## Concrete example
A Swiss commodity trading house needs to sell 50 million GBP/USD to hedge revenue from a metals contract. On 360T, the platform shows live streaming prices from 8 banks. The best bid is 1.26835 from Bank A, second best is 1.26830 from Bank B, and the worst is 1.26810 from Bank E. The trader clicks Bank A's bid and fills 50 million at 1.26835. The mid market on [[Reuters Matching]] at that moment is 1.26840, meaning the effective spread is 2 x (1.26840 - 1.26835) = 0.1 pips, which is excellent.

The fail scenario: the trader has been identified as "toxic flow" (consistently trading in the direction of short term momentum). Banks widen their streams. The same 8 banks now show best bid of 1.26810, a full 3 pips worse than the [[ECN]] mid. The trader is getting worse prices than a less sophisticated client would. This is the [[last look]] and flow segmentation dynamic that makes MDP pricing client-specific.

## Key mechanics and formulas
- **Competitive spread compression**: With N dealers competing, the client's effective spread narrows as N increases, typically following a power law. Going from 1 to 5 dealers captures most of the benefit.
- **Last look window**: Most MDP trades include a [[last look]] window of 50 to 200 milliseconds, during which the bank can reject the trade if the price has moved unfavorably.
- **Reject rate**: Reject rate = rejected trades / total attempted trades. A rising reject rate signals that banks are tightening their [[last look]] criteria against a client's flow.
- **Spread markup**: The price streamed to the client = interbank mid +/- (half spread + client-specific markup). The markup varies by client, pair, time of day, and trade size.
- **RFQ mode**: Some MDPs support [[Request for Quote]] mode where the client specifies size and direction, and banks respond with firm (or indicative) prices.

## Prerequisites
- [[Bid-Ask Spread]]
- [[ECN]]
- [[Liquidity]]
- [[Single Dealer Platform]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: the venue model where a client trades exclusively with one bank, which can offer tighter pricing for non-toxic flow.
- [[Last Look]]: the rejection mechanism that allows MDP liquidity providers to back away from streamed prices after the client clicks.
- [[Request for Quote]]: an alternative MDP workflow where the client asks for prices rather than clicking on streams.
- [[Central Limit Order Book]]: the ECN model that consolidates all liquidity into one anonymous book, unlike the bilateral MDP model.
- [[Transaction Cost Analysis]]: measuring whether MDP execution is actually competitive requires comparing fills against independent benchmarks.
- [[Internalization]]: banks that win MDP trades may internalize the flow rather than hedging on an [[ECN]].
- [[Dark Pool]]: some MDPs offer dark pool functionality where orders are matched at mid price without displaying quotes.

## Common misconceptions
1. **"The best price on the MDP is the true market price"**: MDP prices are client-specific. Two clients looking at the same MDP at the same millisecond will see different prices from the same bank. The true interbank price lives on [[EBS]] and [[Reuters Matching]].
2. **"More dealers always means better execution"**: Beyond about 8 to 10 dealers, adding more can actually worsen execution because banks detect that they are in a large panel and widen spreads defensively, knowing their probability of winning each trade is low.
3. **"MDP execution is firm"**: Most MDP liquidity providers retain [[last look]] rights. The price you click is not guaranteed. Rejection rates of 5% to 15% are common, and they increase during volatile periods precisely when execution matters most.

## Sources
- BIS Triennial Central Bank Survey, "FX Trading Venues and Platforms" (2022)
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
- Euromoney FX Survey, annual dealer rankings and platform market share data
- 360T, "Platform Connectivity and Execution Guide"
