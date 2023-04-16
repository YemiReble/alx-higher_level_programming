#!/usr/bin/python3
"""
 A python file that contains the class definition of
 a State and an instance Base = declarative_base():
 State class:
 links to the MySQL table states
 class attribute id that represents a column of
 an auto-generated, unique integer, can’t be
 null and is a primary key
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()


class State(Base):

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Establishing connection to the local-host
    # engine = create_engine('mysql://localhost:3306')

    # Import all class that inherits from base
    # Base.metadata.create_all(engine)
