# Trading Knowledge Vault

> Personal knowledge system for commodities, FX, and cross asset trading.
> Every concept learned gets documented. Every gap gets identified. The graph compounds.

---

## Quick Start

**Hit something you don't know?** Open [[SYSTEM]] and copy the master prompt into Claude. Paste the output as a new note. Done.

**See the graph:** `Ctrl+G` (full graph) or 3 dots menu on any note tab for local graph.

**See your gaps:** Every grayed out `[[link]]` in your vault is a concept you referenced but haven't documented yet.

---

## Vault Map

| Folder | What Goes Here |
|--------|---------------|
| `00-Inbox` | Raw captures, quick notes, unprocessed ideas |
| `01-Concepts` | Trading concepts with full writeups |
| `02-Instruments` | Specific contracts, their specs, fundamentals, spreads |
| `03-Markets` | Exchanges, venues, regulation, microstructure |
| `04-Strategies` | Trading strategies and playbooks |
| `05-People-and-Firms` | Traders, firms, researchers |
| `06-Data-and-Indicators` | Economic data, reports, releases |
| `07-Infrastructure` | Tools, platforms, code, APIs |
| `08-Journal` | Daily notes, weekly reviews, trade log |
| `09-Resources` | Books, papers, courses |

---

## Gap Tracker

Concepts I know I need to learn:

- [ ] [[Cointegration]]
- [ ] [[Roll Yield]]
- [ ] [[Basis Risk]]
- [ ] [[Convenience Yield]]
- [ ] [[Cost of Carry Model]]
- [ ] [[FX Forward Points]]
- [ ] [[LME Warrant System]]
- [ ] [[WASDE Report]]
- [ ] [[Commitment of Traders Report]]
- [ ] [[Volatility Surface]]
- [ ] [[Delta Hedging]]
- [ ] [[Crush Spread]]
- [ ] [[Spark Spread]]
- [ ] [[Carry Trade]]
- [ ] [[Funding Rate Arbitrage]]

---

## Dataview Dashboards

### All stubs (needs work)
```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  choice(contains(tags, "#type/concept"), "Concept", choice(contains(tags, "#type/instrument"), "Instrument", choice(contains(tags, "#type/strategy"), "Strategy", "Other"))) AS "Type",
  date-added AS "Added"
FROM "" AND #status/stub
SORT date-added DESC
```

### Recently added
```dataview
TABLE WITHOUT ID
  file.link AS "Note",
  choice(contains(tags, "#status/stub"), "Stub", choice(contains(tags, "#status/draft"), "Draft", choice(contains(tags, "#status/solid"), "Solid", "Mastered"))) AS "Status"
FROM "01-Concepts" OR "02-Instruments" OR "04-Strategies"
SORT file.ctime DESC
LIMIT 20
```

### Energy domain
```dataview
TABLE WITHOUT ID file.link AS "Note", date-added AS "Added"
FROM #energy/crude OR #energy/natgas OR #energy/power OR #energy/carbon OR #energy/refined
SORT file.name ASC
```

### Metals domain
```dataview
TABLE WITHOUT ID file.link AS "Note", date-added AS "Added"
FROM #metals/precious OR #metals/base OR #metals/ferrous OR #metals/battery
SORT file.name ASC
```

### Agriculture and softs domain
```dataview
TABLE WITHOUT ID file.link AS "Note", date-added AS "Added"
FROM #agri/grains OR #agri/oilseeds OR #agri/softs OR #agri/livestock
SORT file.name ASC
```

### FX domain
```dataview
TABLE WITHOUT ID file.link AS "Note", date-added AS "Added"
FROM #fx/g10 OR #fx/em OR #fx/structure
SORT file.name ASC
```

---

## Weekly Review Checklist

- [ ] Process inbox to zero
- [ ] Review 10 random notes (Ctrl+O, type "random")
- [ ] Update status tags honestly
- [ ] Pick 3 to 5 gap tracker items for next week
- [ ] Check graph for orphan nodes (notes with 0 connections)

---

## Key References

- [[SYSTEM]] | Full tag taxonomy, master prompt, graph instructions
- `_templates/` | Note templates for Templater plugin

