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
        '''Returns false'''
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns none"""
        return None
