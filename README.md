# African Economic Indicators Analysis (2000–2025)

An exploratory, cross-country analysis of selected macroeconomic, labour-market, demographic, energy and digital-development indicators for **Egypt, Ghana, Kenya, Nigeria and South Africa**. The project uses World Bank indicators and presents the results through Python-based data preparation and analysis and an interactive Power BI dashboard.

## Project objectives

- Compare economic performance across five African economies.
- Examine trends in GDP growth, inflation, GDP per capita, unemployment and exchange rates.
- Explore demographic and digital-development patterns.
- Investigate oil rents and their relationship with economic growth.
- Communicate findings through a multi-page Power BI dashboard.

## Countries and period

- Egypt, Arab Rep.
- Ghana
- Kenya
- Nigeria
- South Africa
- Annual observations: 2000–2025

The analytical panel contains **130 country-year rows** (5 countries × 26 years) and eight indicators. Some indicators have shorter reporting coverage; missing observations are retained as missing rather than converted to zero.

## Tools

- Python: data preparation, exploratory analysis, descriptive statistics and correlation analysis
- pandas / NumPy: data manipulation and numerical analysis
- Matplotlib / Seaborn: exploratory visualisation (where used in the analysis)
- Power BI Desktop: interactive dashboard
- World Bank indicator data: source of the economic and development measures

## Repository structure

```text
african_economic_indicators_analysis/
├── data/
│   ├── raw/                 # Original downloaded source files (add your files)
│   ├── processed/           # Cleaned/exported analytical CSV files (add your files)
│ 
├── notebooks/
│   └──                      # completed analysis notebook
├── src/
│   └──                      # reusable Python scripts
├── dashboard/
│   ├──                      #power bi dashboard
│   └── screenshots/        # Add dashboard page screenshots
├── reports/
│   |    ├── project_report.md
│   |    └── data_dictionary.md   
│   └──  tables/  
|            |
|            ├── correlation_summary.csv
│            └── gdp_growth_by_period.csv
|       
├── docs/
│   
├── .gitignore
├── requirements.txt
└── README.md
```

## Key findings

- Ghana recorded the highest average GDP growth in the five-country comparison (**5.60%**), while South Africa recorded the lowest (**2.18%**).
- Ghana also had the highest average inflation (**17.64%**); South Africa had the lowest (**5.17%**).
- South Africa had the highest average GDP per capita in the group (approximately **US$6,064**), while Kenya had the lowest (approximately **US$1,290**).
- South Africa's average unemployment rate was the highest (**26.04%**) among the five countries.
- South Africa recorded the highest average internet-use share (**37.85%**) over its available observations; its 2024 value reached **78.36%**.
- Nigeria had the largest population, increasing from approximately **126.38 million in 2000** to **237.53 million in 2025**.
- Nigeria had the highest average oil rents as a share of GDP (**10.82%**) over the available observations. Oil-rent data in this analysis ends in 2021.
- In the pooled observations, GDP per capita and internet use had a positive Pearson correlation (**r = 0.564**), while GDP growth and unemployment had a negative correlation (**r = -0.408**). These are associations, not evidence of causation.

See [`reports/project_report.md`](reports/project_report.md) for the full methodology, results, interpretation and limitations.

## Dashboard

The Power BI report is organised into four analytical pages:

1. **African Economic Overview** — headline KPIs, country comparisons, GDP growth trend and population.
2. **Economic Growth & Inflation** — GDP growth, inflation, their relationship and GDP growth by period.
3. **Living Standards & Digital Development** — GDP per capita, internet adoption and population trends.
4. **Labour Market, Oil & Currency** — unemployment, oil rents and exchange-rate trends.

Add the `.pbix` file and exported dashboard screenshots to the `powerbi/` folder before publishing the repository. The dashboard file is not embedded in this starter package.

## Data source

World Bank, World Development Indicators (WDI). Indicator names and codes are listed in [`reports/data_dictionary.md`](reports/data_dictionary.md).

For reproducibility, include the source download date and the exact World Bank download/API query in your notebook or a separate source-notes file. World Bank observations can be revised.

## Important interpretation notes

- Correlation does not establish causation.
- GDP per capita is measured in current US dollars and is affected by prices and exchange rates; it is not a measure of real purchasing-power growth.
- Exchange rates are local-currency units per US dollar. Compare movements within a country rather than comparing the absolute levels across currencies.
- Internet-use observations are available through 2024 in this dataset; oil-rent observations are available through 2021.
- Missing values were not treated as zero.
- Country-level correlations are based on relatively small annual samples and should be interpreted cautiously.


## Author

BASHIR LAWAN ISYAKU, https://lbash-bk.github.io/bashir-lawan-isyaku-portfolio/
