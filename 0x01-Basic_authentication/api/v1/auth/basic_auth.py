#!/usr/bin/env python3
"""Module contains the class BasicAuth"""
from api.v1.auth.auth import Auth
import base64
import binascii


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
