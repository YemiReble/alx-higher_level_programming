#!/usr/bin/python3
"""
This is a python script that add a Data to
a Table in a DataBase.
==========================================
Write a script that adds the State object
“Louisiana” to the database hbtn_0e_6_usa
"""


from sys import argv
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__name__":
    """
    Establishing connection to databese and creating
    a connection session to create new data.
    """

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    # Create Session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Creating New State
    new_state = State(name="Louisiana")
    # Adding the New State and commition the transaction
    session.add(new_state)
    session.commit()
    print('{}'.format(new_state.id))
    session.close()
