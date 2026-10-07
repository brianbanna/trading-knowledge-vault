#!/usr/bin/env python3
"""
Catalogue every note in the trading vault into a single markdown index.

Usage:
    python3 _scripts/build_vault_index.py [output_path]

Default output: Vault_Index.md at the vault root (the parent of _scripts/)
The script walks only the numbered concept/instrument folders plus the
"Physical commodities" tree, so it never catalogues itself, templates, or hubs.
Regenerate after adding notes; the index rebuilds in place.
"""
import os
import re
import sys
import json
from pathlib import Path
from datetime import date

# Vault root is the parent of this script's folder (_scripts/).
VAULT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = VAULT / "Vault_Index.md"

# Curated one-line summaries, keyed by vault-relative note path. When a note
# appears here its curated line is used; otherwise the summary is extracted
# mechanically from the note's Definition. Regenerate curated lines only when
# you want to refresh prose; new notes work immediately via the fallback.
CURATED_PATH = Path(__file__).resolve().parent / "summaries.json"
CURATED = json.loads(CURATED_PATH.read_text(encoding="utf-8")) if CURATED_PATH.exists() else {}

# Folder -> display group name (output order preserved).
GROUPS = [
    ("01-Concepts/market-structure", "Market structure"),
    ("01-Concepts/pricing-and-valuation", "Pricing and valuation"),
    ("01-Concepts/microstructure", "Microstructure"),
    ("01-Concepts/risk", "Risk"),
    ("01-Concepts/macro", "Macro"),
    ("01-Concepts/quantitative", "Quantitative"),
    ("02-Instruments", "Instruments"),
    ("03-Markets", "Markets"),
    ("04-Strategies", "Strategies"),
    ("05-People-and-Firms", "People and firms"),
    ("06-Data-and-Indicators", "Data and indicators"),
    ("07-Infrastructure", "Infrastructure"),
    ("10-Cases", "Cases"),
    ("Physical commodities", "Physical commodities"),
]

# Directories skipped during the walk (matched case-insensitively).
SKIP_DIRS = {"_templates", "_hubs", "_scripts", ".git", ".obsidian", ".claude"}

# Number of longest notes to list in the "Deepest notes" section.
DEEPEST_N = 30


def strip_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            return parts[2]
    return text


def clean_inline(s):
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", s)  # [[a|b]] -> b
    s = re.sub(r"\[\[([^\]]+)\]\]", r"\1", s)            # [[a]]   -> a
    s = s.replace("**", "").replace("__", "")
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)       # [t](u)  -> t
    return s.strip()


def first_sentence(para):
    para = para.strip()
    m = re.match(r"(.+?[.!?])(\s|$)", para)
    if m:
        sent = m.group(1).strip()
        # Extend past a too-short match (likely an abbreviation).
        if len(sent) < 25 and len(para) > len(sent):
            m2 = re.match(r"(.+?[.!?]){2}", para)
            if m2:
                sent = m2.group(0).strip()
        return sent
    return para[:200].strip()


def get_title(text, path):
    m = re.search(r"^#\s+(.+)$", text, re.MULTILINE)
    return m.group(1).strip() if m else path.stem


def get_summary(text, title=""):
    body = strip_frontmatter(text)
    lines = body.split("\n")

    # MOC / index / checklist files have no Definition; describe them.
    if re.search(r"^#+\s*Starter concept checklist", body, re.IGNORECASE | re.MULTILINE):
        topic = re.sub(r"\bindex\b", "", title, flags=re.IGNORECASE).strip()
        return f"Index and starter concept checklist for {topic}."

    # Preferred: first sentence of the Definition section.
    def_idx = None
    for i, ln in enumerate(lines):
        if re.match(r"^#+\s*Definition\b", ln, re.IGNORECASE):
            def_idx = i
            break
    if def_idx is not None:
        para = []
        for ln in lines[def_idx + 1:]:
            if re.match(r"^#+\s", ln):
                break
            if ln.strip() == "":
                if para:
                    break
                continue
            para.append(ln.strip())
        if para:
            return first_sentence(clean_inline(" ".join(para)))

    # Fallback: first prose paragraph (skip headings, tables, quotes, lists).
    para = []
    for ln in lines:
        st = ln.strip()
        if st.startswith("#") or st == "":
            if para:
                break
            continue
        if st[:1] in "|>-*":
            continue
        para.append(st)
    if para:
        return first_sentence(clean_inline(" ".join(para)))
    return ""


def collect(folder):
    base = VAULT / folder
    notes = []
    for root, dirs, files in os.walk(base):
        dirs[:] = [d for d in dirs if d.lower() not in SKIP_DIRS and not d.startswith(".")]
        for f in sorted(files):
            if not f.endswith(".md"):
                continue
            p = Path(root) / f
            text = p.read_text(encoding="utf-8", errors="ignore")
            title = get_title(text, p)
            rel = str(p.relative_to(VAULT))
            summary = CURATED.get(rel) or get_summary(text, title)
            wc = len(text.split())
            notes.append((title, summary, wc, rel))
    return notes


def main():
    out = Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 else DEFAULT_OUT

    all_notes = []
    group_data = []
    for folder, name in GROUPS:
        notes = collect(folder)
        group_data.append((name, notes))
        all_notes.extend(notes)

    total = len(all_notes)
    today = date.today().isoformat()

    out_lines = [
        "# Vault Index",
        "",
        f"Generated: {today}",
        f"Total notes: {total}",
        "",
        "Counts by subdomain:",
    ]
    for name, notes in group_data:
        if notes:
            out_lines.append(f"- {name}: {len(notes)}")
    out_lines += ["", "---", ""]

    for name, notes in group_data:
        if not notes:
            continue
        out_lines += [f"## {name} ({len(notes)})", ""]
        for title, summary, wc, rel in sorted(notes, key=lambda x: x[0].lower()):
            out_lines.append(f"- {title} — {summary or '(no summary)'}")
        out_lines.append("")

    out_lines += [
        "---",
        "",
        "# Deepest notes",
        "",
        f"Top {DEEPEST_N} notes by length (load these in full when needed):",
        "",
    ]
    deepest = sorted(all_notes, key=lambda x: x[2], reverse=True)[:DEEPEST_N]
    for i, (title, summary, wc, rel) in enumerate(deepest, 1):
        out_lines.append(f"{i}. {title} ({wc} words)")
    out_lines.append("")

    out.write_text("\n".join(out_lines), encoding="utf-8")
    missing = sum(1 for n in all_notes if not n[1])
    print(f"Wrote {out}")
    print(f"Total notes catalogued: {total}")
    print(f"Notes with no summary: {missing}")


if __name__ == "__main__":
    main()
