from credential import Credential
import string,random,time
import pyperclip

class UserData:
    '''
    Class that is creates and save new objects of user acccounts data
    '''
    users_list=[]
    password_list = []

    def __init__(self, user_identity, data_identity, account_name, account_key):
        '''
        Initializing the variables for the list of user data
        '''
        self.user_identity=user_identity
        self.data_identity=data_identity
        self.account_name=account_name
        self.account_key=account_key

    def save_account(self):
        '''
        Function to create  and save new accounts n user data list
        '''
        UserData.users_list.append(self)

    @classmethod
    def password_generator(cls,length):
        '''
        Function that is used to generate new password
        '''
        password_list = []
        round = 1
        while round <= length:
            gen_password = random.choice(string.ascii_lowercase + string.ascii_uppercase + string.digits)
            password_list.append(gen_password)
            round+=1
        return ''.join(password_list)


    @classmethod
    def data_exists(cls,number):
        '''
        Checks if data exists in the profile
        '''
        for data in cls.users_list:
            if data.data_identity == number:
                return True
        return False

    @classmethod
    def display_data(cls,user_number,data_number):
        '''
        display all passwords generated by the user
        '''
        for password in cls.users_list:
            if password.user_identity == user_number:
                if password.data_identity == data_number:
                    return password

    @classmethod








    #End of class user data
