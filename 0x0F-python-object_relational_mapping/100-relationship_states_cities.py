#!/usr/bin/python3
"""
A Python Script that creates State and
connect it id with the corresponding city.
"""

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import State, Base
from relationship_city import City


if __name__ == "__main__":
    """
    Create State and City
    create the State “California” with
    the City “San Francisco” from the
    database hbtn_0e_100_usa
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating Queries: State
    state_cal = State(name="California")

    # Creating Queries: City
    city_d = City(name="San Francisco")
    state_cal.cities.append(city_d)

    session.add(state_cal)
    session.commit()
