"""Module for assignment 8.5."""

# 9.4 Write a program to read through the mbox-short.txt
# and figure out who has sent the greatest number of mail messages.
# The program looks for 'From ' lines and takes the second word
# of those lines as the person who sent the mail.
# The program creates a Python dictionary that maps the sender's mail address
# to a count of the number of times they appear in the file.
# After the dictionary is produced, the program reads through the dictionary
# using a maximum loop to find the most prolific committer.

def getEmail(line):
    words = line.split()
    return words[1].strip()

file_name = input('Enter a file name: ')
try:
    file_handle = open(file_name)
except:
    print('File not found:', file_name)

commits_by_user = dict()
for line in file_handle:
    if line.startswith('From '):
        user = getEmail(line)
        commits_by_user[user] = commits_by_user.get(user, 0) + 1

max_commits = None
user_with_max_commits=None
for user,commits in commits_by_user.items():
    if max_commits == None or commits > max_commits:
        max_commits = commits
        user_with_max_commits = user

print(user_with_max_commits, max_commits)