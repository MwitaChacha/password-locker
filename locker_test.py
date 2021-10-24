
import unittest
from user import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    
    '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
    
    def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            User.user_list = []
            
    def setUp(self):
            '''
        Set up method to run before each test cases.
        '''
            self.new_user = User("Willy","6775")


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.username,"Willy")
        self.assertEqual(self.new_user.password,"6775")
       
    def test_save_user(self):
        '''
        test_save_user test case to test if the user object is saved into
         the user list
        '''
        self.new_user.save_user() 
        self.assertEqual(len(User.user_list),1) 
        
    def test_delete_user(self):
            '''
            test_delete_user to test if we can remove a user from our user list
            '''
            self.new_user.save_user()
            test_user = User("Willy","6775")
            test_user.save_user()

            self.new_user.delete_user()
            self.assertEqual(len(User.user_list),1)     
    
    def test_display_user(self):
        '''
        method that returns a list of all contacts saved
        '''

        self.assertEqual(User.display_name(),User.user_list)

class TestCredentials(unittest.TestCase):
     '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''
     def tearDown(self):
            '''
            tearDown method that does clean up after each test case has run.
            '''
            Credentials.credentials_list = []
     
     def setUp(self):
            '''
        Set up method to run before each test cases.
        '''
            self.new_cred = Credentials("Instagram","2020")
            
            
     def test_init(self):
            '''
        test_init test case to test if the object is initialized properly
        '''

            self.assertEqual(self.new_cred.account_name,"Instagram")
            self.assertEqual(self.new_cred.account_password,"2020") 
            
     def test_save_credentials(self):
            '''
        test_save_credentials test case to test if the creential object is saved into
         the credential list
        '''
            self.new_cred.save_credentials() 
            self.assertEqual(len(Credentials.credentials_list),1)       
     
     def test_delete_credentials(self):
            '''
            test_delete_credentials to test if we can remove a cred from our cred list
            '''
            self.new_cred.save_credentials()
            test_cred = Credentials("Instagram","2020")
            test_cred.save_credentials()

            self.new_cred.delete_credentials()
            self.assertEqual(len(Credentials.credentials_list),1)
            
     def test_display_credentials(self):
            '''
        method that returns a list of all credentials saved
        '''

            self.assertEqual(Credentials.display_credentials(),Credentials.credentials_list)                    
if __name__ == '__main__':
    unittest.main()
    