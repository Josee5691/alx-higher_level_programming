-- display top 3 cities
SELECT city, AVG(value) as avg_temp from temperatures WHERE month in (7, 8) GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
