#!/usr/bin/python3
"""
This is a python script that display
the content of a table in a database
using the sqlalchemy model.
=====================================
A script that lists all State objects
from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

from sqlalchemy import (create_engine)

if __name__ == "__main__":
    """
    creating engine using the ORM methods and creating session that
    retirves data from the states table
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating Session from sessionmaker method
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query database
    states = session.query(State).order_by(State.id).all()
    # Lopping throught result and Printing results
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
