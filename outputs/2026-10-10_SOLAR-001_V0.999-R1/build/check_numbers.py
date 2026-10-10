"""SOLAR-001 V0.999-R1 - numeric-preservation check between the V0.999 Markdown source and the R1 Markdown source.

Every numeric token in the R1 text must already occur in the V0.999 text, or be listed with its source in
records/R1-New-Numbers.csv (the R1 additions and new section numbers). Every V0.999 token that no longer appears must
have a note below. Tokens are compared  after normalizing the minus sign, the
'$X million/billion' -> '$Xm/$Xbn' style and thousands separators.
Usage: python3 build/check_numbers.py V0999.md R1.md OUT.json
"""
import collections, csv, json, re, sys
from pathlib import Path

NUM = re.compile(r"(?<![\w.])-?\d[\d,]*(?:\.\d+)?")


def norm(t):
    t = t.replace("−", "-").replace("–", "-")
    t = re.sub(r"(\d) million\b", r"\1m", t); t = re.sub(r"(\d) billion\b", r"\1bn", t)
    t = re.sub(r"\]\([^)]*\)", "]", t)  # link targets (URLs, paths) are not report numbers
    return t


def nums(t):
    return collections.Counter(m.replace(",", "") for m in NUM.findall(norm(t)))


def tables(t):
    out = {}
    for m in re.finditer(r"\*\*Table ([0-9A-D]+-\d+[AB]?)\.[^\n]*\*\*\n\n((?:\|[^\n]*\n)+)", t):
        out[m[1]] = [[c.strip() for c in r.strip().strip("|").split("|")] for r in m[2].strip().split("\n") if not re.match(r"^\|[\s:|-]+\|$", r.strip())]
    return out


NOTES = {"11.8": "section number: V0.999 11.8 (tail dependence) is R1 11.6; its 2026 evidence is R1 11.7",
         "11.9": "section number: V0.999 11.9 (resampling) moved to Appendix B.8",
         "12.6": "section number: V0.999 12.6 (controlled update) is R1 12.5"}


def main():
    a, b, out = map(Path, sys.argv[1:4])
    ta, tb = a.read_text(), b.read_text()
    na, nb = nums(ta), nums(tb)
    new = sorted(k for k in nb if k not in na)
    dropped = sorted(k for k in na if k not in nb)
    # structural numbers of this edition: version/date, Table 0-1 / 13-x numbering, renumbered 10-x tables, list ordinals
    registry = {r["token"]: r for r in csv.DictReader(open(Path(__file__).resolve().parents[1] / "records" / "R1-New-Numbers.csv"))}
    unexplained = [k for k in new if k not in registry]
    unused_registry = sorted(k for k in registry if k not in nb)
    # table numeric cells: every numeric cell string of each V0.999 table must exist in some input table
    cells_a = set()
    for rows in tables(ta).values():
        for r in rows: cells_a.update(norm(c).replace(",", "") for c in r if re.search(r"\d", c))
    tb_tables = tables(tb); cell_missing = {}
    for tid, rows in tb_tables.items():
        miss = [c for r in rows for c in r if re.search(r"\d", c) and NUM.search(norm(c)) and norm(c).replace(",", "") not in cells_a
                and not all(x.replace(",", "") in na or x.replace(",", "") in registry for x in NUM.findall(norm(c)))]
        if miss: cell_missing[tid] = miss
    rep = {"baseline": a.name, "r1": b.name, "distinct_numeric_tokens_baseline": len(na), "distinct_numeric_tokens_r1": len(nb),
           "tokens_absent_from_baseline": new, "registered_new_tokens": {k: registry[k] for k in new if k in registry},
           "unexplained_new_tokens": unexplained, "registry_tokens_not_used": unused_registry,
           "tokens_dropped_from_baseline": dropped, "dropped_token_notes": NOTES, "unexplained_dropped": [k for k in dropped if k not in NOTES],
           "tables_checked": len(tb_tables), "table_cells_with_numbers_not_in_input": cell_missing,
           "result": "PASS" if not unexplained and not cell_missing and not unused_registry and all(k in NOTES for k in dropped) else "REVIEW"}
    out.write_text(json.dumps(rep, indent=1, ensure_ascii=False))
    print(rep["result"], "new:", len(new), "unexplained:", unexplained, "cells:", cell_missing, "unused registry:", unused_registry, "dropped:", dropped)


if __name__ == "__main__":
    main()
