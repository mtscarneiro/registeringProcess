#Registro de usuarios novos.
age = input('Hello user, how old are you? ')
register = input('Press 0 to start registration process! Or press 1 for ...     ')

if int(register) == 0:
    registerName = input('Login name: ')
    print('Want to use your age as password? (y/n)  ')
    answerPass = input()
    if answerPass == 'y':
        registerPass = age
        print(f'{registerName}, your password is now {registerPass}!')
    elif answerPass == 'n':
        registerPass = input('Please insert the password of your choice:    ')
        print(f'{registerName}, your password is now {registerPass}!')
else:
    print('Hope you get to us later! Be safe.')

#Login dos usuarios.
loginName = input('Login: ')

while loginName != registerName:
    print("This login name doesn't exists")
    loginName = input('Login: ')

loginPass = input('Password: ')

if loginPass != registerPass:
    print('Wrong password!')
    loginPass = input('Try password again: ')

print(f'Welcome to PySpace, {loginName}')

