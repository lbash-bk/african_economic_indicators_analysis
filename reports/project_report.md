# Project Report: African Economic Indicators Analysis (2000–2025)

## 1. Executive summary

This project examines selected economic, labour-market, demographic, energy and digital-development indicators for Egypt, Ghana, Kenya, Nigeria and South Africa over 2000–2025. The analysis uses annual World Bank indicator observations, prepares a country-year analytical dataset, explores descriptive trends and correlations, and communicates the results in a four-page Power BI dashboard.

The comparison reveals meaningful differences between the five economies. Ghana has the highest average GDP growth and inflation in the selected sample. South Africa has the highest average GDP per capita, unemployment and internet-use share. Nigeria has the largest population and the highest average oil rents as a share of GDP. The correlation analysis also identifies associations between several indicators, but the results do not establish causal relationships.

## 2. Research objectives and questions

The analysis was designed to answer the following questions:

1. How did GDP growth and inflation evolve across the five countries?
2. How do GDP per capita and unemployment compare?
3. How have population and internet adoption changed?
4. What does the available oil-rent data show about the countries' reliance on oil rents?
5. How did exchange rates change over time?
6. Which indicators move together in the pooled and country-level observations?

## 3. Scope and dataset

### Countries
- Egypt, Arab Rep.
- Ghana
- Kenya
- Nigeria
- South Africa

### Period
2000–2025, annual observations.

### Dataset structure
The cleaned country-year table contains 130 rows and 10 columns: country, year and eight indicator columns. This represents five countries observed over 26 years.

The long-format source table used the fields `country`, `year`, `indicator` and `value`. The analytical table was reshaped to one row per country-year.

### Indicators

| Indicator | World Bank code | Interpretation |
|---|---|---|
| Inflation | `FP.CPI.TOTL.ZG` | Annual consumer-price inflation (%) |
| GDP growth | `NY.GDP.MKTP.KD.ZG` | Annual GDP growth (%) |
| GDP per capita | `NY.GDP.PCAP.CD` | GDP per capita, current US$ |
| Unemployment | `SL.UEM.TOTL.ZS` | Unemployment rate (%) |
| Exchange rate | `PA.NUS.FCRF` | Local currency units per US$ |
| Population | `SP.POP.TOTL` | Total population |
| Internet users | `IT.NET.USER.ZS` | Individuals using the internet (%) |
| Oil rents | `NY.GDP.PETR.RT.ZS` | Oil rents as a share of GDP (%) |

## 4. Data preparation and methodology

The analysis followed these broad stages:

1. Retrieved the selected World Bank indicators for the five countries and the 2000–2025 period.
2. Organised observations into a long-format table.
3. Cleaned and reshaped the data into a country-year analytical table.
4. Reviewed missing values and retained unavailable observations as null/missing values rather than replacing them with zero.
5. Calculated annual percentage changes for GDP per capita, population, exchange rate and internet-use share.
6. Produced descriptive statistics and trend comparisons.
7. Calculated Pearson correlations for selected indicator pairs, including pooled and country-level results.
8. Compared selected Pearson and Spearman coefficients to assess whether relationships were sensitive to the correlation method.
9. Built a Power BI dashboard to present the main indicators and comparisons.

### Data coverage and missing observations

The analytical panel has 130 country-year rows. Internet-use data has five missing observations, with the latest available year being 2024 for each country. Oil-rent data has 20 missing observations, with the latest available year being 2021 for each country. Other listed indicators are complete through 2025 in the prepared dataset.

These coverage differences matter: a chart should not imply that missing observations are zero or that all indicators extend through 2025.

## 5. Descriptive findings

### 5.1 GDP growth

- Ghana recorded the highest average GDP growth at **5.60%**.
- South Africa recorded the lowest average GDP growth at **2.18%**.
- Nigeria showed the greatest volatility among the five countries, with a standard deviation of **3.98 percentage points**.
- Nigeria's GDP growth reached **15.33% in 2002** and fell to **-6.37% in 2020**.
- South Africa's GDP growth fell to **-6.17% in 2020**.

The period averages show a marked slowdown in Nigeria and South Africa in the more recent periods:

| Country | 2000–2007 | 2008–2013 | 2014–2019 | 2020–2025 |
|---|---:|---:|---:|---:|
| Egypt | 4.75% | 3.86% | 4.45% | 4.00% |
| Ghana | 4.96% | 8.76% | 4.86% | 4.06% |
| Kenya | 4.02% | 4.18% | 4.80% | 4.53% |
| Nigeria | 7.74% | 6.50% | 2.05% | 1.74% |
| South Africa | 4.29% | 2.12% | 1.06% | 0.53% |

### 5.2 Inflation

- Ghana had the highest average inflation at **17.64%**, with a standard deviation of **10.19**. Its maximum in the dataset was **41.51% in 2001**.
- South Africa had the lowest average inflation at **5.17%**.
- Nigeria's inflation increased from **6.93% in 2000** to **23.01% in 2025**. It reached **33.24% in 2024**.
- Egypt's inflation reached **33.88% in 2023**.

Inflation patterns differ considerably across countries and periods. The dashboard's trend comparisons are useful for identifying when inflation accelerated or eased, but the descriptive statistics alone do not explain the causes.

### 5.3 GDP per capita

- South Africa recorded the highest average GDP per capita, approximately **US$6,064**.
- Kenya recorded the lowest average, approximately **US$1,290**.
- Nigeria's GDP per capita peaked at **US$3,189.81 in 2019**, before falling to **US$1,224.25 in 2025**.

GDP per capita is expressed in current US dollars. Changes can reflect exchange-rate movements and price-level changes as well as changes in economic output. It should not be interpreted as a direct measure of real purchasing-power growth.

### 5.4 Unemployment

- South Africa recorded the highest average unemployment rate at **26.04%**.
- South Africa's unemployment rate reached **34.01% in 2021**.
- Kenya's average was **3.59%**, while Nigeria's was **4.01%**.

The unemployment series uses modelled estimates. Cross-country comparisons should be made cautiously because labour-market definitions, survey coverage and estimation methods can differ.

### 5.5 Internet adoption

- South Africa had the highest average internet-use share at **37.85%** across available observations.
- South Africa reached **78.36% in 2024**.
- Kenya had the lowest average in the selected group at **13.11%**.
- Internet-use shares increased over time across all five countries in the prepared dataset.

Internet-use data ends in 2024, so 2025 should not be represented as a zero or as a measured value.

### 5.6 Population

Nigeria had the largest population in the comparison. Its population increased from approximately **126.38 million in 2000** to **237.53 million in 2025**, an increase of approximately **111.15 million**.

### 5.7 Exchange rates

Nigeria's exchange rate increased from approximately **101.70 local-currency units per US dollar in 2000** to **1,518.38 in 2025**. Egypt's increased from approximately **3.47** to **49.23** over the same period.

Exchange-rate values are expressed in each country's own currency units per US dollar. Their absolute levels should not be compared as if they were the same currency; the more meaningful comparison is the direction and scale of change within each country.

### 5.8 Oil rents

- Nigeria had the highest average oil rents as a share of GDP at **10.82%**.
- Nigeria's oil rents reached **22.05% of GDP in 2000** and were **6.25% in 2021**.
- Kenya's oil rents were close to zero in the available observations.

Oil-rent data ends in 2021 in this dataset. Oil rents as a percentage of GDP are not the same as total oil revenue or the dollar value of oil exports.

## 6. Correlation analysis

Correlation coefficients describe the direction and strength of association. They do not show that one variable causes another.

### 6.1 Pooled Pearson correlations

| Indicator pair | Pearson r | Observations |
|---|---:|---:|
| GDP growth vs inflation | +0.063 | 130 |
| GDP growth vs unemployment | -0.408 | 130 |
| GDP per capita vs internet users | +0.564 | 125 |
| Population vs GDP per capita | -0.023 | 130 |
| Oil rents vs GDP growth | +0.310 | 110 |
| Exchange rate vs inflation | +0.283 | 130 |

Key observations:
- GDP growth and unemployment show a moderate negative pooled association (**r = -0.408**).
- GDP per capita and internet use show a positive pooled association (**r = +0.564**).
- GDP growth and inflation have a near-zero pooled linear correlation (**r = +0.063**).
- Population and GDP per capita have a near-zero pooled Pearson correlation (**r = -0.023**).

### 6.2 Country-level Pearson correlations

| Country | GDP growth–inflation | GDP growth–unemployment | GDPpc–internet | Population–GDPpc | Oil rents–GDP growth | Exchange rate–inflation |
|---|---:|---:|---:|---:|---:|---:|
| Egypt | +0.017 | -0.354 | +0.878 | +0.887 | +0.292 | +0.610 |
| Ghana | -0.371 | -0.224 | +0.814 | +0.962 | +0.403 | +0.126 |
| Kenya | -0.201 | +0.069 | +0.959 | +0.992 | +0.233 | -0.446 |
| Nigeria | -0.148 | -0.644 | +0.630 | +0.555 | +0.559 | +0.778 |
| South Africa | -0.048 | -0.395 | +0.420 | +0.442 | +0.560 | +0.032 |

The country-level results show that pooled relationships can conceal important differences. For example, the GDP growth–unemployment relationship is most negative in Nigeria (**r = -0.644**) and close to zero in Kenya (**r = +0.069**). The exchange-rate–inflation relationship is positive in Nigeria and Egypt but negative in Kenya.

Country-level coefficients are based on relatively small annual samples (generally 26 observations; fewer for indicators with missing years), so they should be treated as exploratory.

### 6.3 Annual-change correlations

The pooled correlation between annual GDP-per-capita percentage change and annual internet-use percentage change was **+0.137**, much weaker than the correlation between their levels (**+0.564**). This suggests that shared long-run upward trends may contribute to the stronger level correlation.

The pooled correlation between annual population percentage change and annual GDP-per-capita percentage change was **+0.138**, also weak.

The pooled correlation between annual exchange-rate percentage change and the inflation-rate level was **+0.601**. This comparison pairs an annual percentage change in the exchange rate with the inflation rate level; it is not a correlation between exchange-rate depreciation and a change in inflation itself.

### 6.4 Pearson and Spearman comparison

| Indicator pair | Pearson | Spearman | n |
|---|---:|---:|---:|
| GDP growth vs inflation | +0.063 | +0.174 | 130 |
| GDP growth vs unemployment | -0.408 | -0.401 | 130 |
| GDP per capita vs internet users | +0.564 | +0.736 | 125 |
| Population vs GDP per capita | -0.023 | +0.319 | 130 |
| Oil rents vs GDP growth | +0.310 | +0.251 | 110 |
| Exchange rate vs inflation | +0.283 | +0.042 | 130 |

The GDP growth–unemployment relationship is similar under both methods. The GDP-per-capita/internet-use association is stronger under Spearman, suggesting a stronger monotonic than strictly linear pattern in the pooled observations. The difference between Pearson and Spearman for exchange rate and inflation suggests that the linear association is sensitive to the shape and distribution of the observations.

## 7. Main insights

1. **Economic growth performance differs across the five economies.** Ghana has the strongest average growth in the selected period, while South Africa has the lowest.
2. **Growth has weakened in the later periods for Nigeria and South Africa.** Their average GDP growth rates are notably lower in 2014–2019 and 2020–2025 than in the earlier periods.
3. **High GDP per capita does not automatically imply low unemployment.** South Africa has the highest average GDP per capita in the group and also the highest average unemployment rate.
4. **Digital adoption and income levels are positively associated in the pooled observations.** However, annual changes show a much weaker association, so the level correlation should be interpreted in light of shared time trends.
5. **Nigeria's population scale is a major feature of the comparison.** Its population grew by more than 111 million between 2000 and 2025.
6. **Oil rents are more prominent in Nigeria's economy than in the other selected countries.** The available oil-rent data, however, ends in 2021.
7. **Inflation and exchange-rate relationships vary by country.** A single pooled coefficient does not adequately describe all five economies.

## 8. Dashboard design

The Power BI report contains four pages:

### Page 1 — African Economic Overview
Headline KPIs and country-level comparisons provide a quick view of the selected economies, with country and year slicers.

### Page 2 — Economic Growth & Inflation
Trend charts compare GDP growth and inflation over time. A scatterplot explores the GDP growth–inflation relationship, while a period comparison summarises average GDP growth across four time windows.

### Page 3 — Living Standards & Digital Development
Visuals compare GDP per capita, internet adoption and population patterns, including the relationship between internet use and GDP per capita.

### Page 4 — Labour Market, Oil & Currency
Visuals compare unemployment, oil rents and exchange-rate trends.

The `.pbix` file and screenshots should be included in the repository when publishing. This report describes the planned dashboard structure; the actual Power BI file is not included in this documentation package.

## 9. Limitations

- The analysis is descriptive and exploratory, not causal.
- The sample includes only five selected countries and should not be generalised to all African economies.
- Some indicators have shorter time coverage: internet use through 2024 and oil rents through 2021.
- Correlations can be influenced by shared time trends, outliers and differences between countries.
- Country-level correlation estimates use small samples.
- GDP per capita is in current US dollars and is affected by exchange rates and price levels.
- Exchange-rate levels are denominated in different national currencies.
- Unemployment estimates may have cross-country comparability limitations.
- World Bank historical observations may be revised.

## 10. Conclusion

The analysis highlights substantial differences in economic growth, inflation, income per capita, unemployment, population, digital adoption, oil rents and exchange-rate movements across Egypt, Ghana, Kenya, Nigeria and South Africa. The findings show why a multi-indicator approach is useful: no single metric captures the full economic and development picture of a country.

The Power BI dashboard turns the prepared dataset and analytical findings into an accessible visual report. Future work could extend the country sample, incorporate additional indicators, examine inflation-adjusted GDP per capita, test time-series relationships more rigorously and refresh the dataset as new World Bank observations become available.

## 11. Source and reproducibility notes

Source: World Bank, World Development Indicators (WDI).