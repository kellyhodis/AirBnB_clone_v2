#!/usr/bin/python3
''' This module defines the Amenity class.

    Attributes:
        Amenity - Subclass of BaseModel.
'''
from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Represent the amenities of an accommodation. '''
    name = ''
