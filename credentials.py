class Credentials:
    
    """
    A class that generates new instances of creentials
    """
    
    credentials_list = []
    
    def __init__(self, account_name, account_password):
        """
        A method that defines properties of the credentials class 
        """
        self.account_name = account_name
        self.account_password = account_password
    
    def save_credentials(self):
        """
        A method that saves new instances of the Credentials class
        """
        Credentials.credentials_list.append(self)    