#!/usr/bin/python3
"""City Module for HBNB project."""

from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel,Base):
    """Class representing a City.

    Attributes:
>>City inherits from BaseModel and Base
>>__tablename__ -represents the table name, cities
>> name -representing a string column of maximum 128 characters
>>state_id - representing a string column of maximum 60 characters

    """

    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
