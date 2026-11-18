CREATE OR REPLACE VIEW analytics.v_monthly_operations AS
WITH monthly_totals AS (
    SELECT
        carrier,
        MAKE_DATE(year, month, 1) AS period,
        COUNT(DISTINCT airport) AS airports_reporting,
        SUM(arr_flights) AS reported_flights,
        SUM(arr_del15) AS delayed_arrivals,
        SUM(arr_cancelled) AS cancelled_flights,
        SUM(arr_diverted) AS diverted_flights,
        SUM(arr_delay) AS delay_minutes,
        SUM(late_aircraft_delay) AS late_aircraft_minutes
    FROM analytics.airport_month_operations
    GROUP BY carrier, year, month
)
SELECT
    *,
    reported_flights
        - delayed_arrivals
        - cancelled_flights
        - diverted_flights AS on_time_flights,

    100.0 * cancelled_flights
        / NULLIF(reported_flights, 0)
        AS cancellation_rate_pct,

    100.0 * delayed_arrivals
        / NULLIF(reported_flights, 0)
        AS delayed_flight_share_pct,

    100.0 * (
        reported_flights
        - delayed_arrivals
        - cancelled_flights
        - diverted_flights
    ) / NULLIF(reported_flights, 0)
        AS on_time_flight_share_pct,

    1.0 * delay_minutes
        / NULLIF(delayed_arrivals, 0)
        AS avg_delay_minutes_per_delayed_arrival,

    100.0 * late_aircraft_minutes
        / NULLIF(reported_flights, 0)
        AS late_minutes_per_100_flights

FROM monthly_totals;