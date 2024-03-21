"""Module for assignment 7.1."""

# 7.1 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# and print the contents of the file in upper case.
# Use the file words.txt to produce the output below.
# You can download the sample data at http://www.py4e.com/code3/words.txt

# The following lines are to be used for local file system
import os
cwd = os.getcwd()
fname = os.path.join(cwd,'chapter-07', input('Enter file name: '))
# The following line is only to be used for submission
# fname = input('Enter file name: ')
try:
    fhandle = open(fname, 'r')
except:
    print('File not found', fname)
    quit()

for line in fhandle:
    print(line.upper().rstrip())
