---
aliases: [London gold fix, LBMA Gold Price, gold fix, AM fix, PM fix]
tags:
  - "#metals/precious/gold"
date-added: "2026-03-20"
---

# London Fix

## Definition

The London Fix (officially the LBMA Gold Price since 2015) is the benchmark gold price determined twice daily through an electronic auction process administered by ICE Benchmark Administration. The AM fix occurs at 10:30 AM London time and the PM fix at 3:00 PM London time. During the auction, participants submit buy and sell orders at a proposed price. The price is adjusted iteratively until supply and demand balance within a tolerance band. The resulting fix price is used globally as the reference rate for settling gold derivatives, valuing ETF holdings, pricing mine production contracts, and benchmarking central bank reserves. The silver fix (LBMA Silver Price) occurs once daily at noon London time.

## Why it matters (commodities and FX)

The London Fix is the price that matters for physical gold settlement. Billions of dollars in contracts reference the PM fix specifically. Gold ETFs (GLD, IAU) value their holdings at the PM fix. Central banks mark their reserves to the fix. Mine producers sell their output based on fix related formulas. Because so much economic value settles at the fix, there are concentrated order flows around the auction times, creating predictable short term trading patterns. Academic research has documented systematic price patterns around the fix (the "fixing anomaly"), and the transition from the old telephone based fix to the electronic auction in 2015 was driven partly by manipulation concerns.

## Concrete example

A gold ETF needs to redeem 50,000 ounces and settles at the PM fix. The ETF's authorized participant (a bank) must sell physical gold at the fix price. If the bank anticipates this selling pressure, it may pre hedge by selling futures before the fix, creating downward pressure. A trader who monitors ETF flow data sees the large pending redemption and goes short gold ahead of the 3 PM fix. If the fix settles $3/oz below the pre fix price due to the concentrated selling, she covers and profits. If unexpected buying overwhelms the ETF selling, the fix could settle higher and the short loses.

## Key mechanics and formulas

**Auction schedule:**
- AM Fix: 10:30 AM London time
- PM Fix: 3:00 PM London time

**Auction process:**
1. ICE proposes an opening price
2. Participants submit buy/sell orders
3. If imbalance exceeds tolerance (10,000 oz), price adjusts
4. Process repeats until balance is achieved
5. Final price published as LBMA Gold Price

**Key references:**
- Gold ETFs (GLD, IAU): value NAV at PM fix
- Central bank reserves: marked at fix prices
- Mine hedging contracts: often reference monthly average of daily fixes

## Prerequisites

- [[Gold Futures]]
- [[LBMA]]
- [[Troy Ounce]]

## Related concepts (learn next)

- [[LBMA]] because the London Fix is administered under the LBMA framework.
- [[COMEX]] because the fix interacts with COMEX futures pricing through EFP trading.
- [[ETF Flows]] because ETF creation/redemption settles at the fix.
- [[Central Bank Buying]] because central bank gold transactions reference the fix.
- [[FX Fix]] because the FX WMR fix shares similar benchmark dynamics and trading patterns.

## Common misconceptions

**"The fix is just the spot price at that time."** The fix is a separate auction process that can result in a price different from the prevailing spot market. The auction concentrates liquidity and produces a single settlement price.

**"The fix cannot be influenced."** While the 2015 reform improved transparency, concentrated order flow around the fix inherently creates price impact. Large participants can influence the auction outcome.

**"Only the PM fix matters."** The AM fix is used for certain contracts and provides a reference for Asian/European trading. Both fixes are important benchmarks.

## Sources

- ICE Benchmark Administration: LBMA Gold Price Methodology
- LBMA: Price Benchmark Information
- World Gold Council: Gold Pricing and Benchmarks
