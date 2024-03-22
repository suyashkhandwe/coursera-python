"""Module for assignment 8.5."""

# 8.5 Open the file mbox-short.txt and read it line by line.
# When you find a line that starts with 'From ' like the following line:
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# You will parse the From line using split() and print out the
# second word in the line
# (i.e. the entire address of the person who sent the message).
# Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'.
# Also look at the last line of the sample output to see how to print the count.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt

file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print('Failed to open file',file_name)
    quit()

email_ids = list()
for line in file_handle:
    if not line.startswith('From '): continue
    email_ids.append(line.rstrip().split()[1])

for email_id in email_ids:
    print(email_id)
print('There were', len(email_ids), 'lines in the file with From as the first word')
