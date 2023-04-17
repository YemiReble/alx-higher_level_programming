#!/usr/bin/python3
"""
This is a python script that print all cities
in accorndance with their states.
==============================================
A Script that prints all City objects from the
database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    """
    Establishing connection to the database and
    creating sessions that list all cities in correspondence
    to the it State.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query: Listing all cities and the corresponding states
    output = session.query(City, State).join(State).order_by(City.id).all()
    for city, state in output:
        print('{}: ({}) {}'.format(state.name, city.id, city.name))
    session.commit()
