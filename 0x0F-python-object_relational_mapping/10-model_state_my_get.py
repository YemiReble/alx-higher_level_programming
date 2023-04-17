#!/usr/bin/python3
"""
This is a script that prints Table Object
and takes the data as the forth argument
========================================
A script that prints the State object with
the name passed as argument from the
database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Establishing connection to the localhost and
    and creating a session that handles the queries
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating function that Fetch Data
    def fetch_date(name):
        state = session.query(State).filter(State.name == name).first()
        return state

    # Calling Function and printing data
    data = fetch_date(argv[4])
    if data is not None:
        print('{}'.format(data.id))
    else:
        print("Not found")
