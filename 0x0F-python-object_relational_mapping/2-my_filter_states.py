#!/usr/bin/python3
"""
This is a script that takes in an argument and search
such in the database for a matching data.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE BINARY '{}'\
        ORDER BY states.id ASC".format(argv[4]))
    bdb_rows = cur.fetchall()
    for row in bdb_rows:
        print(row)
