-- This Script Removes all the data that are less than 5
-- remove all records with a score <= 5 in the table
-- second_table of the database hbtn_0c_0 on my MySQL server.

DELETE FROM second_table
WHERE score <= 5;
