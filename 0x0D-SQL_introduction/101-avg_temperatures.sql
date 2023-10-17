-- average temparature
SELECT city, AVG(value) AS avg_temparature FROM temparatures GROUP BY city ORDER BY avg_temparature DESC;
