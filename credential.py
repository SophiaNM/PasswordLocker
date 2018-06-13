class Credential:

    credential_list=[]

    '''
    class that generates new instances of credentials
    '''

    def __init__(self, identity, user_name, password):
        '''
        Initializing the variables for the list of credentials
        '''
        self.identity=identity
        self.user_name=user_name
        self.password=password


    def save_credential(self):
        '''
        Function to create  and save log in credentials for users
        '''
        Credential.credential_list.append(self)


    @classmethod
    def authenticate_credential (cls,name,password):
        '''
        Method that checks if user and password are correct
        '''
        for cred in cls.credential_list:
            if cred.user_name == name and cred.password == password:
                return cred
        return 0

    def cred_data_exists(cls,number):
        '''
        Checks if data exists in the profile
        '''
        for data in cls.users_list:
            if data.data_identity == number:
                return True
        return False

    #End of credential class
