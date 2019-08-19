#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    # DBStorage class attribute
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state")
    # FileStorage getter attribute
    else:
        @property
        def cities(self):
            """returns list of City instances with state_id matching the
            current State id
            """
            objects = models.storage.all(City)
            a_list = []
            for obj in objects:
                if obj.state_id == self.id:
                    a_list.append(obj)
            return a_list
