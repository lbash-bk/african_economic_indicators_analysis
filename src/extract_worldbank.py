import json
import requests
from datetime import datetime
from pathlib import Path

RAW_DIR = Path("data/raw")
RAW_DIR.mkdir(parents=True, exist_ok=True)

COUNTRIES = "NGA;GHA;KEN;ZAF;EGY"
INDICATORS = {
    "FP.CPI.TOTL.ZG": "inflation",
    "NY.GDP.MKTP.KD.ZG": "gdp_growth",
    "NY.GDP.PCAP.CD": "gdp_per_capita",
    "SL.UEM.TOTL.ZS": "unemployment",
    "PA.NUS.FCRF": "exchange_rate",
    "SP.POP.TOTL": "population",
    "IT.NET.USER.ZS": "internet_users",
    "NY.GDP.PETR.RT.ZS": "oil_rents",
}

def fetch(code):
    url = f"https://api.worldbank.org/v2/country/{COUNTRIES}/indicator/{code}"
    r = requests.get(url, params={"format": "json", "per_page": 1000, "date": "2000:2025"}, timeout=30)
    r.raise_for_status()
    payload = r.json()
    return payload[1] if len(payload) > 1 and payload[1] else []

def main():
    rows = []
    for code, name in INDICATORS.items():
        data = fetch(code)
        print(f"{name}: {len(data)} records")
        for d in data:
            rows.append({
                "country": d["country"]["value"],
                "country_code": d["countryiso3code"],
                "indicator_code": code,
                "indicator": name,
                "year": int(d["date"]),
                "value": d["value"],
            })

    stamp = datetime.now().strftime("%Y%m%d_%H%M")
    out = RAW_DIR / f"worldbank_{stamp}.json"
    out.write_text(json.dumps(rows, indent=2), encoding="utf-8")
    print(f"Saved {len(rows)} rows to {out}")

if __name__ == "__main__":
    main()