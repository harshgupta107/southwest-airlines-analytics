"""Retrospective analyst scenario, NOT an official Southwest budget.
Run: python budget_scenario.py --source expense_comparison.csv --output results
Optional --growth 0.03 applies an explicitly assumed uniform 3% increase.
No 2024 actual is used to calculate the scenario budget.
"""
import argparse
import csv
import hashlib
import json
from decimal import Decimal, ROUND_HALF_UP
from pathlib import Path

def run(source, output, growth):
    if not growth.is_finite() or growth <= -1:
        raise ValueError('Growth must be finite and greater than -100%.')
    with source.open(encoding='utf-8-sig', newline='') as f:
        rows = list(csv.DictReader(f))
    if len(rows) != 6 or len({r['category'] for r in rows}) != 6:
        raise ValueError('Expected six unique categories.')
    result = []
    for row in rows:
        prior, actual = (Decimal(row[c]) for c in ['expense_2023_usd','expense_2024_usd'])
        if not all(v.is_finite() and v > 0 and v == v.to_integral_value() for v in [prior, actual]):
            raise ValueError('Source actuals must be positive whole USD amounts.')
        budget = (prior * (1 + growth)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)
        if budget <= 0:
            raise ValueError('Rounded budget must be positive.')
        variance = actual - budget
        result.append(dict(category=row['category'], actual_2023_usd=str(prior), assumed_growth_fraction=str(growth), scenario_budget_2024_usd=str(budget), actual_2024_usd=str(actual), actual_minus_budget_usd=str(variance), variance_pct=str(variance / budget * 100), assessment='Above scenario budget' if variance > 0 else 'Below scenario budget' if variance < 0 else 'On scenario budget'))
    prior_total = sum(Decimal(r['actual_2023_usd']) for r in result)
    actual_total = sum(Decimal(r['actual_2024_usd']) for r in result)
    if prior_total != 25867000000 or actual_total != 27162000000:
        raise ValueError('Annual source controls failed.')
    budget_total = sum(Decimal(r['scenario_budget_2024_usd']) for r in result)
    variance_total = sum(Decimal(r['actual_minus_budget_usd']) for r in result)
    if variance_total != actual_total - budget_total:
        raise ValueError('Variance reconciliation failed.')
    output.mkdir(parents=True, exist_ok=False)
    with (output/'budget_vs_actual.csv').open('w',newline='',encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=list(result[0]))
        writer.writeheader(); writer.writerows(result)
    summary = dict(label='Retrospective analyst budget scenario; not official guidance', baseline_year=2023, target_year=2024, assumed_growth_fraction=str(growth), scenario_budget_usd=str(budget_total), actual_usd=str(actual_total), actual_minus_budget_usd=str(variance_total), variance_pct=str(variance_total/budget_total*100), source_file=source.name, source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(), status='PASS', limitation='Cost variance alone does not establish efficiency, performance or savings; no volume/price decomposition.')
    (output/'scenario_summary.json').write_text(json.dumps(summary,indent=2),encoding='utf-8')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    p.add_argument('--growth',type=Decimal,default=Decimal('0'))
    a=p.parse_args(); run(a.source,a.output,a.growth)
