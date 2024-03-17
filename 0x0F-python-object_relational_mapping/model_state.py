#!/usr/bin/python3
""" Python file contains the class definition of a State and an
instance Base = declarative_base() """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ 
    Declaration of the State class inherited from Base

    Attributes:
    __tablename__: A string to store states.
    id: An integer to store states id.
    name: A string conataing states name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullabl=False)
