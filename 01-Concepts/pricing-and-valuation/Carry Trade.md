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

A carry trade involves borrowing in a low interest rate currency and investing the proceeds in a higher interest rate currency, profiting from the interest rate differential (the "carry"). The trader earns the spread between the 2 rates as long as the exchange rate does not move against the position by more than the carry earned. It is the most fundamental strategy in FX markets and one of the oldest forms of [[Relative Value Trade]].

## Why it matters (commodities and FX)

Carry is the dominant force in FX pricing over medium term horizons. Central bank rate differentials drive massive capital flows between currencies. For a commodity trader, carry matters because commodity currencies (AUD, CAD, BRL, ZAR, NOK, CLP) tend to be high yielding, and their exchange rates are driven partly by carry dynamics, partly by commodity prices. Understanding carry helps you decompose whether AUD/USD is moving because of rate expectations or because of [[Copper Futures|copper]] and [[Iron Ore Futures|iron ore]] prices.

Carry also applies directly to commodity futures through the [[Cost of Carry Model]]: a commodity in [[Contango]] has negative carry (costs money to hold), while a commodity in [[Backwardation]] has positive carry (earns money to hold via [[Roll Yield]]).

## Concrete example

Japanese interest rates are 0.25%. Australian interest rates are 4.35%. A trader borrows JPY and buys AUD (goes long AUD/JPY). The annualized carry is approximately 4.10% (4.35% minus 0.25%). If AUD/JPY stays flat for 1 year, the trader earns ~4.10% on the notional. However, if AUD/JPY drops by more than 4.10%, the carry is wiped out and the position loses money.

In practice, carry is collected daily through the FX swap/forward market. The forward points on AUD/JPY will be negative (AUD trades at a forward discount to JPY), meaning rolling a long AUD/JPY position forward earns the carry incrementally.

## Key mechanics and formulas

**Carry return (annualized):**
`Carry = r_invest - r_fund`

Where r_invest is the interest rate on the currency you buy, r_fund is the rate on the currency you borrow.

**Total return of carry trade:**
`Total Return = Carry + Spot Return`
`= (r_invest - r_fund) + (S_end - S_start) / S_start`

**Forward premium/discount (covered interest rate parity):**
`F/S = (1 + r_domestic) / (1 + r_foreign)`

If the foreign rate is higher, the forward trades at a discount, and the carry trade earns the difference between forward and spot when rolled.

**Sharpe ratio of carry:** historically, FX carry strategies have delivered Sharpe ratios of 0.5 to 0.8 over long periods, but with severe left tail risk (carry crashes).

## Prerequisites

- [[Forward Curve]]
- [[Real Interest Rates]]
- [[Central Bank Policy]]
- [[FX Forward Points]]

## Related concepts (learn next)

- [[Uncovered Interest Rate Parity]] - the theoretical framework that says carry should not work because exchange rates should adjust to offset rate differentials. In practice, UIP is violated (the "forward premium puzzle"), which is WHY carry works.
- [[FX Forward Points]] - the mechanical expression of carry in the forward market. You need to understand how forward points are calculated and quoted.
- [[Volatility Risk Premium]] - carry strategies have option like payoff profiles. Understanding vol risk premium helps you size carry trades correctly.
- [[FX Options]] - hedging carry positions with put options converts the trade from unlimited downside to defined risk.
- [[Risk Parity]] - carry is one of the "risk premia" harvested in multi asset risk parity frameworks.
- [[Dollar Smile]] - the USD tends to strengthen in both extreme risk off AND extreme US outperformance. This nonlinear behavior is critical for managing carry positions funded in USD.
- [[Roll Yield]] - the commodity analogue of FX carry. Understanding both shows how carry is a universal concept across asset classes.

## Common misconceptions

**"Carry trades are free money."** They have significant left tail risk. Carry positions get unwound violently during crises (2008 JPY carry unwind, 2020 COVID, 2022 JPY intervention). The carry compensates for this crash risk.

**"Higher carry means better trade."** The highest carry currencies (TRY, BRL, ZAR) often depreciate enough to offset the carry. Risk adjusted carry (carry per unit of volatility) is the correct metric, not raw carry.

**"Carry only works in FX."** Carry is a universal concept. Bond carry (riding the yield curve), commodity carry ([[Roll Yield]]), volatility carry (selling options), and dividend carry (long high dividend stocks) all exploit the same principle.

**"Carry trades are always short JPY."** JPY is the traditional funding currency because of Japan's low rates, but EUR, CHF, and CNH have all been funding currencies at various points depending on relative rate levels.

## Sources

- BIS Triennial Central Bank Survey (FX market structure)
- Burnside, Eichenbaum, Kleshchelski, Rebelo, "Do Peso Problems Explain the Returns to the Carry Trade?" (2011)
- Lustig, Roussanov, Verdelhan, "Common Risk Factors in Currency Markets" (2011)
- CME Group: FX Carry Trade Strategies
