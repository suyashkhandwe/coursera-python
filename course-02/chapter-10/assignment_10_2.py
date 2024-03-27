"""Module for assignment 8.5."""

# 10.2 Write a program to read through the mbox-short.txt
# and figure out the distribution by hour of the day for each
# of the messages.
# You can pull the hour out from the 'From ' line by finding the
# time and then splitting the string a second time using a colon.
# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
# Once you have accumulated the counts for each hour,
# print out the counts, sorted by hour as shown below.

def getHour(line):
    hour = 'n/a'
    words = line.strip().split()
    if len(words) > 5:
        timestamp_parts = words[5].strip().split(':')
        if len(timestamp_parts) > 0:
            hour = timestamp_parts[0].strip()
    return hour

file_name = input('Enter a file name:')
try:
    file_handle = open(file_name)
except:
    print('File not found:', file_name)

count_by_hour = dict()
for line in file_handle:
    if line.startswith('From '):
        hour = getHour(line)
        if hour != 'n/a':
            count_by_hour[hour] = count_by_hour.get(hour, 0) + 1

for hour,count in sorted(count_by_hour.items()):
    print(hour, count)
