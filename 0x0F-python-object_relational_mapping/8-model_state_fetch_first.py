#!/usr/bin/python3
"""
This is a python script that prints
the first data in an SQL Table.
=====================================
A script that prints the first State
object from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Creating the session that request the first
    data of a table from Sql database
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).first()
    if states is not None:
        print("{}: {}".format(states.id, states.name))
    else:
        print("Nothing")
