# Completion and evidence checklist

Status is based on inspected saved notebook content and results shared during development, not a new independent execution of all stages.

## Demonstrated
- [x] SEC and BTS source acquisition and preserved snapshots.
- [x] Financial totals and accounting-identity reconciliation.
- [x] BTS coverage, numerical, key and cause reconciliation checks.
- [x] Financial cost comparison and operational delay analysis.
- [x] Selected management commentary reviewed; other passages remain pending.
- [x] PostgreSQL load and analytical SQL; monthly reporting view.
- [x] Power BI operational and financial visuals observed in screenshots.
- [x] 2024 holdout forecast benchmark, accuracy output and manifests.
- [x] Excel summary formulas, Power Query import and successful VBA PDF export observed.
- [x] Test database restoration: 2,556 rows and 14 annual checks.
- [x] Monthly view recreation: 24 months × 13 metrics matched.
- [x] Saved notebook located in the original project folder.

## Prepared in this documentation pass
- [x] Execution guide and stage labels added without changing code or historical outputs.
- [x] README, data dictionary and this checklist.
- [x] Pinned-run and hardcoded recovery-target limitations identified.

## Remaining before a reproducible release
- [ ] Centralize paths, run IDs and input manifest; remove unintended cross-run dependencies.
- [ ] Implement and test a single pipeline entry point with clear manual acquisition boundaries.
- [ ] Capture and pin Python/package and PostgreSQL environment versions.
- [ ] Run from a clean runtime and save a complete successful run log.
- [ ] Test failure paths: missing source, altered totals, cancelled refresh and failed SQL execution.
- [ ] Review remaining management commentary or explicitly exclude it from published claims.
- [ ] Collect current .pbix, .xlsm, exported PDF and VBA source in the deliverable folder.
- [ ] Audit PBIX measures, filter behavior, scope labels and refresh paths from the actual file.
- [ ] Verify VBA code against the final workbook, including failure paths and repeat runs.
- [ ] Reconcile full restored table fields if claiming complete row-level recovery.
- [ ] Test role/permission restoration separately if claiming access-control recovery.
- [ ] Build a clearly labelled assumption-based budget scenario if budgeting remains in scope.
- [ ] Document stakeholder requirements as a simulated brief unless real engagement occurs.
- [ ] Review credentials, personal information and raw-data redistribution terms before publication.

Do not claim production scheduling, live company collaboration, verified savings, official budgets or a fully automated end-to-end pipeline at this stage.


## Status update — 18 November 2026
This update supersedes earlier statements that a budget exercise or checkpoint pipeline has not been created.
- Added budget_scenario/: runnable Python incremental-budget scenario, source subset, category variance CSV, summary and assumptions guide. Default is explicitly hypothetical zero growth on 2023 actual costs; 2024 actuals are comparison outcomes. Local execution passed annual controls and variance reconciliation.
- Two user-executed checkpoint pipeline runs passed: 20261116T164337507684Z and 20261116T164538836965Z, each with 312 monthly SQL/Python comparisons and reproduced forecast scores. A fresh operating-system runtime was not independently verified. The pipeline restores saved data/backup; it does not automate acquisition through fresh SQL ingestion.
- Desktop files collected in Drive: Southwest_Finance_Report.xlsm and Southwest_Performance_Analytics.pbix. File inspection confirmed Excel formulas/cached totals, tblExpenses, data connection and embedded VBA; Power BI contains two pages with cards/charts. Live macro and Power BI refresh were not rerun by the assistant. The PDF was inspected from the chat upload; all three printed reconciliations passed.
- Power BI page labels remain Page 1 and Page 2. An additional expense-change chart is optional.
- Still open: full acquisition-to-report orchestration, pinned dependencies, clean-runtime evidence, failure-path testing, remaining commentary review and native desktop refresh testing. Advanced Excel coverage remains limited; a Python scenario does not establish advanced Excel modeling skills. No real stakeholder collaboration or production access-control verification is claimed.

