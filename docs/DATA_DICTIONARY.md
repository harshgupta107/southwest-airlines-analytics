# Data dictionary

## Sources and grain
Financials2024: one metric for the 2024 fiscal year per row. ExpenseComparison: one of six operating-expense categories per row with 2023/2024 values. BTS source and analytics.airport_month_operations: carrier-airport-year-month grain. MonthlyOperations / analytics.v_monthly_operations: one carrier-month row.

## Financial columns
| Field | Meaning |
|---|---|
| metric | operating_revenue, operating_expenses, operating_income or net_income |
| value_usd | Reported monetary value in USD; numeric, not display text |
| unit | USD |
| period_start / period_end | Fiscal duration boundaries |
| accession | SEC filing identifier; preserve as text including leading zeros |
| source_tags | XBRL extraction tag(s) |
| source_snapshot | Preserved companyfacts filename |
| category | Operating-expense category |
| expense_2023_usd / expense_2024_usd | Annual expense amount in USD |
| change_usd | 2024 minus 2023 expense |
| change_pct | 100 × change_usd / expense_2023_usd; already on a 0–100 percentage scale |

Operating margin = operating_income / operating_revenue. Power BI percentage measures return a fraction and receive percentage formatting. Source *_pct CSV fields already use percentage points; do not apply percentage formatting directly without scaling.

## BTS input fields
| Field | Meaning / unit |
|---|---|
| year, month | Calendar reporting period |
| carrier, carrier_name | Carrier identifier and name; WN in this project |
| airport, airport_name | Reporting arrival airport identifier and name |
| arr_flights | Total reported flights, including delayed/cancelled/diverted categories |
| arr_del15 | Arrivals delayed at least 15 minutes |
| arr_cancelled, arr_diverted | Cancelled and diverted flight counts |
| arr_delay | Total delay minutes represented by the delay-cause dataset |
| carrier_ct, weather_ct, nas_ct, security_ct, late_aircraft_ct | Attributed delay-cause flight counts; may be fractional |
| carrier_delay, weather_delay, nas_delay, security_delay, late_aircraft_delay | Minutes attributed to each cause |

Cause counts must not be rounded to integers. Missing airport-month source rows are not automatically zero flights. BLI, IAH and SYR September–December 2024 were reviewed as explained service exits.

## Monthly reporting columns and formulas
| Field | Formula / interpretation |
|---|---|
| period | First day of calendar month |
| airports_reporting | Distinct reporting airports in that month; do not sum over months |
| reported_flights | Sum arr_flights |
| delayed_arrivals | Sum arr_del15 |
| cancelled_flights / diverted_flights | Sum corresponding counts |
| delay_minutes / late_aircraft_minutes | Sum corresponding delay minutes |
| on_time_flights | reported_flights − delayed_arrivals − cancelled_flights − diverted_flights |
| cancellation_rate_pct | 100 × cancelled_flights / reported_flights |
| delayed_flight_share_pct | 100 × delayed_arrivals / reported_flights |
| on_time_flight_share_pct | 100 × on_time_flights / reported_flights |
| avg_delay_minutes_per_delayed_arrival | delay_minutes / delayed_arrivals |
| late_minutes_per_100_flights | 100 × late_aircraft_minutes / reported_flights |

Aggregate ratios from summed numerators and denominators, not arithmetic averages of monthly percentages. For zero denominators return missing/not applicable rather than an invented zero. On-time share uses all reported flights as its denominator, not completed arrivals only.

## Forecast output
period: target month. forecast_origin: historical cutoff. source_period: corresponding training month. seasonal_naive: prior-year monthly count. calendar_adjusted_seasonal: rounded prior-year daily rate × target-month days. Error = forecast minus actual, so positive bias is overforecasting. MAE and RMSE are in flights; MAPE and WAPE are percentages. WAPE = sum absolute errors / sum actuals × 100. Bias = sum signed errors / sum actuals × 100. No prediction intervals were estimated.

## Governance
Keep raw sources immutable, maintain hashes and filing/period filters, preserve validation failures, and distinguish reviewed text from pending candidates. Historical aggregate reconciliation cannot replace full row-level comparison or permissions testing.
