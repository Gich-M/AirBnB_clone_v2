#!/usr/bin/python3
""""New sqlalchemy class."""
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv


class DBStorage:
    """This class manages storage of hbnb models in JSON format"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv("HBNB_MYSQL_USER")
        passwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, db),
                                      pool_pre_ping=True)

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        dicn = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            query = self.__session.query(cls)
            for obj in query:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                dicn[key] = obj
        else:
            listc = [State, City, User, Place, Review, Amenity]
            for clss in listc:
                query = self.__session.query(clss)
                for obj in query:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    dicn[key] = obj
        return (dicn)

    def new(self, obj):
        """Adds new object to storage dictionary"""
        self.__session.add(obj)

    def save(self):
        """Saves storage dictionary to file"""
        self.__session.commit()

    def delete(self, obj=None):
        """ delete an existing element in the table
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Loads storage dictionary from file"""
        Base.metadata.drop_all(self.__engine)
        sess = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(sess)

    def close(self):
        """ calls reload()
        """
        self.__session.close()
