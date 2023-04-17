#!/usr/bin/python3
"""
This is a script that print all data in
a table that has at least one leter 'a'
in them.
==========================================
A script that lists all State objects that
contain the letter a from the database
hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Creating and establiching connection to hbtn_0e_6_usa
    database to collect dat that contain letter a
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: Fetching data
    states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()
    for state in states:
        print('{}: {}'.format(state.id, state.name))
