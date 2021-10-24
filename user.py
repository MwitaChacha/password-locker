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
             