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
    