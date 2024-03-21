"""Module for assignment 7.2."""

# 7.2 Write a program that prompts for a file name,
# then opens that file and reads through the file,
# looking for lines of the form:
#   X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point
# values from each of the lines and compute the average of those values
# and produce an output as shown below.
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
# when you are testing below enter mbox-short.txt as the file name.

fname = input('Enter file name: ')
try:
    fhandle = open(fname, 'r')
except:
    print('File not found', fname)
    quit()

spam_count = 0
spam_total = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence'):
        spam_count = spam_count + 1
        spam_total = spam_total + float(line[line.find(' '):].strip())

avg_spam_confidence = spam_total / spam_count
print('Average spam confidence:', avg_spam_confidence)