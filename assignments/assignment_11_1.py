"""Module for assignment 11.1"""

# In this assignment you will read through and parse a file
# with text and numbers. You will extract all the
# numbers in the file and compute the sum of the numbers.

# Data Files
# We provide two files for this assignment. One is a sample file
# where we give you the sum for your testing and the other is
# the actual data you need to process for the assignment.
# Sample data: http://py4e-data.dr-chuck.net/regex_sum_42.txt
# (There are 90 values with a sum=445833)
# 
# Actual data: http://py4e-data.dr-chuck.net/regex_sum_1995354.txt
# (There are 93 values and the sum ends with 147)

import re

filename = input('Enter the file name: ')
try:
    stream = open(filename)
except:
    print('File not found:', filename)
    quit()

sum = 0
for line in stream:
    for numberAsString in re.findall('[0-9]+', line):
        sum = sum + int(numberAsString)
print('Ths sum of all numbers in:', filename, 'is:', sum)
