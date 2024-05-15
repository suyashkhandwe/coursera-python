"""Module for assignment 15.4"""

# Instructions
# This application will read roster data in JSON format, parse the file, 
# and then produce an SQLite database that contains a User, Course, 
# and Member table and populate the tables from the data file.

# You can base your solution on this code:
# http://www.py4e.com/code3/roster/roster.py - this code is incomplete
# as you need to modify the program to store the role column in the 
# Member table to complete the assignment.

# Each student gets their own file for the assignment. Download this file:
# Download your roster.json data
# And save it as roster_data.json. 
# Move the downloaded file into the same folder as your roster.py program.

# Once you have made the necessary changes to the program and it has been 
# run successfully reading the above JSON data, run the following SQL command:

# SELECT User.name,Course.title, Member.role
# FROM User JOIN Member JOIN Course
# ON User.id = Member.user_id
#   AND Member.course_id = Course.id
# ORDER BY User.name DESC, Course.title DESC, Member.role DESC LIMIT 2;

# The output should look as follows:
# | Zunaira |   si364   |   0   |
# | Ziya    |   si364   |   0   |

# Once that query gives the correct data, run this query:
# SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X
# FROM User JOIN Member JOIN Course
# ON User.id = Member.user_id
#   AND Member.course_id = Course.id
# ORDER BY X LIMIT 1;
# You should get one row with a string that looks like XYZZY53656C696E613333.

# File Structure -
#   [
#    "Hareem",  >> User.name
#    "si110",   >> Course.title
#    1          >> Member.role
#  ],

# ? is used to avoid SQL injection

import sqlite3, json

sql = sqlite3.connect('assignment_15_4.sqlite')
query = sql.cursor()

def insert_user(user_name):
    """
    Inserts the user into the database and returns the id.
    """
    query.execute('INSERT OR IGNORE INTO User (name) VALUES (?)', (user_name,))
    sql.commit()
    
    query.execute('SELECT id FROM User WHERE name = ?', (user_name,))
    user_id_record = query.fetchone()
    if user_id_record is None:
        return None
    return user_id_record[0]

def insert_course(course_title):
    """
    Inserts the given course into the database and returns the id.
    """
    query.execute('INSERT OR IGNORE INTO Course (title) VALUES (?)', (course_title,))
    sql.commit()
    query.execute('SELECT id FROM Course WHERE title = ?', (course_title,))
    course_id_record = query.fetchone()
    if course_id_record is None:
        return None
    return course_id_record[0]

def insert_member(user_id, course_id, role):
    """
    Inserts the given member with the other key details into the database.
    """
    query.execute(
        '''
            INSERT OR IGNORE INTO Member
            (user_id,course_id,role)
            VALUES (?,?,?)
        ''',
        (user_id, course_id, role,))
    sql.commit()

def load_data():
    handle = open('roster_data.json')
    roster_json_data = json.loads(handle.read())
    for roster_object in roster_json_data:
        if roster_object is None or len(roster_object) < 3:
            print('Ignoring line -', roster_object, 'since it doesn\'t have enough values to extract all fields')
            continue
        user_name = roster_object[0].strip()
        course_title = roster_object[1].strip()
        role = roster_object[2]
        
        user_id = insert_user(user_name)
        course_id = insert_course(course_title)
        insert_member(user_id, course_id, role)

def generate_report():
    report_query = '''
        SELECT User.name,Course.title, Member.role
        FROM User JOIN Member JOIN Course
        ON User.id = Member.user_id
            AND Member.course_id = Course.id
        ORDER BY User.name DESC, Course.title DESC, Member.role DESC
        LIMIT 2;
    '''
    query.execute(report_query)
    records = query.fetchall()
    if records is None:
        print('Failed to find any records for query -', report_query)
    else:
        for record in records:
            print(f'''{record[0]}|{record[1]}|{record[2]}''')

def compute_x():
    report_query = '''
        SELECT 'XYZZY' || hex(User.name || Course.title || Member.role ) AS X
        FROM User JOIN Member JOIN Course
        ON User.id = Member.user_id
            AND Member.course_id = Course.id
        ORDER BY X
        LIMIT 1;
    '''
    query.execute(report_query)
    records = query.fetchall()
    if records is None:
        print('Failed to find any records for query -', report_query)
    else:
        for record in records:
            print(f'''{record[0]}''')

query.executescript('''
    DROP TABLE IF EXISTS User;
    DROP TABLE IF EXISTS Course;
    DROP TABLE IF EXISTS Member;

    CREATE TABLE User (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name TEXT UNIQUE
    );

    CREATE TABLE Course (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title TEXT UNIQUE
    );

    CREATE TABLE Member (
        user_id INTEGER,
        course_id INTEGER,
        role INTEGER,
        PRIMARY KEY (user_id , course_id)
    );    
    ''')

load_data()
generate_report()
compute_x()

query.close()
