#!/usr/bin/python3
"""
This module defines the State class.
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This class represents a state."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """Returns the list of City objects linked to the current State."""
        from models import storage
        city_objs = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_objs.append(city)
        return city_objs
