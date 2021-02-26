class account:
    def __init__(self, user, password, balance):
        self.user = user
        self.password = password
        self.balance = balance


user1 = account('user1', '1111', 100)
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


def end():
    print('Thank you, goodbye!')
    quit()


# New menu function to check current balance
def account_balance():
    print('Your current account balance is $' + str(user1.balance))


def password_account_check():
    if user1.user == user_username and user1.password == user_password:
        print('Your current account balance is $' + str(user1.balance))
        user_selection()
    elif user1.user != user_username or user1.password != user_password:
        print('Invalid Username and/or Password. Try again later.')


# function to restart sub-menu without ending program
def user_continue():
    user_continue = input('\nDo you want to continue? Y/N: ')
    user_continue = user_continue.upper()
    if user_continue == 'N':
        end()
    elif user_continue == 'Y':
        return user_selection()


# user selection redirects user to selected atm function
def user_selection():
    user_selection = input('\nWhat would you like to do?\n'
                           'Enter 1 - Withdraw\n'
                           'Enter 2 - Deposit\n'
                           'Enter 3 - View Account Balance\n'
                           'Enter 4 - Exit\n'
                           '\nPlease select 1, 2, 3 or 4: ')
    while user_selection != 0:
        if user_selection == '1':
            withdraw()
            user_continue()

        if user_selection == '2':
            deposit()
            user_continue()

        if user_selection == '3':
            account_balance()
            user_continue()

        if user_selection == '4':
            end()

        else:
            print('Invalid Choice')
            user_continue()


password_account_check()
