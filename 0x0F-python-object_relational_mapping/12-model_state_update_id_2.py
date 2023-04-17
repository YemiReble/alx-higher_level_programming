#!/usr/bin/python3
"""
This python Script changes the value of a row
In a table from the recent value to another
=============================================
Write a script that changes the name of a State
object from the database hbtn_0e_6_usa.
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """
    Establishing connect to the database and creating
    a session that replace a data in a databese
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Creating Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Replacing Data
    states = session.query(State).filter(State.id == 2).first()
    states.name = "New Mexico"
    session.commit()
