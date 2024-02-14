-- Script lists all records of the second_table of htbn_0c_0 database.
-- Script don't list rows without a name value.
-- records are listed by descending score.

SELECT score, name FROM second_table
WHERE name != "" ORDER BY score DESC;
