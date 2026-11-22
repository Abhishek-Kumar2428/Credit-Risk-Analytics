# Credit Risk Analytics Dashboard

## Project Overview

This project analyzes credit card customer data to identify patterns associated with payment default risk. It uses Power BI to build an interactive dashboard that helps explore customer demographics, credit limits, repayment behaviour, and default rates.

The project is based on the **Default of Credit Card Clients** dataset from the UCI Machine Learning Repository.

## Dataset

- **Source:** UCI Machine Learning Repository – Default of Credit Card Clients
- **Records:** 30,000 customers
- **Data period:** Historical Taiwan credit card data from 2005
- **Target variable:** `default_next_month` (1 = Default, 0 = No Default)

## Tools and Technologies

- Power BI Desktop
- Power Query
- DAX
- Python
- SQL
- CSV and SQLite

## Dashboard Features

- KPI cards showing total customers, defaulted customers, and default rate
- Customer default distribution
- Default rate by credit limit band
- Default rate by age group
- Default rate by September repayment status
- Summary table comparing customer segments
- Interactive slicers for age group and credit limit band

## Key Metrics

| Metric | Value |
|---|---:|
| Total Customers | 30,000 |
| Defaulted Customers | 6,636 |
| Non-Defaulted Customers | 23,364 |
| Overall Default Rate | 22.12% |

## Default Rate by Credit Limit Band

| Credit Limit Band | Default Rate |
|---|---:|
| 0–50K | 31.79% |
| 50K–100K | 25.80% |
| 100K–200K | 19.48% |
| 200K–500K | 14.80% |
| 500K+ | 11.17% |

## DAX Measures

**Total Customers**
```dax
Total Customers =
COUNTROWS(cleaned_credit_data)
```

**Defaulted Customers**
```dax
Defaulted Customers =
CALCULATE(
    COUNTROWS(cleaned_credit_data),
    cleaned_credit_data[default_next_month] = 1
)
```

**Default Rate**
```dax
Default Rate =
DIVIDE(
    SUM(cleaned_credit_data[default_next_month]),
    COUNTROWS(cleaned_credit_data),
    0
)
```

## Project Structure

```text
Credit-Risk-Analytics/
├── dashboard/
│   ├── Credit_Risk_Analytics.pbix
│   └── Credit_Risk_Analytics.pdf
├── data/
│   └── credit_card_default.csv
├── outputs/
│   ├── cleaned_credit_data.csv
│   └── credit_risk.db
├── scripts/
│   ├── clean_data.py
│   ├── inspect_data.py
│   └── load_database.py
├── sql/
│   └── analysis.sql
├── .gitignore
└── README.md
```

## How to Use

1. Clone or download this repository.
2. Open `dashboard/Credit_Risk_Analytics.pdf` to view the exported dashboard.
3. Open `dashboard/Credit_Risk_Analytics.pbix` in Power BI Desktop to explore the interactive report.
4. Use the cleaned dataset in `outputs/cleaned_credit_data.csv` for further analysis.

## Disclaimer

This project is intended for educational and portfolio purposes. The analysis is based on historical data and should not be used as the sole basis for real-world credit decisions.