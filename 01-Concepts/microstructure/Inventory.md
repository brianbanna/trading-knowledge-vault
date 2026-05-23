---
aliases: [market maker inventory, dealer inventory, net position, book position]
tags:
  - "#microstructure"
date-added: "2026-03-27"
---

# Inventory

## Definition

Inventory is the net position accumulated from market making activity. When a dealer buys from a client, inventory goes [[Long]]; when a dealer sells to a client, inventory goes [[Short]]. Unlike a directional trader who takes positions on purpose, a market maker accumulates inventory as a byproduct of providing [[Liquidity]]. The goal is to earn the [[Bid]] [[Ask]] [[Spread]] while keeping inventory close to [[Flat]] to minimize [[Inventory Risk]].

## Why it matters (commodities and FX)

An FX dealer quoting [[EUR USD]] can accumulate 100M EUR of inventory in minutes from client flow. That carries [[Inventory Risk]]: a 10 pip move against the position is a $100,000 mark to market loss. In commodities, an [[LME]] dealer making markets in copper futures faces the same dynamic. Inventory management (how fast and at what cost the desk returns to flat) is the central challenge of market making.

## Concrete example

**Concrete:** Dealer quotes [[EUR USD]] at 1.08497 / 1.08503. Over 30 minutes: Client A buys 20M EUR at 1.08503 (desk short 20M). Client B buys 15M EUR at 1.08502 (short 35M). Client C sells 40M EUR at 1.08497 (long 5M). Client D sells 10M EUR at 1.08496 (long 15M). Net inventory: long 15M EUR. If price rises 5 pips to 1.08550: desk earns $7,500 on inventory (15M x 0.00050) plus spread revenue. If price drops 10 pips to 1.08400: desk loses $15,000 on inventory, exceeding ~$5,250 spread revenue from the trades. Desk applies [[Skew Microstructure|skew]] to encourage selling from clients and cut the long.

**Simplified:** Inventory is what the desk is left holding after taking the other side of client trades. A trader picks a position because they want it. A market maker ends up with one because clients traded against them. Hold inventory too long and the market moves against you. The job is to flatten it quickly while still earning the spread.

## Key mechanics and formulas

**Inventory tracking:**
Inventory = sum of all fills (buys positive, sells negative)

**Inventory half life:** time for inventory to decay to half its peak. Faster is safer.

Half life = ln(2) / lambda

Where lambda = rate the desk hedges or attracts offsetting flow.

**Inventory cost:**
Inventory cost = |inventory| * sigma * sqrt(holding_time)

Where:
- sigma = [[Volatility]] of the instrument
- holding_time = how long inventory is held before flattening

**Inventory limits:**
- Soft limit: desk starts actively hedging (e.g., 50M EUR)
- Hard limit: system blocks new trades increasing inventory (e.g., 100M EUR)

## Prerequisites

- [[Position]]
- [[Long]]
- [[Short]]
- [[Flat]]
- [[Bid]]
- [[Ask]]

## Related concepts (learn next)

- [[Inventory Risk]] for the formal risk framework
- [[Skew Microstructure]] for how inventory drives quote asymmetry
- [[Reservation Price]] for the inventory adjusted fair value model
- [[Internalization]] for reducing inventory by matching client flows internally
- [[Turnover]] for measuring how frequently inventory cycles
- [[Adverse Selection]] for how informed flow creates one directional buildup
- [[Kill Switch]] for emergency inventory protection

## Common misconceptions

1. **"Inventory is the same as a directional position."** A directional trader wants a position; a market maker accumulates inventory as a side effect of quoting. Intent and management differ completely.

2. **"Zero inventory is always the target."** Some desks hold small inventory when they have a short term view (skewing into expected flow). The target is risk adjusted optimal inventory, not always zero.

3. **"Inventory only matters for large desks."** Even a small prop desk making 1 lot on COMEX gold has inventory risk. Absolute size differs, but accumulation, skew, and risk dynamics are identical.

## Sources

- Avellaneda, M. and Stoikov, S., "High Frequency Trading in a Limit Order Book," 2008
- Gueant, O., Lehalle, C.A., and Fernandez Tapia, J., "Dealing with the Inventory Risk," 2013
- Harris, Larry, "Trading and Exchanges," Oxford University Press
