#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import InvalidRequestError
from sqlalchemy.orm.exc import NoResultFound

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """
        Adds a new user to the database.

        Args:
            email (str): The email of the user.
            hashed_password (str): The hashed password of the user.

        Returns:
            User: The newly created user object.
        """
        new_user = User(email=email, hashed_password=hashed_password)
        self._session.add(new_user)
        self._session.commit()
        return new_user

    def find_user_by(self, **kwargs) -> User:
        """
        Finds a user in the database using provided keyword arguments.
        Args:
            **kwargs: Arbitrary keyword arguments for filtering
                            the users table.
        Returns:
            User: The first user object that matches the filtering criteria.
        Raises:
            NoResultsFound: When no results are found.
            InvalidRequestError: When wrong query arguments are passed.
        """
        if not kwargs:
            raise InvalidRequestError

        users_columns = [
            'id',
            'email',
            'hashed_password',
            'session_id',
            'reset_token'
            ]

        for arg in kwargs:
            if arg not in users_columns:
                raise InvalidRequestError

        """ Search table for user """

        search_user = self._session.query(User).filter_by(**kwargs).first()

        if search_user:
            return search_user
        else:
            raise NoResultFound
