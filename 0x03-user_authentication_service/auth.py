#!/usr/bin/env python3
""""Module contain authorization variables"""

import bcrypt


def _hash_password(password: str) -> str:
    """Takes in a password string arguments and returns bytes.
    The returned bytes is a salted hash of the input password,
    hashed with bcrypt.hashpw
    """
    pswrd = password.encode()
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pswrd, salt)

    return hashed_password
