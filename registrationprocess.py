import sys

print('Hello new user! Let me know you!')
age = input('How old are you? ')

# Checking age:
if int(age) < 18:
    print("You're still a minor. Sorry!")
    sys.exit()
elif int(age) == 18:
    print("You're ready. ")
else:
    print('You can register. You are an adult!')

"""print('Are you registered? (y/n) ')
login = input()
if login == 'y':"""
    

print('Hello, user. Do you want to register? (y/n)')
register = input()

# Register process:
if register == 'y':
    print('Enter your data here!')
    name = input("What's your name? ")

    print(f'Hello {name}, do you want to use your age as your id? (y/n)')
    answer = input()

    if answer == 'y':
        print(f'Your new ID is {age}')
        def age():
            age = idd1
        passw = input('Type a number password: ')
    elif answer == 'n':
        idd = input('Enter your ID: ')
        passw = input('Type a number password: ')
    else:
        if answer != 'y' or 'n':
            print(f'{name}, this answer is wrong, please insert "y" for Yes and "n" for No!')
            answer = input()
            
elif register == 'n':
    print("That's ok! We'll be here for you later! ")
    sys.exit()
else:
    print('Wrong answer.')
    register = input()
    
# End of register process.




print(f'{name}, type in your password to access your space: ')
password = input('Password: ')

while int(password) !=  int(passw):
    print('Wrong password.')
    password = input('Type password again: ')

print(f'Welcome to PySpace, {name}')

