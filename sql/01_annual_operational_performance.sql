WITH annual_totals AS (
    SELECT
        year,
        SUM(arr_flights) AS reported_flights,
        SUM(arr_del15) AS delayed_arrivals,
        SUM(arr_cancelled) AS cancelled_flights,
        SUM(arr_diverted) AS diverted_flights,
        SUM(arr_delay) AS delay_minutes
    FROM analytics.airport_month_operations
    WHERE carrier = 'WN'
      AND year IN (2023, 2024)
    GROUP BY year
),
annual_rates AS (
    SELECT
        *,
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
            AS avg_delay_minutes_per_delayed_arrival

    FROM annual_totals
)
SELECT
    *,
    cancellation_rate_pct
        - LAG(cancellation_rate_pct) OVER (ORDER BY year)
        AS cancellation_change_pp,

    delayed_flight_share_pct
        - LAG(delayed_flight_share_pct) OVER (ORDER BY year)
        AS delayed_share_change_pp,

    on_time_flight_share_pct
        - LAG(on_time_flight_share_pct) OVER (ORDER BY year)
        AS on_time_share_change_pp,

    avg_delay_minutes_per_delayed_arrival
        - LAG(avg_delay_minutes_per_delayed_arrival)
            OVER (ORDER BY year)
        AS average_delay_change_minutes

FROM annual_rates
ORDER BY year;