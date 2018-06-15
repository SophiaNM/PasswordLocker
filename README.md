# PasswordLocker
This is the third Independent project for Moringa Core, June 8th, 2018.


## Description
Password Locker is an application that helps users generate and store passwords on their multiple accounts.
The password locker runs as a terminal application and uses short codes to navigate through it.


## Features
1. Users can create a new account, input their password, log in or exit the application using the following short codes:

    1. cc - Creates new account creadential
    2. li - Logging in
    3. ex - Exit the PasswordLocker


2. After logging in, users can create accounts for which they want their passowrds stored. They can then view the passwords , copy the password or log out of the application. Once logged in the following commands are availed:

    1. ca - Create accounts
    2. va - View accounts
    3. cp - Copy password to clipboard
    4. lo - Log out

## Behavior Driven Development
Specifications include:

| Behavior            | Input                         | Output                        |
| ------------------- | ----------------------------- | ----------------------------- |
| Starting the application | In the terminal run `python3.6 run.py` |Hello,welcome to passwordlocker please input your name |
| Welcome message |Input name `Sophia` | Welcome `Sophia` what would you like to do? <br> cc -Creates new account creadential <br> li-Logging in <br> ex- Exit the PasswordLocker|
| Create new credentials | Type: `cc` Username: Sophia <br>Password: Admin | New Credential for user name `Sophia` with password `Admin` has been created. |
| Logging in the account | Type: `li` <br>  Username: Sophia <br> Password: Admin | Welcome `Sophia` what would you like to do?<br> ca - Create accounts <br> va - View accounts <br> cp - Copy password to clipboard <br>lo - Log out |
| Create new accounts and passwords | Type:`ca` <br> account name: Yelp  | Do you want to to key in your own password or automatically generate one? <br> mp - manually generate password <br>ap - automatically generate password |
|Generate password manually | Type `mp` <br> Input your password: !Password123 |The new password for account Yelp is !Password123 |
| Or Generate password automatically | Type `ap` <br> Input the length of your password:10 | The new password for account Yelp is !Pa2SwqW13 |
| View the accounts and passwords |Type `va` | 1. Account Name: Yelp-----!Pa2SwqW13 |
| Copy password to clipboard | Type `ca` <br> Enter the account index you want to copy| Password 1 on the list has been copied and is ready for pasting|
| Log out of account | Type `lo` |*Goodbye Sophia* returns to first interface with `cc`,`li` and `ex` |
| Exit PasswordLocker | Type `ex` | *Goodbye* Application is closed|


## Prerequiites
    - Python 3.6 required

## Set-up and Installation
    1. Clone or download the Repo
    2. Install python 3.6
    3. Run `python3.6 run.py` on your terminal

## Known bugs
No known bugs so far. If found drop me an email.

## Technologies Used
Built using Python 3.6

## Contributors
    - Sophia Murage

### Contact Information
njerimurage92@gmail.com | snmurage1@gmail.com
