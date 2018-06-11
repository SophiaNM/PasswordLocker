from credential import Credential
import unittest

class TestCredential(unittest.TestCase):
    '''
    This is a test class that tests cases for creating and authenticating credentials
    '''

    def setUp(self):
        '''
        Function to set initial variables for testing
        '''
        self.new_cred = Credential(1,"Sophia","admin")

    def tearDown(self):
        '''
        tear down function does clean up after each test case
        '''
        Credential.credential_list = []

    def test_init(self):
        '''
        test_init test case to test if the object initialized properly
        '''
        self.assertEqual(self.new_cred.identity,1)
        self.assertEqual(self.new_cred.user_name,"Sophia")
        self.assertEqual(self.new_cred.password,"admin")

    def test_save_credential(self):
        '''
        test_create_credential test case to test if credential object is saved into credential_list
        '''
        self.new_cred.save_credential()   #create and save new_cred
        self.assertEqual(len(Credential.credential_list),1)

    def test_create_multiple_credentials(self):
        '''
        test_create_multiple_credentials test case to check if we can save multiple objects to our credential list
        '''
        self.new_cred.save_credential()
        test_cred = Credential(2,"Njeri","admin2") #new credentials
        test_cred.save_credential()

        self.assertEqual(len(Credential.credential_list),2)

    def test_authenticate_credential(self):
        '''
        '''

        test_cred = Credential(1,"Test","Password")
        test_cred.save_credential()

        found_cred = Credential.authenticate_credential("Test","Password")
        self.assertEqual(found_cred.identity,test_cred.identity)


if __name__ == "__main__":
    unittest.main()
