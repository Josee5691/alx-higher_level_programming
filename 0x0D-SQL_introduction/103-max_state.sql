-- max temp
SELECT state, MAX(value) as max_temp GROUP BY state ORDER BY state;
