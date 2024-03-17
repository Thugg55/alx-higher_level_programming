#!/usr/bin/python3

from sqlalchemy import Column, Foreignkey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Class for a city for the database"""
    """
    Attributes:
    id: The City's id
    name: The name of City
    State_id: The city's state id
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, Foreignkey("states.id"), nullable=False)
