-- Write a script that displays the top 3 of cities temperature during July and August ordered by temperature (descending)

SELECT UNIQUE(city), value
FROM temperatures
WHERE month IN (7,8)
ORDER BY value desc
LIMIT 3;