---
aliases: [multi dealer platform, MDP, multi-dealer platform, multi-bank platform]
tags:
  - "#microstructure"
  - "#fx/structure"
date-added: "2026-03-27"
---

# Multi Dealer Platform

## Definition
A Multi Dealer Platform (MDP) is an electronic venue where clients view and compare prices streamed by multiple banks simultaneously and select the best one. Major FX MDPs: Bloomberg FXGO, 360T, FXall (Refinitiv), Currenex. MDPs differ from [[ECN]]s because prices are bilateral (each bank streams its own to the client) rather than consolidated into a single anonymous [[Central Limit Order Book]]. The advantage is competitive tension: banks know they are being compared, which tightens [[bid-ask spread]]s.

## Why it matters (commodities and FX)
MDPs are the primary execution venue for corporate and institutional FX hedging. A commodities firm converting USD oil revenues to EUR executes on an MDP to get competitive pricing from 5 to 15 banks at once. The MDP model extends to OTC commodity [[swap]]s and [[forward contract]]s on Bloomberg and ICE, where clients request prices from multiple dealers. MDP pricing is not the same as interbank pricing on [[EBS]] or [[Reuters Matching]]: banks apply [[skew]] and spread adjustments by client profitability, flow toxicity, and inventory. Ignore this and you misjudge execution quality.

## Concrete example

**Concrete:** A Swiss commodity trading house needs to sell 50M GBP/USD to hedge metals revenue. On 360T, 8 banks stream prices. Best bid 1.26835 from Bank A, second 1.26830 from Bank B, worst 1.26810 from Bank E. The trader clicks A and fills 50M at 1.26835. [[Reuters Matching]] mid at that moment is 1.26840: effective spread 0.1 pips, excellent. Adverse scenario: the same trader gets flagged as "toxic flow" (consistently trading with short term momentum). All 8 banks widen. Best bid drops to 1.26810, 3 pips worse than [[ECN]] mid. Less sophisticated clients get better prices. This is the [[last look]] and flow segmentation dynamic that makes MDP pricing client specific.

**Simplified:** Multiple banks compete for your order in real time. You see all their quotes, you pick the best. Banks know they are being shopped, so they tighten. The catch: each bank tailors the price to who you are. If they think you trade with information, you get a worse price than the corporate next to you.

## Key mechanics and formulas
- **Competitive spread compression:** with N dealers competing, effective spread narrows roughly as a power law. Going from 1 to 5 captures most of the benefit.
- **Last look window:** most MDP trades include a [[last look]] of 50 to 200 ms.
- **Reject rate:** rejected / attempted. A rising reject rate signals banks tightening last look against your flow.
- **Spread markup:** client price = interbank mid +/- (half spread + client specific markup). Markup varies by client, pair, time, size.
- **RFQ mode:** some MDPs support [[Request for Quote]] where the client specifies size and direction and banks respond firm or indicative.

## Prerequisites
- [[Bid-Ask Spread]]
- [[ECN]]
- [[Liquidity]]
- [[Single Dealer Platform]]

## Related concepts (learn next)
- [[Single Dealer Platform]]: trade exclusively with one bank; tighter pricing for non toxic flow
- [[Last Look]]: rejection mechanism letting LPs back away after the client clicks
- [[Request for Quote]]: alternative workflow asking for prices rather than clicking streams
- [[Central Limit Order Book]]: the ECN model consolidating all liquidity anonymously
- [[Transaction Cost Analysis]]: measuring MDP competitiveness needs independent benchmarks
- [[Internalization]]: winning banks may internalize the flow rather than hedge on an [[ECN]]
- [[Dark Pool]]: some MDPs offer mid match dark functionality

## Common misconceptions
1. **"Best price on the MDP is the true market price."** MDP prices are client specific. Two clients at the same millisecond see different prices from the same bank. True interbank lives on [[EBS]] and [[Reuters Matching]].
2. **"More dealers always means better execution."** Above 8 to 10 dealers, more can worsen execution: banks detect a large panel, lower win probability, and widen defensively.
3. **"MDP execution is firm."** Most MDP LPs retain [[last look]]. Rejection rates of 5 to 15% are normal and rise in volatile periods precisely when execution matters most.

## Sources
- BIS Triennial Central Bank Survey, "FX Trading Venues and Platforms" (2022)
- King, Osler, Rime, "Foreign Exchange Market Structure, Players, and Evolution," Norges Bank Working Paper (2012)
- Euromoney FX Survey, annual dealer rankings and platform market share data
- 360T, "Platform Connectivity and Execution Guide"
