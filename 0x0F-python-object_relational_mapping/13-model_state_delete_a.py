#!/usr/bin/python3
"""
This is a python script that delete all vaule of
a table where 'a' apears atleast ones.
========================================================
a script that deletes all State objects with a name
containing the letter a from the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Establishing connection to the database and
    creating session that remove any data that has
    letter a in them.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Removing Data
    states = session.query(State).filter(State.name.like(
        '%a%')).order_by(State.id).all()
    for state in states:
        session.delete(state)
    session.commit()
