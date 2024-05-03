"""Module for assignment 15.2"""

# Counting Organizations
# This application will read the mailbox data (mbox.txt) 
# and count the number of email messages per organization (i.e. domain name of the email address)
# using a database with the following schema to maintain the counts.

# CREATE TABLE Counts (org TEXT, count INTEGER)
# When you have run the program on mbox.txt 
# upload the resulting database file above for grading.
# 
# If you run the program multiple times in testing or with different files, 
# make sure to empty out the data before each run.

# You can use this code as a starting point 
# for your application: http://www.py4e.com/code3/emaildb.py.

# The data file for this application is the same 
# as in previous assignments: http://www.py4e.com/code3/mbox.txt.

# Because the sample code is using an UPDATE statement and committing 
# the results to the database as each record is read in the loop, 
# it might take as long as a few minutes to process all the data. 
# The commit insists on completely writing all the data to disk every time it is called.

# The program can be speeded up greatly by moving the commit operation outside of the loop. 
# In any database program, there is a balance between the number of operations you 
# execute between commits and the importance of not losing the results of 
# operations that have not yet been committed.

# ? is used to avoid SQL injection

import sqlite3, re

sql = sqlite3.connect('assignment_15_2.sqlite')
query = sql.cursor()

query.execute('DROP TABLE IF EXISTS Counts')

query.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

handle = open('mbox.txt')
for line in handle:
    if not line.startswith('From '): continue
    organizations = re.findall('\\S+?@(\\S+)', line.strip())
    if len(organizations) == 1:
        organization = organizations[0]
    else:
        print('Found 2 organizations which was not expected in line=', line)
        continue
    
    query.execute('SELECT count FROM Counts WHERE org = ?', (organization,))

    row = query.fetchone()
    if row is None:
        query.execute('INSERT INTO Counts (org,count) VALUES (?, 1)', (organization,))
    else:
        query.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (organization,))
    sql.commit()

listAllOrganizations = 'SELECT * FROM Counts ORDER BY count desc LIMIT 10'

for row in query.execute(listAllOrganizations):
    org = row[0]
    count = row[1]
    print('org =', org, ' :: count =', count)

query.close()
