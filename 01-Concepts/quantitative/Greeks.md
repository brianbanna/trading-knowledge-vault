---
aliases: [Greeks, option Greeks, option sensitivities, Greek letters]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-24"
---

# Greeks

## Definition

The Greeks are a family of risk sensitivities that measure how an option's price changes in response to changes in underlying variables: spot price, volatility, time, and interest rates. They are called "Greeks" because most are named after Greek letters. Think of them as the dashboard gauges on a car: each one tells you a different dimension of how your position behaves. Delta tells you direction, gamma tells you acceleration, vega tells you volatility sensitivity, theta tells you the daily cost of holding, and the higher order Greeks tell you how these gauges themselves shift as conditions change.

First order Greeks measure direct sensitivities. Second order Greeks measure how first order Greeks change, capturing the curvature and cross effects that dominate risk in volatile markets. Understanding the hierarchy, from first order through second order and beyond, is what separates basic option awareness from real options trading competence.

## Why it matters (commodities and FX)

Options are central to commodity and FX risk management. Producers hedge with puts, consumers hedge with calls, dealers make markets in vol, and macro traders express views through options structures. Every one of these participants is exposed to Greek risks whether they manage them explicitly or not.

In FX, the entire vol surface is organized by [[Delta]] (10D, 25D, ATM), and the standard market quotes ([[Risk Reversal]], [[Butterfly]]) are directly defined in terms of Greeks. Market makers manage their books greek by greek: flatten delta continuously, monitor gamma exposure near expiries, hedge vega against the surface, and watch vanna/volga for smile risk.

In commodities, short dated options near delivery (e.g., on [[WTI Crude Oil]] or [[Henry Hub Natural Gas]]) create extreme gamma exposures. Seasonal vol patterns mean vega risk varies through the year. Commodity option books with barrier or Asian features have exotic Greek profiles that require careful monitoring.

## Concrete example

A crude oil options desk has the following book Greeks (aggregated across all positions):

| Greek | Value | Meaning |
|-------|-------|---------|
| Delta | +500 lots | Net long 500,000 barrels of directional exposure |
| Gamma | +80 lots/dollar | Each $1 move in crude adds 80 lots of delta |
| Vega | -$200,000 | Each 1 vol point increase loses $200,000 |
| Theta | +$45,000 | Earning $45,000/day from time decay |
| Vanna | +$30,000 | If vol rises 1 point, delta increases by 30 lots |

**Reading the dashboard:** This desk is long direction (delta), long convexity near current spot (gamma), short volatility (collecting premium via negative vega, earning positive theta), and has a vanna exposure that will increase their directional risk if vol rises. The key risk: a sharp move in crude combined with a vol spike would hurt through the vega channel while the gamma gains may not fully offset.

## Key mechanics and formulas

### First Order Greeks

These measure direct sensitivity to a single variable.

| Greek | Measures | Formula (Black-Scholes) | Units |
|-------|----------|------------------------|-------|
| [[Delta]] | dOption/dSpot | N(d1) for calls | Change in option price per $1 spot move |
| [[Vega]] | dOption/dVol | S x N'(d1) x sqrt(T) | Change in option price per 1% vol change |
| [[Theta]] | dOption/dTime | Complex (negative for long options) | Daily time decay in dollars |
| Rho | dOption/dRate | K x T x e^(-rT) x N(d2) for calls | Change per 1% rate change |

### Second Order Greeks

These measure how first order Greeks change, capturing curvature and cross effects.

| Greek | Measures | What It Tells You |
|-------|----------|-------------------|
| [[Gamma]] | dDelta/dSpot | How fast your directional exposure shifts as spot moves. The source of [[Convexity]]. |
| [[Vanna]] | dDelta/dVol (= dVega/dSpot) | How your directional exposure changes when vol moves, OR how your vol exposure changes when spot moves. Critical for [[Risk Reversal]] positions. |
| [[Volga]] | dVega/dVol | How your vol exposure changes when vol itself moves. Dominates pricing of OTM options and [[Butterfly]] positions. |
| Charm | dDelta/dTime | How delta drifts as time passes (delta bleed). Critical near expiry. |

### Third Order Greeks (rarely traded directly)

| Greek | Measures | When It Matters |
|-------|----------|-----------------|
| Speed | dGamma/dSpot | Extreme gamma positions near barriers |
| Color | dGamma/dTime | Gamma exposure evolution into expiry |
| Ultima | dVolga/dVol | Deeply OTM option pricing in stressed markets |

### The Greek Hierarchy

```
Spot Sensitivity          Vol Sensitivity          Time Sensitivity
      |                         |                        |
    Delta                     Vega                     Theta
      |                         |
    Gamma                     Volga
      |
    Speed

Cross Sensitivities:
    Vanna = dDelta/dVol = dVega/dSpot  (links spot and vol)
    Charm = dDelta/dTime               (links spot and time)
    Color = dGamma/dTime               (links convexity and time)
```

### Greek Relationships

- **Gamma-Theta tradeoff:** For a delta hedged position, theta = 0.5 x gamma x spot^2 x vol^2 / 252. Long gamma always costs theta. Short gamma always earns theta.
- **Vanna-Volga method:** A pricing approach for OTM options that adjusts Black-Scholes prices using vanna and volga exposures to capture the [[Volatility Smile]]. Standard in FX options.
- **Put-call parity for Greeks:** Call delta - put delta = 1 (same strike/expiry). Call gamma = put gamma. Call vega = put vega.

## Prerequisites

- [[Vanilla Option]]
- [[Implied Volatility]]
- [[Hedging]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Delta]] as the most fundamental Greek, the starting point for all option risk management.
- [[Gamma]] because gamma drives convexity and determines how violently delta shifts during large moves.
- [[Vega]] because vol exposure is often the dominant risk in an options portfolio, larger than directional risk.
- [[Theta]] because the gamma/theta tradeoff is the central tension in options trading.
- [[Vanna]] because it links spot and vol risk, dominating the behavior of risk reversals and skewed positions.
- [[Volga]] because it drives OTM option pricing and the cost of tail protection.
- [[Vol Surface]] because the surface is the organizing framework for all Greeks across strikes and tenors.
- [[Convexity]] because Greeks quantify the non-linearity that makes options fundamentally different from linear instruments.

## Common misconceptions

**"Managing delta is enough."** Delta is necessary but far from sufficient. A delta neutral book can still lose millions from gamma (sudden spot move), vega (vol shift), or theta (time decay). Professional desks manage all major Greeks simultaneously.

**"Greeks are constant."** Every Greek changes with spot, vol, time, and rates. Delta changes with spot (gamma). Vega changes with vol (volga). Gamma changes with time (color). This "Greeks of Greeks" dynamic is what makes option risk management a continuous, active process rather than a set and forget exercise.

**"Second order Greeks only matter for exotic options."** Vanna and volga matter for ANY OTM option. The Black-Scholes model prices ATM options reasonably but misprices OTM options because it ignores the smile. The vanna-volga adjustment corrects this. If you trade risk reversals, strangles, or any OTM structure, second order Greeks are first order concerns.

**"You can hedge all Greeks simultaneously."** In practice, hedging one Greek often increases exposure to another. Buying options to reduce gamma risk increases vega and theta exposure. The art of options portfolio management is choosing which Greeks to hedge and which to accept as residual risk.

## Sources

- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options* (1997).
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed. (2014).
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed. (2017).
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
