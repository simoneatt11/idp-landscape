#!/usr/bin/env python3
"""Validate the CSV datasets and regenerate derived outputs.

Usage:
    python3 scripts/build.py          # validate + write site/data.js + refresh README tables
    python3 scripts/build.py --check  # validate only (used in CI); exits 1 on errors

The CSV files in data/ are the single source of truth. Everything else
(site/data.js, the tables between AUTO markers in README.md) is generated.
"""
import csv
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

REGIONS = {"Europe", "USA", "China"}
RELEVANCE = {"core", "adjacent", "watchlist"}
CONFIDENCE = {"high", "medium", "low"}
STAGES = ["research", "discovery", "preclinical", "phase-1", "phase-2", "phase-3",
          "approved", "discontinued", "closed"]
EVENT_TYPES = {"funding", "deal", "clinical", "science", "setback"}
DATE_RE = re.compile(r"^\d{4}(-\d{2}(-\d{2})?)?$")


def load(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def split(v):
    return [x.strip() for x in (v or "").split(";") if x.strip()]


def validate():
    errors = []
    companies = load("companies.csv")
    sources = load("sources.csv")
    approaches = load("approaches.csv")
    academia = load("academic_groups.csv")
    tools = load("tools.csv")
    events = load("events.csv")

    src_ids = [s["id"] for s in sources]
    for dup, n in Counter(src_ids).items():
        if n > 1:
            errors.append(f"sources.csv: duplicate id {dup}")
    src_ids = set(src_ids)
    appr_ids = {a["id"] for a in approaches}
    comp_ids = [c["id"] for c in companies]
    for dup, n in Counter(comp_ids).items():
        if n > 1:
            errors.append(f"companies.csv: duplicate id {dup}")
    comp_ids = set(comp_ids)

    def check_sources(where, value):
        refs = split(value)
        if not refs:
            errors.append(f"{where}: no sources")
        for r in refs:
            if r not in src_ids:
                errors.append(f"{where}: unknown source {r}")

    for c in companies:
        w = f"companies.csv[{c['id']}]"
        for field in ("id", "name", "region", "status", "relevance", "approach", "stage", "confidence"):
            if not c.get(field):
                errors.append(f"{w}: missing {field}")
        if c["region"] not in REGIONS:
            errors.append(f"{w}: region must be one of {sorted(REGIONS)}")
        if c["relevance"] not in RELEVANCE:
            errors.append(f"{w}: bad relevance {c['relevance']}")
        if c["confidence"] not in CONFIDENCE:
            errors.append(f"{w}: bad confidence {c['confidence']}")
        if c["stage"] not in STAGES:
            errors.append(f"{w}: stage must be one of {STAGES}")
        for a in [c["approach"]] + split(c["approach_secondary"]):
            if a not in appr_ids:
                errors.append(f"{w}: unknown approach {a}")
        if c["funding_total_usd_m"]:
            try:
                float(c["funding_total_usd_m"])
            except ValueError:
                errors.append(f"{w}: funding_total_usd_m must be a number")
        for d in ("last_event_date", "last_verified"):
            if c[d] and not DATE_RE.match(c[d]):
                errors.append(f"{w}: {d} must be YYYY, YYYY-MM or YYYY-MM-DD")
        check_sources(w, c["sources"])

    for a in academia:
        w = f"academic_groups.csv[{a['id']}]"
        if a["region"] not in REGIONS:
            errors.append(f"{w}: bad region")
        for cid in split(a["company_links"]):
            if cid not in comp_ids:
                errors.append(f"{w}: unknown company {cid}")
        check_sources(w, a["sources"])

    for t in tools:
        check_sources(f"tools.csv[{t['id']}]", t["sources"])

    for e in events:
        w = f"events.csv[{e['date']} {e['title'][:30]}]"
        if not DATE_RE.match(e["date"]):
            errors.append(f"{w}: bad date")
        if e["type"] not in EVENT_TYPES:
            errors.append(f"{w}: type must be one of {sorted(EVENT_TYPES)}")
        if e["company_id"] and e["company_id"] not in comp_ids:
            errors.append(f"{w}: unknown company {e['company_id']}")
        check_sources(w, e["sources"])

    bundle = dict(companies=companies, sources=sources, approaches=approaches,
                  academia=academia, tools=tools, events=events, stages=STAGES,
                  built=date.today().isoformat())
    return errors, bundle


def md_table(rows, cols):
    head = "| " + " | ".join(h for h, _ in cols) + " |"
    sep = "|" + "|".join("---" for _ in cols) + "|"
    body = ["| " + " | ".join(fn(r).replace("|", "/") for _, fn in cols) + " |" for r in rows]
    return "\n".join([head, sep] + body)


def refresh_readme(b):
    appr = {a["id"]: a["label"] for a in b["approaches"]}
    order = {s: i for i, s in enumerate(STAGES)}
    rows = sorted(b["companies"], key=lambda c: (["Europe", "USA", "China"].index(c["region"]),
                                                   c["relevance"] != "core", c["name"]))

    def name(c):
        return f"[{c['name']}]({c['website']})" if c["website"] else c["name"]

    def money(c):
        return f"${float(c['funding_total_usd_m']):g}M" if c["funding_total_usd_m"] else "n/d"

    table = md_table(rows, [
        ("Company", name),
        ("Region", lambda c: c["region"]),
        ("Approach", lambda c: appr[c["approach"]]),
        ("Stage", lambda c: c["stage"]),
        ("Lead / targets", lambda c: c["lead_asset"] or c["targets"]),
        ("Funding (USD)", money),
        ("Status", lambda c: c["status"]),
        ("Confidence", lambda c: c["confidence"]),
    ])
    counts = Counter(c["region"] for c in b["companies"])
    summary = (f"_{len(b['companies'])} organisations tracked "
               f"(Europe {counts['Europe']}, USA {counts['USA']}, China {counts['China']}) · "
               f"{len(b['academia'])} academic groups · {len(b['tools'])} tools/databases · "
               f"{len(b['sources'])} sources · generated {b['built']}_")
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    block = f"<!-- AUTO:COMPANIES START -->\n{summary}\n\n{table}\n<!-- AUTO:COMPANIES END -->"
    text = re.sub(r"<!-- AUTO:COMPANIES START -->.*?<!-- AUTO:COMPANIES END -->", block, text, flags=re.S)
    readme.write_text(text, encoding="utf-8")


def main():
    errors, bundle = validate()
    if errors:
        print("Validation errors:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    print(f"OK: {len(bundle['companies'])} companies, {len(bundle['academia'])} academic groups, "
          f"{len(bundle['tools'])} tools, {len(bundle['events'])} events, {len(bundle['sources'])} sources")
    if "--check" in sys.argv:
        return
    (ROOT / "site" / "data.js").write_text(
        "// Generated by scripts/build.py - do not edit by hand.\nwindow.IDP_DATA = "
        + json.dumps(bundle, ensure_ascii=False, indent=1) + ";\n", encoding="utf-8")
    refresh_readme(bundle)
    print("Wrote site/data.js and refreshed README.md")


if __name__ == "__main__":
    main()
