# Analyst budget scenario
This is a retrospective portfolio exercise, not Southwest's approved budget or guidance. No claim is made that it was prepared before 2024.

## Assumption and calculation
Hold each category's 2024 scenario budget equal to its 2023 actual expense (0% assumed growth). This neutral baseline demonstrates budget construction and variance reconciliation without inventing company planning data. It is a simple incremental budget, not a driver-based operating plan.

Budget = 2023 actual × (1 + assumed growth).
Variance = 2024 actual − scenario budget. Positive is above budget.
Total variance percentage uses total variance / total budget, not the average of category percentages.

## Verified result
- Scenario budget: $25,867,000,000.
- 2024 actual: $27,162,000,000.
- Above scenario budget: $1,295,000,000 (5.01%).
- Labor: $1,088,000,000 above; fuel: $405,000,000 below.
- Category totals reconcile to both reported annual totals.
Lower spending is not automatically operational improvement. Volume, prices and service levels are not separated here.

## Source
budget_source.csv contains only the category and annual-amount columns extracted from the project's validated source:
budget_source.csv
SEC filing accession 0000092380-25-000024. Original source is preserved.

## Reproduce in Colab
After mounting Drive, run:
```python
from pathlib import Path
import subprocess, sys
from datetime import datetime, timezone
base = Path("/content/drive/MyDrive/southwest_analytics/budget_scenario")
out = base / ("run_" + datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ"))
subprocess.run([sys.executable, str(base/"budget_scenario.py"),
               "--source", str(base/"budget_source.csv"),
               "--output", str(out), "--growth", "0"], check=True)
```
For sensitivity analysis change --growth to an explicitly labelled assumption, for example 0.03. That value is hypothetical, not sourced. Use a new output directory for every run. The runner rejects duplicate categories, invalid amounts, altered source totals and non-finite growth. Saved CSVs can be imported into Power BI or Excel; they have not been added to the existing PBIX/XLSM.

## Validation scope
The default scenario was executed locally and passed reconciliation. This does not validate a native Excel scenario model or create official budget-versus-actual performance reporting.

