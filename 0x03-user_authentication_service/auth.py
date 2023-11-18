#!/usr/bin/env python3
""""Module contain authorization variables"""

import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> str:
    """Takes in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    pswrd = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pswrd, salt)

    return hashed_password

class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def _hash_password(self, password: str) -> str:
        """Takes in a password string arguments and returns bytes.
        The returned bytes is a salted hash of the input password,
        hashed with bcrypt.hashpw
        """
        pswrd = password.encode()
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(pswrd, salt)

        return hashed_password.decode()

    def register_user(self, email: str, password:str ) -> User:
        """Take mandatory email and password
        string arguments and return a User object.
        If a user already exist with the passed
        email, raise a ValueError with the message
        User <user's email> already exists. If not,
        hash the password with _hash_password, save
        the user to the database using self._db and
        return the User object.
        """
        try:
            find_user = self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists.")
        except NoResultFound:
            pw = self._hash_password(password)
            self._db.add_user(email, pw)

