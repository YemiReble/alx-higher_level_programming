#!/usr/bin/python3
"""
A Script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa.

This script takes 4 Arguments.
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    db = MySQLdb.connect(
        host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities JOIN states ON\
        cities.state_id=states.id WHERE states.name LIKE BINARY\
        %(states_name)s ORDER BY cities.id ASC", {'state_name': argv[4]})
    new_var = cur.fetchall()
    for row in new_var:
        print(row)