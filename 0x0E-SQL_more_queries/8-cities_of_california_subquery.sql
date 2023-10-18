-- creating sub queries
SELECT * FROM cities WHERE state_id = ( 
	--subquery
	SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
