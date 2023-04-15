#!/usr/bin/python3
"""
This is a script that takes in 4 arguments and search
for the forth arguments' input in the database for a
matching data.

In regargs to the privious code which was vulnurabel to
attackers and Injection. This is the amended and optimised
code/software
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY %(name)s\
        ORDER BY states.id ASC",{'name':argv[4]})
    bdb_rows = cur.fetchall()
    for row in bdb_rows:
        print(row)
