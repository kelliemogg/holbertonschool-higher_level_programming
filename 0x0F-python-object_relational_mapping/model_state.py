#!/usr/bin/python3
""" Contains definition of a State """


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """ State inherits from Base """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, unique=True)
    name = Column(String(128), nullable=False)
