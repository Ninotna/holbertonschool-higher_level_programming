-- Select cities and their corresponding state names
-- The output should be ordered by the cities id
-- The states table has (id, name)
SELECT a.id, a.name, b.name
FROM cities as a
JOIN states as b ON a.state_id = b.id
ORDER BY a.id ASC;
