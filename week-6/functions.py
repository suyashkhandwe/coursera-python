"""Module for demo of functions."""

# printit() : Ths will not work since the order of function definition matters and the function must be 'def'ined first before using.

"""Sample function to print something"""
def printit():
    print('hello from my function')

printit()    

# Function with a return

"""Sample function with a parameter"""
def greet(lang):
    if lang =='es':
        return 'hola'
    elif lang == 'en':
        return 'hi'
    else:
        return 'huh?'

print(greet('es'), 'user')
print(greet('en'), 'user')
print(greet('foo'), 'user')
