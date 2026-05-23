---
aliases: [US Dollar Index, dollar index, USDX, dixie]
tags:
  - "#fx"
  - "#fx/g10"
date-added: "2026-03-27"
---

# DXY

## Definition

The DXY (US Dollar Index) is a weighted geometric mean of the US dollar against 6 major currencies. Established in 1973 after the Bretton Woods collapse. The index is heavily weighted toward EUR (57.6%), making it largely a mirror of [[EUR USD]]. Traded as a futures contract on ICE and used as a shorthand for overall dollar strength or weakness.

## Why it matters (commodities and FX)

Most commodities are priced in USD, so DXY strength directly pressures commodity prices. When DXY rises, [[Brent Crude]], [[Gold]], and [[Copper Futures]] fall as non USD buyers face higher effective costs. FX traders watch DXY to gauge broad dollar momentum before positioning in individual pairs. A DXY breakout above resistance often signals sustained USD strength across pairs.

## Concrete example

**Concrete:** DXY at 104.00. The Fed signals more rate hikes than expected. Over 2 weeks DXY rallies to 106.50 (a 2.4% move). FX impact: [[EUR USD]] drops 1.0800 to 1.0540 (EUR absorbs most of the move at 57.6% weight). [[GBP USD]] falls 1.2700 to 1.2480. [[USD JPY]] rises 150.00 to 153.20. Commodities: [[Gold]] drops $2,050 to $2,000 per [[Troy Ounce]]. [[Brent Crude]] slips $82 to $79. A trader who went long gold expecting a breakout while ignoring the simultaneous DXY breakout sees the dollar overwhelm the gold thesis: gold drops $40, $4,000 loss per contract.

**Simplified:** DXY measures USD against a basket of major currencies, mostly EUR. When DXY rises, USD is strengthening. Commodities priced in USD get cheaper in dollar terms when DXY rises. Always check DXY before any commodity or FX trade.

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

- [[EUR USD]]: the pair that dominates DXY (57.6% weight)
- [[Real Effective Exchange Rate]]: trade weighted and inflation adjusted alternative to DXY
- [[Intervention]]: central bank actions that cause sharp DXY moves
- [[Interest Rate Differential]]: macro driver behind DXY trends
- [[Covered Interest Parity]]: how rate differences link to FX forward pricing
- [[Correlation]]: quantifying the DXY to commodities relationship

## Common misconceptions

**"DXY represents the dollar against all currencies."** It includes only 6 currencies, with EUR at 57.6%. It excludes CNY, AUD, NZD, MXN, and all EM. A G10 centric, euro heavy measure.

**"DXY up means all dollar pairs are up."** Pairs can diverge. USD/JPY can fall on BOJ intervention while DXY rises because EUR/USD is falling harder. Always check the individual pair.

**"DXY and commodity prices always move inversely."** The negative correlation is real but not 1:1. Supply shocks push oil higher even as the dollar strengthens. Correlation breaks down during crisis.

## Sources

- ICE, "US Dollar Index (DXY) Contract Specifications"
- Federal Reserve, "Trade Weighted Dollar Index" (alternative to DXY)
- Bloomberg, "Dollar Index Analytics"
