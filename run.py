#!/usr/bin/env python
from credential import Credential

def create_credential(identity, user_name, password):
    '''
    Function used to initialize and create new accounts
    '''
    new_cred = Credential(identity, user_name,password)
    return new_cred


def save_credential(credential):
    '''
    Function that saves user credentials
    '''
    credential.save_credential()

def authenticate(name,password):
    '''
    Function that authenticates for signing in
    '''
    return Credential.authenticate_credential(name,password)











def main():
    '''
    Main function for the program
    '''
    user_id = 0 #assigned to identity variable
    print("\n")
    print("Hello, welcome to password locker!")
    print("-"*35)
    print("\n")

    print("Please enter your name")
    user_name= input()

    print("\n")
    print(f"Hello {user_name}. what would you like to do?")


    while True:

        print("Type in one of these short codes : \n cc - create a new account credential,\n li - logging in, \n ex - exit passwordlocker ")

        short_code = input().lower()

        if short_code == 'cc':
                #creating a new account
                print("Creating new account"+"\n"+"-"*20+"\n"+ "Enter your Username:")
                username = input()
                print("\n"+"Enter your password:")
                password = input()

                save_credential(create_credential(user_id,username,password)) # create and save new contact.
                user_id+=1
                print ('\n')
                print(f"New Credential for user {username} with password {password} has been created")
                print ('\n')
                print("Log in to continue")
                print("-"*20)

        elif short_code == 'li':
                #logging in to the account
                pass

        elif short_code == 'ex':
                #exiting from the progra,
                print ("Thank you and Goodbye")
                break
        else:
                print("I did not get that. Kindly use the short codes")


if __name__ == '__main__':

    main()
