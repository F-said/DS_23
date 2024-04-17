SELECT state, SUM(rolling_average) AS tot_cases
FROM covid_case
GROUP BY state
ORDER BY tot_cases DESC;