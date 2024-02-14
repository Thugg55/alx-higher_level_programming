-- Script lists the number of records with the same score.
-- in the second_table of the database hbtn_0c-0.

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score ORDER BY score DESC;
