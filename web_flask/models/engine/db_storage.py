#!/usr/bin/python3
"""Definition for database storage"""
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import models
from models.base_model import BaseModel, Base
from models.user import User
from models.job import Job
from models.application import Application


classes = {"User": User, "Application": Application, "Job": Job}


class DBStorage:
    """DB class definition"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        MYSQL_USER = "jc_user"
        MYSQL_PWD = "root"
        MYSQL_HOST = "localhost"
        MYSQL_DB = "jc_db"
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(MYSQL_USER,
                                             MYSQL_PWD,
                                             MYSQL_HOST,
                                             MYSQL_DB))
   
    def all(self, cls=None):
        """returns a dictionary
        Return:
            returns a dictionary of __object
        """
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            lista = [Job, Application, User]
            for clase in lista:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)
    
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def new(self, obj):
        """add the object to the current database session"""
        if isinstance(obj, User):
        # Ensure that first_name and last_name are not None
            if obj.first_name is not None and obj.last_name is not None:
                self.__session.add(obj)
            else:
            # Handle the case where first_name or last_name is None
                raise ValueError("Both first_name and last_name must be provided for a new User.")
        else:
            self.__session.add(obj)

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()
    
    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None
    
    def get_email(self, cls, email):
        """
        Returns the object based on the email
        None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.email == email):
                return value
        return None
    
    def get_username(self, cls, username):
        """
        Returns the object based on the username or
        None if not found
        """
        if cls not in classes.values():
            return None
        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.username == username):
                return value
        return None
    
    # def search(self, cls=None, keyword=None):
    #     """Search based on keyword"""
    #     if cls not in classes.values():
    #         return None
    #     dic = {}
    #     if keyword:
    #         all_cls = models.storage.all(cls)
    #         if keyword.lower() in ["partime", "fulltime"]:
    #             for value in all_cls.values():
    #                 if (value.type == keyword):
    #                     key = "{}.{}".format(type(value).__name__, value.id)
    #                     dic[key] = value
    #             return (dic)
    #         for value in all_cls.values():
    #             if keyword.lower() in value.title.lower():
    #                 key = "{}.{}".format(type(value).__name__, value.id)
    #                 dic[key] = value
    #     return (dic)
    def search(self, cls=None, keyword=None):
        """Search for instances of the given class based on a keyword.

        Args:
            cls (class): The class to search for instances.
            keyword (str): The keyword to search for.

        Returns:
            dict: A dictionary containing instances that match the search criteria.
        """
        if not cls or cls not in classes.values() or not keyword or not isinstance(keyword, str):
            return None

        result_dict = {}

        all_instances = models.storage.all(cls)

        if keyword.lower() in ["partime", "fulltime"]:
            for instance in all_instances.values():
                if instance.type.lower() == keyword.lower():
                    key = f"{type(instance).__name__}.{instance.id}"
                    result_dict[key] = instance
        else:
            for instance in all_instances.values():
                if keyword.lower() in instance.title.lower():
                    key = f"{type(instance).__name__}.{instance.id}"
                    result_dict[key] = instance

        return result_dict

        