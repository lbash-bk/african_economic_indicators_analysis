import json
import pandas as pd
from pathlib import Path

raw = Path("data/raw")
arb = pd.DataFrame(json.loads(sorted(raw.glob("arbeitnow_*.json"))[-1].read_text(encoding="utf-8")))
rem = pd.DataFrame(json.loads(sorted(raw.glob("remotive_*.json"))[-1].read_text(encoding="utf-8")))

for name, df in [("Arbeitnow", arb), ("Remotive", rem)]:
    print(f"\n=== {name} ===")
    print(df.shape)
    print(df.columns.tolist())
    print(df.isna().sum())
    print(df.head(2).T)

print("Arbeitnow duplicate slugs:", arb["slug"].duplicated().sum())