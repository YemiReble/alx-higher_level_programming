#!/usr/bin/python3
"""
This is Python program that connects to MySQL
DataBase and Returns some dat. But in this case
this script will return all list of cities in
the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    INNER JOIN states ON cities.state_id=states.id ORDER BY cities.id ASC")
    db_cit = cur.fetchall()
    for row in db_cit:
        print(row)
