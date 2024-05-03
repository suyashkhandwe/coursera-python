"""Module for demo of Email DB using Python"""

# ? is used to avoid SQL injection

import sqlite3

sql = sqlite3.connect('emaildb.sqlite')
query = sql.cursor()

query.execute('''
            DROP TABLE IF EXISTS Counts
            ''')

query.execute('''
            CREATE TABLE Counts(email TEXT, count INTEGER)
            ''')

handle = open('../../../assignments/mbox-short.txt')
for line in handle:
    if not line.startswith('From '): continue
    email = line.split()[1]
    
    query.execute('''
                SELECT count FROM Counts WHERE email = ?
                ''', (email,))
    row = query.fetchone()
    if row is None:
        query.execute('''
                    INSERT INTO Counts (email,count) VALUES (?, 1)
                    ''', (email,))
    else:
        query.execute('''
                    UPDATE Counts SET count = count + 1 WHERE email = ?
                    ''', (email,))
    
    sql.commit()

listAllCountsSqlQuery = 'SELECT * FROM Counts ORDER BY count desc LIMIT 10'

for row in query.execute(listAllCountsSqlQuery):
    email = row[0]
    count = row[1]
    print('Email =', email, ' :: count =', count)

query.close()