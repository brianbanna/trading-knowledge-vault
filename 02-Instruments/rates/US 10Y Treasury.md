---
aliases: [US 10Y, 10 year treasury, UST 10Y, US10Y, 10Y yield, TNX, ZN]
tags:
  - "#rates/govies/ust"
date-added: "2026-07-03"
---

# US 10Y Treasury

## Definition

The US 10 year Treasury is the 10 year debt obligation of the US federal government, and its yield is the global benchmark risk free rate. In plain terms, it is the interest rate the market demands to lend to the United States for 10 years, and almost everything else in finance is priced off it. Precisely, the note pays a fixed semiannual coupon and returns par at maturity; the quoted yield is the internal rate of return that discounts those cash flows to the current market price. Yield 4.485% on 2026-07-02, up 2.58% on the day. It anchors mortgage rates, the discount rate on equities, the dollar, and [[Gold Futures|gold]]. Critically, yield and price move inversely: when the yield rises, the price of the bond falls, and when the yield falls, the price rises. The liquid futures expression is the CBOT 10 Year Note contract (ZN).

## Why it matters (commodities and FX)

The 10Y yield is the single most watched number in macro. It is the denominator of the discount rate for every future cash flow, so it drives equity valuations through [[S&P 500|the S&P 500]] and sets the opportunity cost baseline that competes with [[Gold Futures|gold]]. For an FX trader, the 10Y is one leg of every rate differential: the US 10Y minus the foreign 10Y helps explain the level of [[DXY]] and major pairs over medium horizons, while the front end (see [[US 2Y Treasury]]) dominates the short horizon. For a commodity trader, the 10Y matters through two channels. First, the real yield component (10Y nominal minus [[TIPS Breakeven|breakeven inflation]], see [[Real Interest Rates]]) sets the carry hurdle for holding non yielding assets. Second, the 10Y is a growth and inflation barometer; a sharp move usually reflects a repricing of [[Central Bank Policy]] or the growth outlook, both of which feed directly into industrial commodity demand. The relationship between the 10Y and the 2Y defines the [[Yield Curve Slope]], the market's cleanest recession signal.

## Concrete example

**Concrete:** Non Farm Payrolls Friday, 14:30 CET. The 10Y yield is 4.60% going in. A desk is long ZN (10Y note futures) expecting a soft print. Payrolls miss badly, 60k versus 180k expected, and the unemployment rate ticks up. The market prices faster [[Central Bank Policy|Fed]] cuts, so yields fall. The 10Y yield drops from 4.60% to 4.485% in an hour. Because yield and price move inversely, the ZN price rises. The 10Y note has a duration near 8, so a roughly 11.5 bp fall in yield lifts the price about 0.92% (8 × 0.115%). On 100 ZN contracts (roughly $10M notional at ~$110k per contract face-adjusted), that is a gain of roughly $92,000. The win case: the trader was long duration into a dovish surprise. The fail case: had payrolls printed hot at 300k, the 10Y would have jumped to 4.75%, the ZN price would have fallen about 1.2%, and the same 100 lot position would have lost roughly $120,000. Duration cuts both ways.

**Simplified:** The 10Y Treasury yield is the interest rate the US government pays to borrow for 10 years, and it is the reference rate for the whole financial system. When investors expect slower growth or rate cuts, they buy bonds, the price goes up, and the yield goes down. When they expect strong growth or inflation, they sell bonds, the price goes down, and the yield goes up. Remember the inverse: yield up means price down. You trade the price through the ZN futures contract, and a small move in yield is a large move in dollars because the note has high duration.

## Contract specifications

| Field | Value |
|-------|-------|
| Instrument | US 10 Year Treasury Note |
| Cash market | OTC, primary dealers, on the run and off the run |
| Futures exchange | CBOT (CME Group) |
| Futures contract | 10 Year Note (ZN) |
| Contract size | $100,000 face value |
| Deliverable basket | Notes with 6.5 to 10 years remaining maturity |
| Tick size | 1/64 of a point (half of 1/32) |
| Tick value | $15.625 |
| Price convention | Points and 32nds of par (e.g. 110'16.5) |
| Trading hours | Nearly 24h Sun to Fri (CME Globex) |
| Settlement | Physical delivery of eligible notes |
| Quote for yield | TNX (CBOE 10Y yield index, ×10) |

## Fundamentals

### Drivers of higher 10Y yields (price lower)
- Hawkish [[Central Bank Policy]] repricing (fewer cuts, or hikes)
- Upside growth surprises (strong payrolls, PMIs, retail sales)
- Rising inflation expectations lifting [[TIPS Breakeven|breakeven]]
- Heavy Treasury supply (large auctions, wider deficits, term premium)
- Foreign selling or reserve diversification away from USD assets

### Drivers of lower 10Y yields (price higher)
- Dovish policy repricing (faster cuts on soft data)
- Growth scares, recession fear, credit stress
- Safe haven flight to quality in [[Risk-On Risk-Off|risk off]] episodes
- Falling inflation expectations
- Central bank balance sheet expansion (QE)

### Term premium and real yield decomposition
The 10Y yield decomposes into expected average short rates over 10 years plus a term premium (compensation for duration risk), and separately into a real yield plus a breakeven inflation component. Watching which component moves tells you whether a yield change is about growth, inflation, or supply and risk appetite.

## Key data and reports

- FOMC decisions, dot plot, and minutes (drives the expected path)
- US Non Farm Payrolls (monthly, first Friday, highest impact)
- US CPI and PCE inflation prints
- Treasury quarterly refunding announcements and auction results
- ISM manufacturing and services PMIs
- Fed balance sheet data (QE/QT pace)
- CFTC positioning in Treasury futures

## Key spreads and relative value

- **[[Yield Curve Slope|2s10s]] (10Y yield minus [[US 2Y Treasury|2Y yield]]):** the flagship curve trade and recession signal.
- **10Y real yield (10Y minus [[TIPS Breakeven|breakeven]]):** the [[Real Interest Rates|real rate]] that competes with [[Gold Futures|gold]].
- **US 10Y minus German 10Y (Bund):** a driver of [[EUR/USD]] and [[DXY]] over medium horizons.
- **10Y swap spread (Treasury yield minus matched swap rate):** balance sheet and funding stress gauge.
- **5s30s and 2s5s10s butterfly:** shape trades expressing views on the belly versus wings.

## Important relationships

- Inverse price to yield: the defining mechanic of the instrument
- Inverse to [[Gold Futures|gold]] through the [[Real Interest Rates|real yield]] channel
- Positive yield correlation with growth surprises and [[S&P 500|equity]] cyclicality in normal regimes, but flight to quality flips the sign in stress
- One leg of the [[Yield Curve Slope]] with the [[US 2Y Treasury]]
- A component of USD rate differentials that influence [[DXY]] and [[EUR/USD]]
- Sets the discount rate anchoring [[S&P 500|equity]] valuations

## Trading notes

*Add personal observations here.*

## Related instruments

- [[US 2Y Treasury]]
- [[Gold Futures]]
- [[S&P 500]]
- [[DXY]]

## Related concepts

- [[Real Interest Rates]]
- [[TIPS Breakeven]]
- [[Central Bank Policy]]
- [[Yield Curve Slope]]
