#!/usr/bin/python3
"""Definition of Rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing a new Rectangle"""
