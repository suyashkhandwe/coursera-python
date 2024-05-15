"""Module for assignment 15.3"""

# Musical Track Database
# This application will read an iTunes export file in CSV format and produce a properly normalized database with this structure:

# CREATE TABLE Artist (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Genre (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     name    TEXT UNIQUE
# );

# CREATE TABLE Album (
#     id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
#     artist_id  INTEGER,
#     title   TEXT UNIQUE
# );

# CREATE TABLE Track (
#     id  INTEGER NOT NULL PRIMARY KEY 
#         AUTOINCREMENT UNIQUE,
#     title TEXT  UNIQUE,
#     album_id  INTEGER,
#     genre_id  INTEGER,
#     len INTEGER, rating INTEGER, count INTEGER
# );

# If you run the program multiple times in testing or with different files, 
# make sure to empty out the data before each run.
# 
# You can use this code as a starting point for your application: http://www.py4e.com/code3/tracks.zip.
# 
# The ZIP file contains the tracks.csv file to be used for this assignment.
# 
# You can export your own tracks from iTunes and create a database, 
# but for the database that you turn in for this assignment, 
# only use the tracks.csv data that is provided. 
# You can adapt the tracks_csv.py application in the zip file to complete the assignment.

# To grade this assignment, the program will run a query like this on your uploaded database and look for the data it expects to see:
# SELECT Track.title, Artist.name, Album.title, Genre.name 
#     FROM Track JOIN Genre JOIN Album JOIN Artist 
#     ON Track.genre_id = Genre.ID and Track.album_id = Album.id 
#         AND Album.artist_id = Artist.id
#     ORDER BY Artist.name LIMIT 3

# The expected result of the modified query on your database is: (shown here as a simple HTML table with titles)
#
# | Track                                   |   Artist  |   Album           |   Genre   |
# | -------                                 |   ------- |   -------         |   ------- |
# | Chase the Ace                           |   AC/DC   |   Who Made Who    |   Rock    |
# | D.T.                                    |   AC/DC   |   Who Made Who    |   Rock    |    
# | For Those About To Rock (We Salute You) |   AC/DC   |   Who Made Who    |   Rock    |

# File Structure -
# name = pieces[0]
# artist = pieces[1]
# album = pieces[2]
# count = pieces[3]
# rating = pieces[4]
# length = pieces[5]

# ? is used to avoid SQL injection

import sqlite3

sql = sqlite3.connect('assignment_15_3.sqlite')
query = sql.cursor()

def get_artist_id(artist_name):
    '''
    Gets the artist_id for the given artist_name from the database.
    '''
    query.execute('SELECT id FROM Artist WHERE name = ?', (artist_name,))
    artist_id_record = query.fetchone()
    if artist_id_record is None:
        return None
    return artist_id_record[0]

def insert_artist(artist_name):
    '''
    Inserts the given artist into the database and returns the id.
    '''
    query.execute('INSERT INTO Artist (name) VALUES (?)', (artist_name,))
    sql.commit()
    return get_artist_id(artist_name)

def get_genre_id(genre_name):
    '''
    Gets the genre_id for the given genre from the database.
    '''
    query.execute('SELECT id FROM Genre WHERE name = ?', (genre_name,))
    genre_id_record = query.fetchone()
    if genre_id_record is None:
        return None
    return genre_id_record[0]

def insert_genre(genre_name):
    '''
    Inserts the given genre into the database and returns the id.
    '''
    query.execute('INSERT INTO Genre (name) VALUES (?)', (genre_name,))
    sql.commit()
    return get_genre_id(genre_name)

def get_album_id(album_title):
    '''
    Gets the album_id for the given album from the database.
    '''
    query.execute('SELECT id FROM Album WHERE title = ?', (album_title,))
    album_id_record = query.fetchone()
    if album_id_record is None:
        return None
    return album_id_record[0]

def insert_album(album_title, artist_id):
    '''
    Inserts the given album into the database and returns the id.
    '''
    query.execute('INSERT INTO Album (title,artist_id) VALUES (?,?)', (album_title,artist_id,))
    sql.commit()
    return get_album_id(album_title)

def get_track_title_id(track_title):
    '''
    Gets the title_id for the given title name from the database.
    '''
    query.execute('SELECT id FROM Track WHERE title = ?', (track_title,))
    track_id_record = query.fetchone()
    if track_id_record is None:
        return None
    return track_id_record[0]

def insert_track(track_title, album_id, genre_id, track_length, track_rating, track_count):
    '''
    Inserts the given title with the other key details into the database
    '''
    query.execute(
        '''
            INSERT INTO Track
            (title,album_id,genre_id,len,rating,count)
            VALUES (?,?,?,?,?,?)
        ''',
        (track_title, album_id, genre_id, track_length, track_rating, track_count,))
    sql.commit()

def load_data():
    handle = open('tracks.csv')
    for line in handle:
        parts = line.strip().split(',')
        if len(parts) < 7:
            print('Ignoring line -', line, 'since it doesn\'t have enough columns to extract all values')
        track_title = parts[0].strip()
        artist_name = parts[1].strip()
        album_title = parts[2].strip()
        track_count = parts[3].strip()
        track_rating = parts[4].strip()
        track_length = parts[5].strip()
        genre_name = parts[6].strip()
        
        artist_id = get_artist_id(artist_name)
        if artist_id is None:
            artist_id = insert_artist(artist_name)
        
        genre_id = get_genre_id(genre_name)
        if genre_id is None:
            genre_id = insert_genre(genre_name)
        
        album_id = get_album_id(album_title)
        if album_id is None:
            album_id = insert_album(album_title, artist_id)
        
        title_id = get_track_title_id(track_title)
        if title_id is None:
            insert_track(track_title, album_id, genre_id, track_length, track_rating, track_count)

def generate_report():
    report_query = '''
        SELECT Track.title, Artist.name, Album.title, Genre.name
            FROM Track JOIN Genre JOIN Album JOIN Artist
                ON Track.genre_id = Genre.id
                    AND Track.album_id = Album.id 
                    AND Album.artist_id = Artist.id
            ORDER BY Artist.name
            LIMIT 3
    '''
    query.execute(report_query)
    records = query.fetchall()
    if records is None:
        print('Failed to find any records for query -', report_query)
    else:
        print('Track, Artist, Album, Genre')
        for record in records:
            print(f'''{record[0]}, {record[1]}, {record[2]}, {record[3]}''')


query.execute('DROP TABLE IF EXISTS Artist')
query.execute('DROP TABLE IF EXISTS Genre')
query.execute('DROP TABLE IF EXISTS Album')
query.execute('DROP TABLE IF EXISTS Track')

query.execute('''
    CREATE TABLE Artist (
        id    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name  TEXT UNIQUE
    );'''
)

query.execute('''
    CREATE TABLE Genre (
        id      INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        name    TEXT UNIQUE
    );'''
)

query.execute('''
    CREATE TABLE Album (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        artist_id   INTEGER,
        title       TEXT UNIQUE
    );'''
)

query.execute('''
    CREATE TABLE Track (
        id          INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
        title       TEXT UNIQUE,
        album_id    INTEGER,
        genre_id    INTEGER,
        len         INTEGER,
        rating      INTEGER,
        count       INTEGER
    );'''
)

load_data()
generate_report()

query.close()
