---
aliases: [market maker inventory, dealer inventory, net position, book position]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Inventory

## Definition

Inventory is the current net position accumulated from market making activity. When a dealer buys from a client, inventory goes [[Long]]; when a dealer sells to a client, inventory goes [[Short]]. Unlike a directional trader who takes positions intentionally, a market maker accumulates inventory as a byproduct of providing [[Liquidity]]. The goal is to earn the [[Bid]]-[[Ask]] [[Spread]] while keeping inventory close to [[Flat]] to minimize [[Inventory Risk]].

## Why it matters (commodities and FX)

An FX dealer quoting [[EUR USD]] might accumulate 100 million EUR of inventory in minutes from client flow. That inventory carries [[Inventory Risk]] because if EUR/USD moves 10 pips against the position, the mark to market loss is $100,000. In commodities, a [[LME]] dealer making markets in copper futures faces the same dynamic. Inventory management (how quickly and at what cost the desk returns to flat) is the central challenge of market making.

## Concrete example

A dealer quotes [[EUR USD]] at 1.08497 / 1.08503. Over 30 minutes:

- Client A buys 20M EUR at 1.08503. Desk is now short 20M EUR.
- Client B buys 15M EUR at 1.08502. Desk is now short 35M EUR.
- Client C sells 40M EUR at 1.08497. Desk is now long 5M EUR.
- Client D sells 10M EUR at 1.08496. Desk is now long 15M EUR.

Net inventory: long 15M EUR.

**If price rises 5 pips to 1.08550:** The desk earns $7,500 on inventory (15M * 0.00050) plus the spread revenue from all 4 trades.

**If price drops 10 pips to 1.08400:** The desk loses $15,000 on inventory, which may exceed the spread revenue of approximately $5,250 earned from the trades.

The desk applies [[Skew Microstructure|skew]] to encourage selling from clients and reduce the long inventory.

## Key mechanics and formulas

**Inventory tracking:**
Inventory = sum of all fills (buys positive, sells negative)

**Inventory half life:** The time for inventory to decay to half its peak. Faster is safer.

Half life = ln(2) / lambda

Where lambda = the rate at which the desk hedges or attracts offsetting flow.

**Inventory cost:**
Inventory cost = |inventory| * sigma * sqrt(holding_time)

Where:
- sigma = [[Volatility]] of the instrument
- holding_time = how long inventory is held before flattening

**Key inventory limits:**
- Soft limit: desk starts actively hedging (e.g., 50M EUR)
- Hard limit: system blocks new trades that would increase inventory (e.g., 100M EUR)

## Prerequisites

- [[Position]]
- [[Long]]
- [[Short]]
- [[Flat]]
- [[Bid]]
- [[Ask]]

## Related concepts (learn next)

- [[Inventory Risk]] for the formal risk framework around holding inventory
- [[Skew Microstructure]] for how inventory drives quote asymmetry
- [[Reservation Price]] for the theoretical model of inventory adjusted fair value
- [[Internalization]] for reducing inventory by matching client flows internally
- [[Turnover]] for measuring how frequently inventory cycles
- [[Adverse Selection]] for how informed flow creates one directional inventory buildup
- [[Kill Switch]] for emergency inventory protection

## Common misconceptions

1. **"Inventory is the same as a directional position."** A directional trader wants a position; a market maker accumulates inventory as a side effect of quoting. The intent and management are completely different.

2. **"Zero inventory is always the target."** Some desks intentionally hold small inventory when they have a short term view (e.g., skewing into expected flow). The target is risk adjusted optimal inventory, not always zero.

3. **"Inventory only matters for large desks."** Even a small prop desk market making 1 lot on COMEX gold has inventory risk. The absolute size differs, but the dynamics of accumulation, skew, and risk are identical.

## Sources

- Avellaneda, M. and Stoikov, S., "High Frequency Trading in a Limit Order Book," 2008
- Gueant, O., Lehalle, C.A., and Fernandez Tapia, J., "Dealing with the Inventory Risk," 2013
- Harris, Larry, "Trading and Exchanges," Oxford University Press
