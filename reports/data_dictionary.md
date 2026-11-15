# Data dictionary

The main processed analytical file is expected to contain one row per country-year.

| Field | Type | Description |
|---|---|---|
| `country` | Text | Country name |
| `year` | Whole number | Observation year, 2000–2025 |
| `exchange_rate` | Decimal | Local currency units per US dollar |
| `gdp_growth` | Decimal | Annual GDP growth rate (%) |
| `gdp_per_capita` | Decimal | GDP per capita, current US$ |
| `inflation` | Decimal | Annual consumer-price inflation (%) |
| `internet_users` | Decimal | Individuals using the internet (%) |
| `oil_rents` | Decimal | Oil rents as a share of GDP (%) |
| `population` | Whole number / decimal | Total population |
| `unemployment` | Decimal | Unemployment rate (%) |

## World Bank indicator codes

| Field | Indicator code |
|---|---|
| `inflation` | `FP.CPI.TOTL.ZG` |
| `gdp_growth` | `NY.GDP.MKTP.KD.ZG` |
| `gdp_per_capita` | `NY.GDP.PCAP.CD` |
| `unemployment` | `SL.UEM.TOTL.ZS` |
| `exchange_rate` | `PA.NUS.FCRF` |
| `population` | `SP.POP.TOTL` |
| `internet_users` | `IT.NET.USER.ZS` |
| `oil_rents` | `NY.GDP.PETR.RT.ZS` |

## Coverage notes

- Internet users: latest available year in the prepared dataset is 2024; five 2025 values are missing.
- Oil rents: latest available year in the prepared dataset is 2021; 20 values for 2022–2025 are missing.
- Missing values should remain blank/null and must not be interpreted as zero.

## Annual-change dataset

The annual-change export is expected to contain the country and year fields plus:
- `gdp_per_capita_pct_change`
- `population_pct_change`
- `exchange_rate_pct_change`
- `internet_users_pct_change`

These fields represent year-over-year percentage changes. The first observation for each country has no prior year and is therefore missing. Large percentage changes in internet use can occur when the starting penetration rate is very small.
