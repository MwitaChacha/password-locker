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
    
def get_credentials(account_name):
    """
    A function that finds and returns a credential
    """
    return Credentials.get_credentials(account_name)

def display_credentials():
    """
    A function that displays available credentials
    """
    return Credentials.display_credentials()   

def main():
    print("Hi :) Welcome to Password Locker.")
    print("\n")
    print("Use the following short codes to navigate through the application.")
    print("na - To create a new account.")
    print("lg - To log in to your account.")
    short_code = input("Write your short code here: ")
    print("\n") 
             
    while True:
        if short_code == "na":
            print("To create a new account, you will need a username and a password.")  
            print("Write your username below:")
            username = input()
            print("Write your password below: ")
            password = input()
            save_user(create_user(username, password))
            print("Can you please confirm your password below:") 
            confirmed_password = input()
            
            while confirmed_password != password:
                print("Please input the correct password to continue")
                password = input()
                print("Confirm your password")
                confirmed_password = input()
                
            else:
                print(f"Congratulations {username}! You have successfully created a Passwor Locker account.")
                print("\n")
                print("Enter your login details to continue...")
                print("Enter usernme")
                login_username = input()
                print("Enter password")
                login_password = input()
                
            while username != login_username or confirmed_password != login_password:
                print("Invalid username or password. Please try again.")
                print("Enter username")
                login_username = input()
                print("Enter password")
                login_password = input()
                
            else:
                print(f"Welcome {username} to your Password Locker account.")       
                    
                
                    