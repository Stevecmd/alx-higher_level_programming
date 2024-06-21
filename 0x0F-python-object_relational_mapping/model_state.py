#!/usr/bin/python3
"""
Defines the State class and initializes
a connection to a MySQL database using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Initialize Base object using declarative_base()
Base = declarative_base()


class State(Base):
    """
    State class inherits from Base and links to the MySQL table states.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
