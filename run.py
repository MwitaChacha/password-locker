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

def save_user(user):
    """
    A function that saves a user
     """
    user.save_user()
    
def delete_user(user):
    """
    A function that deletes a user
    """
    user.delete_user()
        
def login_user(username, password):
    """
    A function that verifies a user login
    """
    check_user = User.verify_login(username, password)
    return check_user

def create_cred(account_name, account_password):
    """
    A function that creates a new credential
    """
    new_cred = Credentials(account_name, account_password)
    return new_cred   

def save_credentials(cred): 
    """
    A function that saves a credential
    """
    cred.save_credentials()
    
def delete_credentials(cred):
    """
    A function that deletes a credential
    """
    cred.delete_credentials()
    
           