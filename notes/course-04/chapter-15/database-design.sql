-- Create multiple tables in a database to track song titles 

CREATE TABLE "Artist" (
	"id"	INTEGER NOT NULL UNIQUE,
	"name"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Artist" (name) VALUES ("Led Zepplin");
INSERT INTO "Artist" (name) VALUES ("AC/DC");

CREATE TABLE "Genre" (
    "id" INTEGER NOT NULL UNIQUE,
    "name" TEXT NOT NULL,
    PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Genre" (name) VALUES ("Rock");
INSERT INTO "Genre" (name) VALUES ("Metal");

CREATE TABLE "Album" (
    "id" INTEGER NOT NULL UNIQUE,
    "title" TEXT,
    "artist_id" INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Album" (title, artist_id) VALUES ("Who Made Who", 2);
INSERT INTO "Album" (title, artist_id) VALUES ("IV", 1);

CREATE TABLE "Track" (
    "id" INTEGER NOT NULL UNIQUE,
    "title" TEXT,
    "rating" INTEGER,
    "len" INTEGER,
    "count" INTEGER,
    "album_id" INTEGER,
    "genre_id" INTEGER,
    PRIMARY KEY("id" AUTOINCREMENT)
);
INSERT INTO "Track" (title, rating, len, count, album_id, genre_id) VALUES ("Black Dog", 5, 297, 0 , 2, 1);
INSERT INTO "Track" (title, rating, len, count, album_id, genre_id) VALUES ("Stairway", 5, 482, 0 , 2, 1);
INSERT INTO "Track" (title, rating, len, count, album_id, genre_id) VALUES ("About to Rock", 5, 313, 0 , 1, 2);
INSERT INTO "Track" (title, rating, len, count, album_id, genre_id) VALUES ("Who Made Who", 5, 207, 0 , 1, 2);

SELECT Album.title, Artist.name FROM Album
    JOIN Artist ON Album.artist_id = Artist.id;

SELECT Track.title, Artist.name, Album.title, Genre.name
FROM Track
	JOIN Genre ON Track.genre_id = Genre.id
	    JOIN Album ON Track.album_id = Album.id
	        JOIN Artist ON Album.artist_id = Artist.id;

-- Check out INSERT OR IGNORE