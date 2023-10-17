-- average temparature
SELECT city, AVG(value) AS avg_temp FROM temparatures GROUP BY city ORDER BY avg_temp DESC;
