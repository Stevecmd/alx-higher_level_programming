-- List all records from second_table with non-empty name value
SELECT `score`, `name`
FROM `second_table`
WHERE `name` IS NOT NULL AND name != ''
ORDER BY `score` DESC;
