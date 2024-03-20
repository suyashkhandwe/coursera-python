"""Module for assignment 5.2."""

# Problem Statement
# 5.2 Write a program that repeatedly prompts a user for integer numbers
# until the user enters 'done'.
# 
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a
# try/except and put out an appropriate message and ignore the number.
# 
# Enter 7, 2, bob, 10, and 4 and match the output below.


MAX = None
MIN = None
while(1):
    num_str = input('Enter an integer: ')
    if num_str == 'done':
        break
    try:        
        num = int(num_str)
    except:
        print('Invalid input')
        continue
    if MAX is None or num > MAX:
        MAX = num
    if MIN is None or num < MIN:
        MIN = num

print('Maximum is', MAX)
print('Minimum is', MIN)
