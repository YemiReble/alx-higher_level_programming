-- This is a script that updates the score of Bob to 10 in the table second_table
-- Usin Bob’s name field
-- The database name will be passed as an argument of the mysql command

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
