# Oil Central Lab: Power BI Dashboards

[النسخة العربية](README_ar.md)

A four-page Power BI report analysing laboratory sample operations, finance, legal referrals and turnaround time for an oil-sector central laboratory.

> **Data notice:** All data in this project is synthetic and was generated for demonstration purposes. It does not represent any real customer, company or transaction.

## Report Pages

| # | Page | What it answers |
|---|------|-----------------|
| 1 | **Sample Overview** | How many cases and sample units were received, by customer type, laboratory, year and sample type? |
| 2 | **Finance** | How much was invoiced, paid and is still outstanding? What is the collection rate and the share of each payment method? |
| 3 | **Report Status & Legal Referrals** | How are reports distributed by status, and how many cases were referred to legal administration and for what value? |
| 4 | **Results Dashboard** | What is the average delay, how often do delays happen, and what are the main delay reasons? |

Screenshots are in the [`screenshots/`](screenshots/) folder.

## Key Definitions

| Term | Meaning | Value |
|------|---------|-------|
| **Case** | One Sample ID (one row in `public results`) | 2,000 |
| **Sample Unit** | An individual lab sample. A single Sample ID may contain several units | 3,209 |
| **Legal Case** | A case referred to Legal Administration | 10 (containing 13 sample units) |
| **Legal Transfer Value** | Sum of `sample_price_before_vat` for legal cases (before VAT) | SAR 17,919.50 |

## Headline Figures

- Total invoiced: SAR 4,829,103.35
- Total paid: SAR 3,831,200.97
- Total outstanding: SAR 997,902.38
- Collection rate: 79.34%
- Average delay (all samples): 1.34 days
- Average delay (delayed samples only): 7.61 days
- Share of delayed samples: 17.65%

## Data Model

Three tables:

- `public samples`: sample details, customer type, laboratory, quantity and price
- `public results`: report status, legal status, delay days and delay reason
- `public finance`: invoices, payments, payment method and outstanding amounts

## Notes and Limitations

- 2026 data is partial (through October), so the last point in *Sample Units by Year* is not a full-year figure.
- Chart titles state whether they count **cases** (Sample IDs) or **sample units**; the two are not interchangeable.
- The legal transfer value is calculated **before VAT**.

## Tools

- Power BI Desktop
- DAX (see [`measures.md`](measures.md))

## How to Open

1. Install [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (Windows).
2. Download `Oil_Central_Lab.pbix` from this repository.
3. Open the file. The data is embedded, so no gateway or refresh is needed.
