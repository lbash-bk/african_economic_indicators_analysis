import json
import pandas as pd
from pathlib import Path

RAW = Path("data/raw")
OUT = Path("data/raw/worldbank_raw.csv")

f = sorted(RAW.glob("worldbank_*.json"))[-1]
df = pd.DataFrame(json.loads(f.read_text(encoding="utf-8")))

df.to_csv(OUT, index=False)
print(f"Saved {len(df)} rows from {f.name} to {OUT}")