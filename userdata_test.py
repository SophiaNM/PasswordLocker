from userdata import UserData
import unittest,pyperclip

class TestUserData(unittest.TestCase):
    '''
    This is a test class that tests cases for creating and authenticating user data
    '''

    def setUp(self):
        '''
        Function to set initial variables for testing
        '''
        self.new_userdata= UserData(1,1,"Yelp","adminpass")

    def tearDown(self):
        '''
        tear down function does clean up after each test case
        '''
        UserData.users_list = []

    def test_init(self):
        '''
        test_init test case to check if objects initialized properly
        '''
        self.assertEqual(self.new_userdata.user_identity,1)
        self.assertEqual(self.new_userdata.data_identity,1)
        self.assertEqual(self.new_userdata.account_name,"Yelp")
        self.assertEqual(self.new_userdata.account_key,"adminpass")

    def test_save_account(self):
        '''
        test_save_account test case to test if userdata object is saved into users_list
        '''
        self.new_userdata.save_account()   #create and save new_cred
        self.assertEqual(len(UserData.users_list),1)

    def test_password_generator(self):
        '''
        test_password_generator test case to test if password has been generated and saved
        '''
        password_list = []

        password = self.new_userdata.password_generator(2)
        password_list.append(password)
        self.assertEqual(len(password_list),1)

    def test_data_exists(self):
        '''
        test_data_exists test case to test if the the function checks that the data exists
        '''

        self.new_userdata.save_account()
        test_data = UserData(2,2,"Test","admintest")

        test_data.save_account()
        data_exists = UserData.data_exists(2)
        self.assertTrue(data_exists)

    def test_display_data(self):
        '''
        test_display_data test case used to test if the function displays the data
        '''
        self.new_userdata.save_account()
        test_data = UserData(2,2,"Test","admintest")

        test_data.save_account()
        display_data = UserData.display_data(2,2)
        self.assertEqual(test_data.account_name,display_data.account_name)

    def test_copy_password(self):
        '''
        Test to confirm that we are copying the email address from a found contact
        '''

        self.new_userdata.save_account()
        UserData.copy_password(1,1)

        self.assertEqual(self.new_userdata.account_key,pyperclip.paste())




if __name__ == "__main__":
    unittest.main()
