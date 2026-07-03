---
aliases: [US 2Y, 2 year treasury, UST 2Y, US2Y, 2Y yield, ZT]
tags:
  - "#rates/govies/ust"
date-added: "2026-07-03"
---

# US 2Y Treasury

## Definition

The US 2 year Treasury is the 2 year debt obligation of the US federal government, and its yield is the most [[Central Bank Policy|Fed]] policy sensitive point on the curve. In plain terms, it is the interest rate the market demands to lend to the United States for 2 years, and it tracks where investors think the policy rate will average over the next two years. Precisely, the note pays a fixed semiannual coupon and returns par at maturity; the quoted yield is the internal rate of return discounting those cash flows to the market price. Yield 4.170% on 2026-07-01. Because it sits at the front end, the 2Y is the cleanest market proxy for the expected policy rate path over the near term. As with all bonds, yield and price move inversely: a rising yield means a falling price. The liquid futures expression is the CBOT 2 Year Note contract (ZT).

## Why it matters (commodities and FX)

The 2Y is the market's vote on [[Central Bank Policy]]. It moves almost one for one with shifts in the expected number of hikes or cuts over the next two years, which makes it the fastest reacting Treasury to labor data, inflation prints, and Fed speak. For an FX trader, the front end rate differential (US 2Y minus the foreign 2Y) is the strongest short horizon driver of major pairs; the US 2Y minus German 2Y spread is one of the best explanations of [[EUR/USD]] moves around central bank meetings, and it feeds directly into [[DXY]]. For a commodity trader, the 2Y matters because it prices the near term policy stance that governs dollar strength, funding costs, and the growth trajectory. The 2Y is also the short leg of the [[Yield Curve Slope]]: when the front end reprices faster than the long end, the curve steepens or flattens, and that shape is a leading signal on the business cycle. Its short duration means yield moves translate into much smaller price moves than the [[US 10Y Treasury]], so the 2Y is where you express a pure policy view with limited duration risk.

## Concrete example

**Concrete:** CPI Tuesday, 14:30 CET. The 2Y yield is 4.30% going in. Core CPI surprises hot, 0.5% month on month versus 0.3% expected. The market removes two [[Central Bank Policy|Fed]] cuts from the next 12 months of pricing. The 2Y yield jumps from 4.30% to 4.42% almost immediately, far more than the [[US 10Y Treasury|10Y]], because the front end is where policy expectations live. A desk short ZT (2Y note futures) into the print profits: the 2Y note has a duration near 1.9, so a 12 bp yield rise cuts the price about 0.23% (1.9 × 0.12%), and because yield up means price down, the short gains. On 200 ZT contracts (roughly $40M notional at $200k face each), that is a gain of roughly $92,000. The win case: short the front end into a hot inflation print. The fail case: had CPI come in soft at 0.1%, the market would have added cuts, the 2Y would have fallen to 4.18%, the ZT price would have risen about 0.23%, and the same short would have lost roughly $92,000.

**Simplified:** The 2Y Treasury yield is the interest rate the US government pays to borrow for 2 years, and it closely tracks where the market thinks the Fed's policy rate is heading. When traders expect the Fed to cut, they buy the 2Y, its price rises and its yield falls. When they expect the Fed to stay high or hike, the yield rises. It reacts faster and harder to Fed related news than any other Treasury. It has low duration, so a given yield move is a smaller dollar move than a longer bond, which makes it the tool for betting on rate policy without much interest rate risk. You trade it through the ZT futures contract.

## Contract specifications

| Field | Value |
|-------|-------|
| Instrument | US 2 Year Treasury Note |
| Cash market | OTC, primary dealers, on the run and off the run |
| Futures exchange | CBOT (CME Group) |
| Futures contract | 2 Year Note (ZT) |
| Contract size | $200,000 face value |
| Deliverable basket | Notes with 1.75 to 2 years remaining maturity |
| Tick size | 1/128 of a point (quarter of 1/32) |
| Tick value | $15.625 |
| Price convention | Points and 32nds of par |
| Trading hours | Nearly 24h Sun to Fri (CME Globex) |
| Settlement | Physical delivery of eligible notes |

## Fundamentals

### Drivers of higher 2Y yields (price lower)
- Hawkish [[Central Bank Policy]] repricing (fewer cuts, hikes back on the table)
- Hot inflation prints (CPI, PCE) lifting the expected policy path
- Strong labor data reducing cut expectations
- Hawkish Fed speak and a higher dot plot

### Drivers of lower 2Y yields (price higher)
- Dovish repricing (faster or deeper cuts)
- Soft labor data (weak payrolls, rising unemployment)
- Cooling inflation
- [[Risk-On Risk-Off|Risk off]] flight to quality and growth scares

### Why the front end leads
The 2Y is dominated by the expected average policy rate over two years, with a small term premium. That makes it a near pure read on [[Central Bank Policy]] expectations, and it is why the 2Y reprices first and fastest when the policy outlook shifts.

## Key data and reports

- FOMC decisions, dot plot, minutes, and Fed speaker calendar
- US CPI and PCE inflation prints (highest sensitivity)
- US Non Farm Payrolls and JOLTS
- Fed funds futures and SOFR futures implied path
- 2 Year Note auction results
- CFTC positioning in short end Treasury futures

## Key spreads and relative value

- **[[Yield Curve Slope|2s10s]] ([[US 10Y Treasury|10Y yield]] minus 2Y yield):** the front leg of the flagship curve trade.
- **US 2Y minus German 2Y (Schatz):** the strongest short horizon driver of [[EUR/USD]] and a key input to [[DXY]].
- **2Y yield minus Fed funds rate:** measures how much easing or tightening the market has priced relative to the current policy rate.
- **2s5s:** front to belly shape trade on the pace of the cutting or hiking cycle.

## Important relationships

- Inverse price to yield, with low duration so smaller dollar moves than the [[US 10Y Treasury]]
- Highest sensitivity of any Treasury to [[Central Bank Policy]] expectations
- Short leg of the [[Yield Curve Slope]] with the 10Y
- Front end rate differentials drive [[EUR/USD]] and [[DXY]] over short horizons
- Influenced by the same [[Real Interest Rates|real rate]] and inflation forces that move the whole curve, but the policy expectations component dominates

## Trading notes

*Add personal observations here.*

## Related instruments

- [[US 10Y Treasury]]
- [[EUR/USD]]
- [[DXY]]

## Related concepts

- [[Central Bank Policy]]
- [[Yield Curve Slope]]
- [[Real Interest Rates]]
