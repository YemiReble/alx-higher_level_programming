-- This script lists all records with a score >= 10 in 
-- the Table "second_table" of the database hbtn_0c_0
-- on my MySQL server
-- Results will display both the score and the name
-- Records will be ordered by score (top first)
-- The database name will be passed as an argument of the mysql command

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
