import re

def strong(password):
    length = re.compile(r'.{8,}')
    lower = re.compile(r'[a-z]')
    upper = re.compile(r'[A-Z]')
    numeral = re.compile(r'[0-9]')

    if length.search(password) == None:
        return False
    elif lower.search(password) == None:
        return False
    elif upper.search(password) == None:
        return False
    elif numeral.search(password) == None:
        return False
    else:
        return True

if strong(input('Please enter your password : ')):
    print('Strong Password')
else:
    print('Weak Password')
