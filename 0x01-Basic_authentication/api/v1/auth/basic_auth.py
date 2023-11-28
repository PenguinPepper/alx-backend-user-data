#!/usr/bin/env python3
"""Module contains the class BasicAuth"""
from api.v1.auth.auth import Auth
import base64
import binascii
from typing import TypeVar
from models.user import User


class BasicAuth(Auth):
    """Class inherits from Auth
    """
    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """
        returns the Base64 part of the
        Authorization header for a Basic Authentication:
        Return None if authorization_header is None
        Return None if authorization_header is not a string
        Return None if authorization_header doesn’t
        start by Basic (with a space at the end)
        Otherwise, return the value after Basic (after the space)
        You can assume authorization_header contains only one Basic
        """
        if authorization_header is None:
            return None
        try:
            arr = authorization_header.split()
            if 'Basic' not in arr:
                return None
            return arr[1]
        except AttributeError:
            return None

    def decode_base64_authorization_header(self, base64_authorization_header:
                                           str) -> str:
        """
        returns the decoded value of a Base64
        string base64_authorization_header:
        Return None if base64_authorization_header is None
        Return None if base64_authorization_header is not a string
        Return None if base64_authorization_header
        is not a valid Base64 - you can use try/except
        Otherwise, return the decoded value as
        UTF8 string - you can use decode('utf-8')
        """
        if (base64_authorization_header is None or
           isinstance(base64_authorization_header, str) is False):
            return None
        else:
            try:
                decoded_value = base64.b64decode(base64_authorization_header)\
                        .decode('utf-8')
                return decoded_value
            except binascii.Error as e:
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header:
                                 str) -> (str, str):
        """
        returns the user email and password from the Base64 decoded value.
        This method must return 2 values
        Return None, None if decoded_base64_authorization_header is None
        Return None, None if:
         decoded_base64_authorization_header is not a string
         decoded_base64_authorization_header doesn’t contain :
        Otherwise, return the user email and the user
        password - these 2 values must be separated by a :
        You can assume decoded_base64_authorization_header
        will contain only one :
        """
        nan = (None, None)
        if decoded_base64_authorization_header is None:
            return nan
        try:
            arr2 = decoded_base64_authorization_header.split(':')
            return (arr2[0], arr2[1])
        except (AttributeError, IndexError):
            return nan

    def user_object_from_credentials(self, user_email: str,
                                     user_pwd: str) -> TypeVar('User'):
        """
        returns the User instance based on his email and password.
        Return None if user_email is None or not a string
        Return None if user_pwd is None or not a string
        Return None if your database (file) doesn’t
        contain any User instance with email equal
        to user_email - you should use the class method
        search of the User to lookup the list of users
        based on their email. Don’t forget to test all
        cases: “what if there is no user in DB?”, etc.
        Return None if user_pwd is not the password of the User instance
        found - you must use the method is_valid_password of User
        Otherwise, return the User instance
        """
        if (user_email is None or isinstance(user_email, str) is False):
            return None
        if (user_pwd is None or isinstance(user_pwd, str) is False):
            return None
        mail = {'email': user_email}
        user = User()
        if user.search(mail) is None:
            return None
        else:
            if user.is_valid_password(user_pwd):
                return user
