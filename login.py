import sqlite3
import setup as user

def login():
    result = None
    while True:
        user_name = input('Enter your user name: ')
        password = input('Input your password: ')
        us = sqlite3.connect('inCollege.db')
        cu = us.cursor()
        cu.execute("""SELECT user_name, password from users WHERE user_name=? AND password=?""", (user_name, password))
        result = cu.fetchone()
        cu.close()
        us.close()

        if result:
            print('You have successfully logged in!')
            #return 'You have successfully logged in!', user_name
            return user_name
        else:
            print("Incorrect username/password. Do you want to try again?")
            ans = input("Type 0 to return to previous menu. Enter any other key to try again: ")
            if ans == '0':
                return None


