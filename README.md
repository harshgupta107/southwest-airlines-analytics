# Southwest Airlines Financial and Operational Analytics

Independent portfolio case study using real SEC disclosures and BTS domestic arrival statistics for 2023–2024. This project was not commissioned by Southwest Airlines.

## What this project demonstrates

- Python collection, cleaning and reconciliation of structured financial and operational data.
- Extraction and manual evidence review of management commentary from a Form 10-K.
- PostgreSQL ingestion, analytical SQL, a monthly reporting view, and tested backup recovery.
- Power BI operational and financial dashboards.
- Excel Power Query reporting and VBA refresh/reconciliation/PDF export.
- Historical forecast evaluation and an explicitly hypothetical expense-budget scenario.
- A repeatable checkpoint pipeline with saved validation evidence and input hashes.

## Main findings

| Metric | Result |
|---|---:|
| 2024 operating revenue | $27.483 billion |
| 2024 operating expenses | $27.162 billion |
| 2024 operating income | $321 million |
| 2024 operating margin | 1.17% |
| Operating expense increase from 2023 | $1.295 billion / 5.01% |
| Labor expense increase | $1.088 billion |
| Fuel expense decrease | $405 million |
| Average delay among delayed arrivals, 2023 → 2024 | 49.69 → 53.96 minutes |
| Calendar-adjusted seasonal benchmark, held-out 2024 WAPE | 4.52% |

BTS coverage comprises 2,556 airport-month records across 24 months and 107 airports. Financial disclosures cover company-wide activity; BTS results cover reported domestic arrivals. These populations are not interchangeable.

## Files

| Location | Purpose |
|---|---|
| `Southwest_Analytics_End_to_End.ipynb` | Annotated research notebook and final checkpoint-pipeline cell |
| `Southwest_Performance_Analytics.pbix` | Power BI report with operational and financial pages |
| `Southwest_Finance_Report.xlsm` | Excel report with embedded VBA and data connection |
| `Southwest_Finance_Report.xlsx` | Earlier workbook retained for completeness; use the `.xlsm` for macros |
| `data/raw/` | Source snapshots and provenance |
| `data/processed/` | Validated datasets and dashboard exports |
| `sql/` | Annual analysis and monthly reporting-view SQL |
| `backups/` | PostgreSQL archives |
| `reports/` | Charts, findings, forecasts, validation and pipeline-run evidence |
| `budget_scenario/` | Hypothetical planning scenario, code, inputs and outputs |
| `docs/` | Execution guidance, dictionary and completion checklist |
| `PUBLICATION_NOTES.md` | Publication changes, verification scope and remaining limitations |
| `FILE_MANIFEST.json` | SHA-256 hashes of the prepared project files |

Repeated timestamped runs and source snapshots are intentionally retained. Root-level CSV copies were also retained from the project folder.

## Running the project

1. Read [the execution guide](docs/EXECUTION_GUIDE.md). The notebook contains interactive stages and historical recovery cells; do not blindly run every cell in order.
2. Copy the repository contents into `MyDrive/southwest_analytics` and open the notebook in Google Colab. Mount Drive when requested.
3. For checkpoint reproduction, run the final cell headed `SOUTHWEST ANALYTICS — REPEATABLE CHECKPOINT PIPELINE`. It uses preserved inputs and an isolated PostgreSQL restore; it does not acquire new source data.
4. For source acquisition and analysis, follow the notebook stage guidance. SEC acquisition requests a contact user-agent, and BTS acquisition requires a downloaded source file.
5. Open the Power BI and Excel files in their desktop applications and repoint source paths to your local CSV files before refreshing.
6. See [budget scenario instructions](budget_scenario/BUDGET_SCENARIO.md) for the standalone scenario exercise.

The notebook uses pandas, NumPy, requests, matplotlib, Beautiful Soup, SQLAlchemy and PostgreSQL connectors. Installation/setup steps are in the notebook. Dependencies are not yet pinned; Colab setup and desktop refresh are environment-dependent.

## Validation and limitations

Two saved checkpoint runs passed 24-month comparisons across 13 SQL/Python metrics (312 comparisons) and reproduced forecast results. A separate restore test matched 2,556 records and 14 annual count/total checks. These checks do not establish field-by-field equality, production availability, or role-permission correctness. A fresh-runtime run was not independently verified.

The pipeline automates processing of saved checkpoints, not scheduled acquisition-to-dashboard refresh. The budget scenario is a planning exercise, not Southwest's official budget. Forecast evaluation covers only one held-out year using later data snapshots. Reviewed commentary is distinguished from pending evidence. No real stakeholder interviews, realized savings or causal financial impact are claimed.

## Sources

- [SEC Company Facts](https://data.sec.gov/api/xbrl/companyfacts/CIK0000092380.json), accession `0000092380-25-000024`.
- [BTS Airline On-Time Statistics and Delay Causes](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp), carrier `WN`, 2023–2024.

Source snapshots retain their original attribution. No license over third-party source material is asserted by this repository.
