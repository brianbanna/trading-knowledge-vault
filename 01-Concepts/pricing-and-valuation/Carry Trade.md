---
aliases: [carry trade, FX carry, interest rate carry]
tags:
  - "#fx/g10"
  - "#fx/em"
  - "#rates/swaps"
date-added: "2026-03-20"
---

# Carry Trade

## Definition

A carry trade borrows in a low rate currency and invests in a higher rate currency, earning the rate differential (the "carry"). The trader pockets the spread as long as the exchange rate does not move against the position by more than the carry. The most fundamental strategy in FX and one of the oldest forms of [[Relative Value Trade]].

## Why it matters (commodities and FX)

Carry dominates FX pricing over medium term horizons. Central bank rate differentials drive massive capital flows. Commodity currencies (AUD, CAD, BRL, ZAR, NOK, CLP) are high yielding, with exchange rates driven partly by carry dynamics and partly by commodity prices. Decomposing AUDUSD moves into rate expectations vs [[Copper Futures|copper]] and [[Iron Ore Futures|iron ore]] requires understanding carry.

Carry also applies directly to commodity futures via the [[Cost of Carry Model]]: [[Contango]] means negative carry (costs money to hold); [[Backwardation]] means positive carry (earns money via [[Roll Yield]]).

## Concrete example

**Concrete:** JPY rate 0.25%, AUD rate 4.35%. Trader borrows JPY, buys AUD (long AUDJPY). Annualized carry ≈ 4.10%. If AUDJPY stays flat for 1 year, the trader earns ~4.10% on notional. If AUDJPY drops more than 4.10%, carry is wiped out. Carry is collected daily through the FX swap/forward market: forward points on AUDJPY are negative (AUD at forward discount to JPY), so rolling long AUDJPY forward earns carry incrementally.

**Simplified:** Borrow cheap, lend expensive. In FX, that means borrowing yen at near zero and parking the money in Australian dollars at 4%. You earn the gap each day. The risk: if AUDJPY falls more than the carry pays, you lose. The strategy works on average but collapses when risk aversion spikes and everyone unwinds at once, dragging the high yielder down sharply against the funder.

## Key mechanics and formulas

**Carry return (annualized):**
`Carry = r_invest − r_fund`

Where r_invest is the rate on the currency bought, r_fund the rate on the currency borrowed.

**Total return:**
`Total Return = Carry + Spot Return = (r_invest − r_fund) + (S_end − S_start) / S_start`

**Forward premium/discount (covered interest rate parity):**
`F/S = (1 + r_domestic) / (1 + r_foreign)`

When the foreign rate is higher, the forward trades at a discount; the carry trade earns this differential on each roll.

**Sharpe ratio of carry:** historically 0.5 to 0.8 over long samples, with severe left tail risk (carry crashes).

## Prerequisites

- [[Forward Curve]]
- [[Real Interest Rates]]
- [[Central Bank Policy]]
- [[FX Forward Points]]

## Related concepts (learn next)

- [[Uncovered Interest Rate Parity]] — the theory says carry should not work because spot should adjust. UIP fails empirically (the "forward premium puzzle"), which is WHY carry works.
- [[FX Forward Points]] — the mechanical expression of carry in the forward market.
- [[Volatility Risk Premium]] — carry has option like payoff profiles; vol risk premium drives correct sizing.
- [[FX Options]] — hedging carry with put options converts unlimited downside to defined risk.
- [[Risk Parity]] — carry is one of the risk premia harvested in multi asset frameworks.
- [[Dollar Smile]] — USD strengthens in both extreme risk off and extreme US outperformance. Nonlinear behavior matters for USD funded carry.
- [[Roll Yield]] — the commodity analogue of FX carry.

## Common misconceptions

**"Carry trades are free money."** Significant left tail risk. Carry unwinds violently in crises (2008 JPY unwind, 2020 COVID, 2022 JPY intervention). Carry compensates for crash risk.

**"Higher carry means better trade."** Highest carry currencies (TRY, BRL, ZAR) depreciate enough to offset carry. Risk adjusted carry (carry per unit vol) is the correct metric.

**"Carry only works in FX."** Bond carry (yield curve), commodity carry ([[Roll Yield]]), volatility carry (short options), dividend carry (high dividend equities) all exploit the same principle.

**"Carry trades are always short JPY."** JPY is the traditional funder, but EUR, CHF, and CNH have served depending on relative rate levels.

## Sources

- BIS Triennial Central Bank Survey (FX market structure)
- Burnside, Eichenbaum, Kleshchelski, Rebelo, "Do Peso Problems Explain the Returns to the Carry Trade?" (2011)
- Lustig, Roussanov, Verdelhan, "Common Risk Factors in Currency Markets" (2011)
- CME Group: FX Carry Trade Strategies
