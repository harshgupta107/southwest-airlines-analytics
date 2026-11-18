# Execution guide

## Prerequisites
Use Colab with Google Drive access, the project folder and preserved BTS input. SEC acquisition prompts for a contact email. Keep credentials out of shared outputs. PostgreSQL setup installs packages and creates a local database role. The database lives in the temporary Colab runtime; Drive backups persist.

## Cell numbering
The labels S01–S27 added above code cells identify original saved code positions. Inline comments such as CELL 3 predate the recovery cell and do not equal notebook positions. Documentation cells do not change these labels.

## Fresh acquisition route
Skip S01, which requires existing checkpoints. Run S02 setup, S03 SEC acquisition, S04 financial validation, S05 expense breakdown, S06 annual comparison, S07 filing text extraction, S08 reviewed findings, S09 BTS upload, S10 BTS validation, S11 coverage/KPIs, S12 cause analysis, S13 airport analysis. Stop at any failed validation.

S08 contains reviewed findings tied to existing passages; do not label new passages reviewed automatically. S09 requires an official BTS ZIP or CSV upload, not a generated dataset. All new runs must retain source provenance.

## Existing-checkpoint route
Run S01 to restore the pinned validated BTS checkpoint and constants. It does not restore every financial variable or PostgreSQL. Run S13 for the checkpoint-based airport analysis, or S14–S17 for SQL setup/loading/reporting. S12 needs the dependent validated state described in its code; S01 alone is not a universal recovery cell.

## SQL and reporting
S14 installs/starts PostgreSQL and configures credentials. S15 loads the pinned BTS CSV and creates a backup. S16 runs annual SQL validation. S17 creates the monthly view and dashboard export. S18–S21 are optional download/mount/inspection helpers.

Important: S15 explicitly pins BTS run 20261113T180223779285Z. Fresh acquisition can create a newer run, but SQL loading will still use this historical checkpoint until configured. Do not claim that a fresh BTS upload automatically flows through every downstream step.

## Forecast evaluation
S22 inspects the monthly export. S23 validates it, freezes forecasts using 2023, and evaluates 2024. It uses a pinned monthly export. Outputs are timestamped. Keep test-year evaluation separate from future tuning and do not call these forecasts official budgets.

## Recovery testing
S24 checks the backup and installed PostgreSQL. S25 restores the pinned backup into a newly named isolated test database and compares annual totals. S26 recreates the monthly view and compares dashboard values.

S26 currently hardcodes southwest_restore_20261115t184531406040z and its report directory. Before a NEW recovery test, set TEST_DB to the test_db created by S25 and REPORT_DIR to S25's report_dir. Otherwise it targets the previous test database. The historical test passed; automatic chaining still needs implementation.

S27 lists saved project artifacts. Do not use Run all blindly: recovery comes first physically, uploads require input, and several later cells pin prior run IDs.

## Desktop deliverables
Power BI uses exported CSVs, not a live connection to Colab's localhost. Preserve table names MonthlyOperations, Financials2024 and ExpenseComparison when refreshing. Financial cards cover 2024; expense comparisons cover both years. Excel needs the local CSV path configured in Power Query and an .xlsm file saved to a local filesystem path for the supplied VBA export.

## Verification and restart
After a Colab reset, remount Drive and reinstall/start PostgreSQL as needed. Preserve existing archives. Use a separate database for restore tests. Do not delete backups or rewrite raw data to get checks to pass. Save validation manifests alongside each run. A reproducible release still needs a clean-runtime test with captured dependency versions and explicit input configuration.
