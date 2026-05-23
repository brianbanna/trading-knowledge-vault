---
aliases: [Greeks, option Greeks, option sensitivities, Greek letters]
tags:
  - "#quant"
  - "#risk"
date-added: "2026-03-24"
---

# Greeks

## Definition

The Greeks are risk sensitivities that measure how an option's price responds to changes in spot, volatility, time, and interest rates. Most are named after Greek letters. Think of them as dashboard gauges: delta is direction, gamma is acceleration, vega is volatility sensitivity, theta is the daily holding cost. Higher order Greeks measure how the gauges themselves shift as conditions change.

First order Greeks measure direct sensitivities. Second order Greeks measure how first order Greeks change, capturing curvature and cross effects that dominate risk in volatile markets. The hierarchy from first through second order separates basic option awareness from real options competence.

## Why it matters (commodities and FX)

Options are central to commodity and FX risk management. Producers hedge with puts, consumers hedge with calls, dealers make markets in vol, macro traders express views through option structures. Every participant is exposed to Greek risks whether they manage them or not.

In FX, the entire vol surface is organized by [[Delta]] (10D, 25D, ATM), and the standard market quotes ([[Risk Reversal]], [[Butterfly]]) are defined in terms of Greeks. Market makers manage greek by greek: flatten delta continuously, monitor gamma near expiries, hedge vega against the surface, watch vanna/volga for smile risk.

In commodities, short dated options near delivery (e.g., [[WTI Crude Oil]], [[Henry Hub Natural Gas]]) create extreme gamma exposures. Seasonal vol patterns mean vega risk varies through the year. Commodity option books with barrier or Asian features have exotic Greek profiles requiring careful monitoring.

## Concrete example

**Concrete:** Crude oil options desk book Greeks:

| Greek | Value | Meaning |
|-------|-------|---------|
| Delta | +500 lots | Net long 500,000 barrels directional |
| Gamma | +80 lots/dollar | Each $1 move adds 80 lots of delta |
| Vega | -$200,000 | Each 1 vol point increase loses $200,000 |
| Theta | +$45,000 | Earning $45,000/day from time decay |
| Vanna | +$30,000 | Vol up 1 point, delta up 30 lots |

This desk is long direction, long convexity near current spot, short vol (collecting premium, earning theta), with vanna that increases directional risk if vol rises. Key risk: a sharp crude move plus vol spike hurts through vega; gamma gains may not offset.

**Simplified:** Each greek is one channel through which an option position gains or loses money. Delta is your direct directional bet. Gamma is how that direct bet accelerates. Vega is your bet on volatility levels. Theta is the rent you pay (or collect) for the option. The higher order greeks tell you how the lower ones drift as the world changes. A real book is not flat in any greek by accident: management chooses which to hedge and which to wear as conviction.

## Key mechanics and formulas

### First Order Greeks

These measure direct sensitivity to a single variable.

| Greek | Measures | Formula (Black-Scholes) | Units |
|-------|----------|------------------------|-------|
| [[Delta]] | dOption/dSpot | N(d1) for calls | Change in option price per $1 spot move |
| [[Vega]] | dOption/dVol | S × N'(d1) × sqrt(T) | Change in option price per 1% vol change |
| [[Theta]] | dOption/dTime | Complex (negative for long options) | Daily time decay in dollars |
| [[Rho]] | dOption/dRate | K × T × e^(-rT) × N(d2) for calls | Change per 1% rate change |

### Second Order Greeks

These measure how first order Greeks change, capturing curvature and cross effects.

| Greek | Measures | What It Tells You |
|-------|----------|-------------------|
| [[Gamma]] | dDelta/dSpot | How fast directional exposure shifts as spot moves. Source of [[Convexity]]. |
| [[Vanna]] | dDelta/dVol (= dVega/dSpot) | How directional exposure changes when vol moves. Critical for [[Risk Reversal]] positions. |
| [[Volga]] | dVega/dVol | How vol exposure changes when vol itself moves. Dominates OTM and [[Butterfly]] pricing. |
| [[Charm]] | dDelta/dTime | Delta drift as time passes (delta bleed). Critical near expiry. |
| [[Veta]] | dVega/dTime | Vega decay as time passes (vega bleed). Critical for long vol books and tail hedges. |

### Third Order Greeks (rarely traded directly)

| Greek | Measures | When It Matters |
|-------|----------|-----------------|
| [[Speed]] | dGamma/dSpot | Extreme gamma near barriers, hedging cost forecasting |
| [[Color]] | dGamma/dTime | Gamma evolution into expiry, especially [[0DTE]] |
| [[Zomma]] | dGamma/dVol | Wing gamma redistribution during vol regime shifts |
| [[Ultima]] | dVolga/dVol | Deep OTM pricing in stressed markets, exotic books |

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

- **Gamma-Theta tradeoff:** For a delta hedged position, theta = 0.5 × gamma × spot² × vol² / 252. Long gamma always costs theta. Short gamma always earns theta.
- **Vanna-Volga method:** Prices OTM options by adjusting Black-Scholes via vanna and volga to capture the [[Volatility Smile]]. Standard in FX options.
- **Put-call parity for Greeks:** Call delta - put delta = 1 (same strike/expiry). Call gamma = put gamma. Call vega = put vega.

## Prerequisites

- [[Vanilla Option]]
- [[Implied Volatility]]
- [[Hedging]]
- [[Forward Curve]]

## Related concepts (learn next)

- [[Delta]] as the most fundamental Greek, the starting point for all option risk management.
- [[Gamma]] because gamma drives convexity and how violently delta shifts during large moves.
- [[Vega]] because vol exposure is often the dominant portfolio risk, larger than directional risk.
- [[Theta]] because the gamma/theta tradeoff is the central tension in options trading.
- [[Vanna]] because it links spot and vol risk, dominating risk reversals and skewed positions.
- [[Volga]] because it drives OTM option pricing and the cost of tail protection.
- [[Vol Surface]] because the surface is the organizing framework for all Greeks across strikes and tenors.
- [[Convexity]] because Greeks quantify the non linearity that distinguishes options from linear instruments.
- [[Rho]] for long dated FX and rates exposure where the otherwise ignored first order rate greek becomes material.
- [[Charm]], [[Veta]], [[Color]] as the time bleed family. Charm bleeds delta, veta bleeds vega, color bleeds gamma.
- [[Speed]] and [[Zomma]] as the spot and vol derivatives of gamma, dominant for near expiry hedging cost and wing gamma dynamics.
- [[Ultima]] for third order vol convexity, the deepest vol greek encountered in tail hedge and exotic books.

## Common misconceptions

**"Managing delta is enough."** A delta neutral book can lose millions from gamma (sudden spot move), vega (vol shift), or theta (time decay). Professional desks manage all major Greeks simultaneously.

**"Greeks are constant."** Every Greek changes with spot, vol, time, and rates. Delta changes with spot (gamma). Vega changes with vol (volga). Gamma changes with time (color). This "Greeks of Greeks" dynamic makes option risk management continuous and active, not set and forget.

**"Second order Greeks only matter for exotic options."** Vanna and volga matter for ANY OTM option. Black-Scholes prices ATM reasonably but misprices OTM because it ignores the smile. Vanna-volga corrects this. Risk reversals, strangles, any OTM structure: second order Greeks are first order concerns.

**"You can hedge all Greeks simultaneously."** Hedging one Greek increases exposure to another. Buying options to reduce gamma raises vega and theta exposure. The art is choosing which Greeks to hedge and which to accept as residual.

## Sources

- Taleb, Nassim Nicholas. *Dynamic Hedging: Managing Vanilla and Exotic Options* (1997).
- Natenberg, Sheldon. *Option Volatility and Pricing*, 2nd ed. (2014).
- Hull, John. *Options, Futures, and Other Derivatives*, 11th ed.
- Wystup, Uwe. *FX Options and Structured Products*, 2nd ed. (2017).
- Bennett, Colin. *Trading Volatility*, Santander Equity Derivatives.
