---
aliases: [US Dollar Index, dollar index, USDX, dixie]
tags:
  - "#fx"
  - "#fx/g10"
date-added: "2026-03-27"
---

# DXY

## Definition

The DXY (US Dollar Index) is a weighted geometric mean of the US dollar's value against a basket of 6 major currencies. It was established in 1973 after the Bretton Woods system collapsed. The index is heavily weighted toward the euro (57.6%), making it largely a mirror of [[EUR USD]]. It is traded as a futures contract on ICE and is widely used as a shorthand for overall dollar strength or weakness.

## Why it matters (commodities and FX)

Most commodities are priced in USD, so DXY strength directly pressures commodity prices (and vice versa). When DXY rises, [[Brent Crude]], [[Gold]], and [[Copper Futures]] often fall as non USD buyers face higher effective costs. FX traders watch DXY to gauge broad dollar momentum before taking positions in individual pairs. A DXY breakout above resistance often signals sustained USD strength across multiple pairs.

## Concrete example

DXY is at 104.00. The Federal Reserve signals more rate hikes than expected. Over 2 weeks, DXY rallies to 106.50 (a 2.4% move).

**Impact on FX:** [[EUR USD]] drops from 1.0800 to 1.0540 (since EUR is 57.6% of the index, it absorbs most of the move). [[GBP USD]] falls from 1.2700 to 1.2480. [[USD JPY]] rises from 150.00 to 153.20.

**Impact on commodities:** [[Gold]] drops from $2,050 to $2,000 per [[Troy Ounce]]. [[Brent Crude]] slips from $82 to $79.

**Failure case:** A trader goes long gold expecting a breakout, ignoring that DXY is simultaneously breaking out to the upside. The dollar strength overwhelms the gold thesis, and gold drops $40. The trader loses $4,000 per contract.

## Key mechanics and formulas

**DXY basket weights:**

| Currency | Weight | Pair |
|----------|--------|------|
| EUR | 57.6% | [[EUR USD]] |
| JPY | 13.6% | [[USD JPY]] |
| GBP | 11.9% | [[GBP USD]] |
| CAD | 9.1% | [[USD CAD]] |
| SEK | 4.2% | USD/SEK |
| CHF | 3.6% | USD/CHF |

**Formula (geometric weighted mean):**

DXY = 50.14348112 * (EUR/USD)^(-0.576) * (USD/JPY)^(0.136) * (GBP/USD)^(-0.119) * (USD/CAD)^(0.091) * (USD/SEK)^(0.042) * (USD/CHF)^(0.036)

The constant 50.14348112 normalizes the index to 100.00 at inception (March 1973).

**Key levels:** 100 is the psychological round number. Above 100 means USD is stronger than the 1973 baseline on a weighted basis.

## Prerequisites

- [[EUR USD]]
- [[G10 Currencies]]
- [[Currency Pair]]

## Related concepts (learn next)

- [[EUR USD]] for the pair that dominates DXY movement (57.6% weight)
- [[Real Effective Exchange Rate]] for a trade weighted and inflation adjusted alternative to DXY
- [[Intervention]] for central bank actions that can cause sharp DXY moves
- [[Interest Rate Differential]] for the macro driver behind DXY trends
- [[Covered Interest Parity]] for how interest rate differences link to FX forward pricing
- [[Correlation]] for quantifying the DXY to commodities relationship

## Common misconceptions

1. **"DXY represents the dollar against all currencies."** It only includes 6 currencies, with EUR at 57.6%. It completely excludes CNY, AUD, NZD, MXN, and all EM currencies. It is a G10 centric, euro heavy measure.

2. **"DXY up means all dollar pairs are up."** Individual pairs can diverge. USD/JPY might fall on BOJ intervention while DXY rises because EUR/USD is falling harder. Always check the individual pair, not just the index.

3. **"DXY and commodity prices always move inversely."** The negative correlation is real but not 1:1. Supply shocks can push oil higher even as the dollar strengthens. The correlation breaks down during crisis periods.

## Sources

- ICE, "US Dollar Index (DXY) Contract Specifications"
- Federal Reserve, "Trade Weighted Dollar Index" (alternative to DXY)
- Bloomberg, "Dollar Index Analytics"
