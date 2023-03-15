-- This Script Creates a New Table in my database
-- Consisting of 3 columns
-- with the following data descriptions:
--      id INT
--      name VARCHAR(256)
--      score INT

CREATE TABLE IF NOT EXISTS second_table (id INT, name 
    VARCHAR(256), 
    score INT
);

INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex',3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'Goerge', 8);
