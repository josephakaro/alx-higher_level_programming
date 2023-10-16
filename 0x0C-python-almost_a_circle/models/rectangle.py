#!/usr/bin/python3
"""
    Rectangle Class
"""

from models.base import Base


class Rectangle(Base):
    """ Class Rectangle inherit from Base Class """
    def __init__(self, id=None):
        super().__init__(id)