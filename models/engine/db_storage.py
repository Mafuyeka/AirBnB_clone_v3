# models/engine/db_storage.py

from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError
from os import getenv

class DBStorage:
    """This class manages storage using SQLAlchemy ORM."""

    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage."""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(getenv('HBNB_MYSQL_USER'),
                                             getenv('HBNB_MYSQL_PWD'),
                                             getenv('HBNB_MYSQL_HOST'),
                                             getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query all objects of a certain class."""
        obj_dict = {}
        classes = [cls] if cls else [BaseModel, User, State, City, Amenity, Place, Review]
        for cls in classes:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(obj.__class__.__name__, obj.id)
                obj_dict[key] = obj
        return obj_dict

    def new(self, obj):
        """Add object to current database session."""
        self.__session.add(obj)

    def save(self):
        """Commit all changes to current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete object from current database session."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Create all tables in the database."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Close the current session."""
        self.__session.close()

    def get(self, cls, id):
        """Retrieve one object based on class and id."""
        try:
            return self.__session.query(cls).filter_by(id=id).one()
        except NoResultFound:
            return None

    def count(self, cls=None):
        """Count the number of objects in storage."""
        if cls:
            return self.__session.query(cls).count()
        else:
            total_count = 0
            classes = [BaseModel, User, State, City, Amenity, Place, Review]
            for cls in classes:
                total_count += self.__session.query(cls).count()
            return total_count
