class account:
    def __init__(self, user, password, balance):
        self.user = user
        self.password = password
        self.balance = balance


user1 = account('user1', '1111', 5)
user_username = input('Enter username: ')
user_password = input('Enter password: ')


# atm functions
def withdraw():
    cash = int(input('How much would you like to withdraw?: '))
    user1.balance = user1.balance - cash
    print('Your new account balance is $' + str(user1.balance))


def deposit():
    cash = int(input('How much would you like to deposit?: '))
    user1.balance = user1.balance + cash
    print('Your new account balance is $' + str(user1.balance))


"""
def end():
    print('Thank you, goodbye!')


def user_continue():
    user_continue = input('Do you want to continue? Y/N: ')
    if user_continue == 'n':
        end()
    else:
        return
"""

if user1.user == user_username and user1.password == user_password:
    print('Your current account balance is $' + str(user1.balance))
    user_selection = input('\nWhat would you like to do?\n'
                           'Enter 1 - To Withdraw\n'
                           'Enter 2 - To Deposit\n'
                           'Enter 3 - To Exit\n'
                           '\nPlease select 1, 2 or 3: ')
    while user_selection != 0:
        if user_selection == '1':
            withdraw()
            user_continue = input('\nDo you want to continue? Y/N: ')
            user_continue = user_continue.upper()
            if user_continue == 'N':
                print('Thank you, Goodbye!')
                break
            else:
                continue

        if user_selection == '2':
            deposit()
            break
        if user_selection == '3':
            break


elif user1.user != user_username or user1.password != user_password:
    print('Invalid Username and Password. Try again.')
