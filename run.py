#!/usr/bin/env python
from credential import Credential
from userdata import UserData
import pyperclip
import string,random,time

#Functions for Credentials
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

#Functions for User Data
def create_data(user_identity, data_identity, account_name, account_key):
    '''
    Function used to create new user data
    '''
    new_userdata = UserData(user_identity, data_identity, account_name, account_key)
    return new_userdata

def save_account(data):
    '''
    '''
    data.save_account()

def generate_password(length):
    '''
    Function that generates new password
    '''
    return UserData.password_generator(length)

def cred_data_exists(number):
    '''
    Functionthat checks for existing credentials
    '''
    return Credential.cred_data_exists(number)

def data_exists(number):
    '''
    Function that checks if the data exists
    '''
    return UserData.data_exists(number)

def display_data(user_number,data_number):
    '''
    Function that displays existing data
    '''
    return UserData.display_data(user_number,data_number)

def account_exist(name):
    '''
    Function that checks if the account exists by name
    '''
    return UserData.account_exist(name)

def copy_password(number,count):
    '''
    Function that copies the password to the clipboard
    '''
    UserData.copy_password(number,count)

def main():
    '''
    Main function for the program
    '''
    user_id = 0  # assigned to identity variable
    user_entries = []  # variable to hold the identity of user
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
                print("\n"+"Enter your password: ")
                password = input()

                save_credential(create_credential(user_id,username,password)) # create and save new contact.
                user_id+=1
                print ('\n')
                print(f"New Credential for user {username} with password {password} has been created.")
                print ('\n')
                print("Log in to continue")
                user_entries.append(0)
                print("-"*20)

        elif short_code == 'li':
                #logging in to the account
                print("Enter your user name and password to log in:")
                print("-"*40)

                my_username = input("Username: ")
                my_password = input("Password: ")
                result = authenticate(my_username,my_password)

                if result == 0:
                    print('\n')
                    print("Invalid username and/or password")
                    print("-"*30)
                elif result != 0:
                    print(f"Welcome result {result.user_name}. What would you like to do?")

                    while True:
                        print("Type one of the short codes:\n  ca - create new account \n  va - view accounts\n  cp - copy password to clipboard\n  lo - Log Out")
                        code_input = input().lower()

                        if code_input == 'ca':
                                #Creating new account
                                print("Enter new account name eg. facebook, yelp")
                                account_name = input("Account Name")
                                print("Do you want to to key in your own password or automatically generate one?")


                                print("Type these codes:\n mp - manually generate password\n ap - automatically generate password")
                                password_input = input().lower()

                                if password_input == 'mp':
                                    #mannually input password
                                    account_key = input("Enter your new password: ")
                                    user_identity = result.identity

                                    save_account(create_data(user_identity,user_entries[user_identity], account_name, account_key))
                                    user_entries[user_identity] = user_entries[user_identity]+1

                                    print("\n Kindly wait ....")
                                    time.sleep(1.5)

                                    print('\n')
                                    print(f"The new password for account {account_name} is {account_key}\n")



                                elif password_input == 'ap':
                                    #automatically generate password
                                    print("How long would you like the password to be")
                                    password_length = int(input("Length of password: "))

                                    account_key = generate_password(password_length)
                                    user_identity = result.identity

                                    save_account(create_data(user_identity,user_entries[user_identity], account_name, account_key))
                                    user_entries[user_identity] = user_entries[user_identity]+1

                                    print("\n Kindly wait ....")
                                    time.sleep(1.5)

                                    print('\n')
                                    print(f"The new password for account {account_name} is {account_key} your {user_identity} and {user_entries[user_identity]}\n")

                                else:
                                    print("Invalid entry enter command again")

                        elif code_input == 'va':
                            #displaying data
                            if data_exists(result.identity):
                                length = user_entries[result.identity]
                                print(f"You have {length} passwords:")
                                print("\n")

                                mydata = 0

                                while mydata < length:
                                    get_data = display_data(result.identity,mydata)
                                    print(f"***{mydata+1}. Account Name:{get_data.account_name}-----Account Password:{get_data.account_key}***")
                                    mydata+=1
                                print("Type a command to continue")
                            else:
                                print("You haave no data use ca code  to create new accounts")
                                print("-"*20)

                        elif code_input == 'cp':
                            # copying password to clipboard
                            if data_exists(result.identity):
                                print("Enter the account id you want to copy")
                                get_index = int (input("Enter index: "))-1

                                if get_index >= user_entries[result.identity] or get_index<0:
                                    print("\n")
                                    print(f"{get_index+1} is invalid. Enter the correct index of password to copy")
                                    print("confirm index using vp password")
                                    print("-"*25)

                                elif get_index < user_entries[result.identity]:
                                    copy_password(result.identity,get_index)
                                    print("\n")
                                    print(f"Password {get_index+1} on the list has been copied, and is ready for pasting")
                                    print("-"*30)
                            else:
                                print("\nYou have no data.\nType ac to add some passwords")
                                print("-"*20)


                        elif code_input == 'lo':
                            #logging out of account
                            print('\n')
                            print(f"Goodbye {result.user_name}")
                            break

                        else:
                            print("Invalid entry enter command again")
                            print("\n"+"-"*35)




        elif short_code == 'ex':
                #exiting from the program
                print ("Thank you and Goodbye")
                break
        else:
                print("I did not get that. Kindly use the short codes")


if __name__ == '__main__':

    main()
