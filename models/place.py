#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, Table, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship


if getenv('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60),
                                 ForeignKey('places.id'),
                                 primary_key=True,
                                 nullable=False),
                          Column('amenity_id', String(60),
                                 ForeignKey('amenities.id'),
                                 primary_key=True,
                                 nullable=False))


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night: price for a staying in int
        latitude: latitude in float
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'),
                     nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0,
                              nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0,
                            nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    amenity_ids = []

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity",
                                 secondary=place_amenity,
                                 viewonly=False)
    else:
        @property
        def reviews(self):
            """returns list of Review instances with place_id equal
            to current Place.id
            """
            from models import storage
            from models.review import Review
            objects = storage.all(Review)
            a_list = []
            for obj in objects:
                if obj.place_id == self.id:
                    a_list.append(obj)
            return a_list

        @property
        def amenities(self):
            """returns list of Amenity instances with amenity_id equal
            to current Place.id
            """
            from models import storage
            from models.amenity import Amenity
            a_list = []
            objects = storage.all(Amenity)
            for obj in objects:
                if obj.id in amenity_ids:
                    a_list.append(obj)
            return a_list

        @amenities.setter
        def amenities(self, obj):
            """handles append method for adding Amenity.id to attribute
            amenity_ids.
            """
            if type(obj).__name__ == "Amenity":
                self.amenity_ids.append(obj)
