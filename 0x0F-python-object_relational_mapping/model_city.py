#!/usr/bin/python3
""" Contains definition of a State and an instance """
""" Base = declarative_base() """


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


class City(Base):
    """ this class inherits from base """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
