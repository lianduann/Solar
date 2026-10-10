"""Extract the label/value pairs of the retained Texas Comptroller Chapter 313 Form 773 (2023 biennial progress report) workbooks.
Values are copied as filed (agreement holder's self-report); nothing is inferred. Usage: 04_extract_ch313_773.py <comparables_dir> <out_csv>"""
import glob, hashlib, sys
from pathlib import Path
import pandas as pd
rows = []
for f in sorted(glob.glob(str(Path(sys.argv[1]) / "C*_773_2023.xlsx"))):
    d = pd.read_excel(f, header=None)
    sha = hashlib.sha256(Path(f).read_bytes()).hexdigest()
    for i, r in d.iterrows():
        v = [x for x in r if pd.notna(x) and not str(x).startswith("Column")]
        if len(v) >= 2:
            rows.append(dict(local_file=Path(f).name, sha256=sha, row=i + 1, field=str(v[0]).strip(), value=str(v[1]).strip()))
out = pd.DataFrame(rows); out.to_csv(sys.argv[2], index=False)
w = out.pivot_table(index="local_file", columns="field", values="value", aggfunc="first")
keep = ["Application ID", "Company Name of Agreement Holder", "Name of Central Appraisal District (CAD)", "Name of School District", "Date Of Commmencement of Commercial Operations",
        "Amount of Qualified Investment the Applicant Committed", "The Amount The Agreement Holder Had Made to Date", "Total Investment through The Life of The Agreement", "Limitation Amount in Executed Agreement", "First Year Of Property Value Limitation"]
print(w[[k for k in keep if k in w.columns]].to_string())
