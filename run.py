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

def create_credentials(account_name, account_password):
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
    print("\n")
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
                print(f"Congratulations {username}! You have successfully created a Password Locker account.")
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
                print(f"Welcome {username} to your Password Locker account. Your password is {password}.")
                print("\n")
                print("You can be able to interact with your passwords here.")       
        
        elif short_code == "lg":
            print("Welcome back to Password Locker!")
            print("Enter your details for you to login in your account")
            print("Enter your username")
            username = input()
            print("Enter your password")
            password = input() 
            login = login_user(username, password)
            
            if login_user == login:
                print("\n")
                print(f"Welcome {username} to your Password Locker account. Your password is {password}.")
                print("You can be able to interact with your passwords here.")       
            else:
                print("Invalid username or password. Please try again or first create an account.")
                print("Enter username")
                username = input()
                print("Enter password")
                password = input()              
        
        while True:
            print("Input the following short codes to perform various actions in your Password Locker account:")
            print("ad - To add a new password")
            print("vw - To view our passwords")
            print("del - To delete your passwords")
            print("cc - To make Password Locker generate you a password for any of your accounts")
            print("ex - To exit")
            short_code = input("Enter your short code here: ")
            
            if short_code == "ad":
                print("Enter your the account whose password you want to store, e.g Snapchat" )
                print("Account Name: ")
                account_name = input()
                print("Enter the password for the account you have just entered ")
                account_password = input()
                print("\n")
                print("You have successfully added a password to your account!")
                print(f"Account: {account_name}  Password: {account_password}")
                print("\n")
                save_credentials(create_credentials(account_name, account_password))
                
            elif short_code == "vw":
                if display_credentials():
                  print("\n")
                  print("The following are your available passwords in your account: ")
                  for cred in display_credentials():
                      
                      print(f"Account name: {cred.account_name}  Account Password: {cred.account_password}")
                      print("\n")
                else: print("You do not seem to have any save passwords")
                
            elif short_code == "cc":
                print("Thank you for choosing us to help you generate your password.")
                print("To begin, enter the account you wish to have a password, e.g Twitter.")
                account_name = input()
                account_password = random.randint(1000, 9999)
                print("\n")
                print(f"Your generated password is {account_password}")
                save_credentials(create_credentials(account_name, account_password)) 
                print("\n")       
            
            elif short_code == "del":
                print("Enter the account name you want to delete below, e.g Twitter")
                search_account = input()
                search_account = get_credentials(account_name)
                print(f"Your account for {search_account.account_name} has been deleted successfully!")
                
           
            elif short_code == "ex":    
                print("Thank you for using Password Locker!")
                print("BYE")
                break        
                    
if __name__ == "__main__":
    main()                    