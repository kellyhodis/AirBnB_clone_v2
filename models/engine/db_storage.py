#!/usr/bin/python3
"""This is the database storage class for AirBnB"""
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage:
    """This class stores instances in tables and
    converts tables to instances
    Attributes:
        __engine: connection to mysql db
        __session: sqlalchemy mysql session
    """
    __engine = None
    __session = None

    def __init__(self):
        """connects to the database with
        user, password, host, and database retrieved from
        environment variables
        dialect: mysql
        driver: mysqldb
        """
        # Get environment variables and store them
        user = getenv('HBNB_MYSQL_USER')
        password = getenv('HBNB_MYSQL_PWD')
        host = getenv('HBNB_MYSQL_HOST')
        database = getenv('HBNB_MYSQL_DB')

        sql = "mysql+mysqldb://{}:{}@{}/{}".format(user, password,
                                                   host, database)
        self.__engine = create_engine(sql, pool_pre_ping=True)

        if getenv('HBNB_ENV') is not None and getenv('HBNB_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query on the current database
        Return:
            returns a dictionary of object
        """
        a_d = {}
        if cls:
            objects = self.__session.query(cls).all()
        else:
            objects = self.__session.query(City).all()
            objects += self.__session.query(State).all()
            objects += self.__session.query(User).all()
            objects += self.__session.query(Place).all()
            objects += self.__session.query(Review).all()
            objects += self.__session.query(Amenity).all()
        for obj in objects:
            key = type(obj).__name__ + "." + obj.id
            a_d[key] = obj
        return a_d

    def new(self, obj):
        """adds obj to __session
        Args:
            obj: given object
        """
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit changes to __session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """delete object from __session if it's inside
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """serialize the file path to JSON file path
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
