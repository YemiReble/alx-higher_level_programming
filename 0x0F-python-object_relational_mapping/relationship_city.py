#!/usr/bin/python3
"""
A python program that create Cities Object
Accordingly
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """
    Declaring City Objects and Instances
    id (int) Being the Cities ID number
    name (str) Being the Cities Names
    state_id (int) Being the Corresponding Cities of a state
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
