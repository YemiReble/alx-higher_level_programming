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
from relationship_city import City
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    """
    Class - Table Attributes:
    id: (int)   Takes in or count the table row
    name: (str) A column that takes In the names
                of states in the table.
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
