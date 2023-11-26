#!/usr/bin/env python3
""""Module contains the class Auth"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Class Auth
    Methods:
      require_auth
      authorization
      current_user
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        '''returns True if the path is not
        in the list of strings excluded_paths:
        Returns True if path is None
        Returns True if excluded_paths is None or empty
        Returns False if path is in excluded_paths
        You can assume excluded_paths contains string path always ending by a /
        This method must be slash tolerant: path=/api/v1/status
        and path=/api/v1/status/ must be returned False if
        excluded_paths contains /api/v1/status/'''
        if path is None or excluded_paths is None or len(excluded_paths) == 0:
            return True
        else:
            for paths in excluded_paths:
                if path == paths or path + '/' == paths:
                    return False
            return True

    def authorization_header(self, request=None) -> str:
        """If request is None, returns None
        If request doesn’t contain the header key Authorization, returns None
        Otherwise, return the value of the header request Authorization
        """
        if request is None or 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns none"""
        return None
