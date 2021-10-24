class User:
    """
    A class that generates new instances of our password locker users
    """
    user_list = []
    
    def __init__(self, username, password):
        """
        A method that defines properties of the User class
        """
        
        self.username = username
        self.password = password
    
    def save_user(self):
        
        """
        A method that saves a new User instance
        """
        User.user_list.append(self)
    
    def delete_user(self):
        """
        A method that delete an instance of User
        """
        User.user_list.remove(self)
    
    @classmethod
    def display_name(cls):
        """
        A method that displays the available users in the list 
        """
        return cls.user_list
    
    @classmethod
    def verify_login(cls, username, password):
         """
         A method that verifies a user login
         """
         for user in cls.user_list:
             if user.username == username and user.password == password:
                 return user               