#!/usr/bin/env python3.9
import random
from user import User
from credentials import Credentials

def create_user(username, password):
    """[A function that creates a new user]

    Args:
        username ([type]): [description]
        password ([type]): [description]
    """
    new_user = User(username, password)
    return new_user

