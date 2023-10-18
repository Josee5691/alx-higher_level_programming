-- creating sub queries
USE hbtn_0d_usa;
-- main query
SELECT * FROM cities WHERE state_id = 
(
	-- subquery
	SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
