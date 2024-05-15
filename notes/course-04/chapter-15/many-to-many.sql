-- Many to many relations can happen in cases such as courses and users - one course can have many users, and one user can have many courses

-- Python script - 
-- CREATE TABLE User (
-- 	    id INTEGER NOTNULL PRIMARY KEY AUTOINCREMENT UNION
-- 	    name TEXT,
-- 	    email TEXT
-- );

-- CREATE TABLE Course (
-- 	    id INTEGER NOTNULL PRIMARY KEY AUTOINCREMENT UNION
-- 	    title TEXT
-- );

-- CREATE TABLE Member (
--      user_id INTEGER,
-- 	    course_id INTEGER,
-- 	    role INTEGER,
-- 	    PRIMARY KEY (user_id , course_id)
-- );

-- SQL Syntax
--CREATE TABLE "User" (
--	    id INTEGER NOT NULL UNIQUE,
--	    name TEXT,
--	    email TEXT,
--	    PRIMARY KEY ("id" AUTOINCREMENT)
-- );

-- CREATE TABLE "Course" (
--      id INTEGER NOT NULL UNIQUE,
--      title TEXT,
--      PRIMARY KEY ("id" AUTOINCREMENT)
-- );

-- CREATE TABLE "Member" (
--      user_id INTEGER,
--      course_id INTEGER,
--      role INTEGER,
--      PRIMARY KEY (user_id , course_id)
-- );

-- Data Load
-- INSERT INTO Member(user_id, course_idm role) VALUES ('John', 'john@company.com');
-- INSERT INTO User (name, email) VALUES ('Jane', 'jane@company.com');
-- INSERT INTO User (name, email) VALUES ('Mark', 'mark@company.com');

-- INSERT INTO Course (title) VALUES ('Python');
-- INSERT INTO Course (title) VALUES ('Java');
-- INSERT INTO Course (title) VALUES ('PHP');

-- INSERT INTO Member(user_id, course_id, role) VALUES (1,1,1);
-- INSERT INTO Member(user_id, course_id, role) VALUES (2,1,0);
-- INSERT INTO Member(user_id, course_id, role) VALUES (3,1,1);

-- INSERT INTO Member(user_id, course_id, role) VALUES (1,2,0);
-- INSERT INTO Member(user_id, course_id, role) VALUES (2,2,1);

-- INSERT INTO Member(user_id, course_id, role) VALUES (2,3,1);
-- INSERT INTO Member(user_id, course_id, role) VALUES (3,3,0);

-- SELECT User.name, Member.role, Course.title
-- FROM User JOIN Member JOIN Course
-- ON Member.user_id = User.id AND Member.course_id = Course.id
-- ORDER BY Course.title, Member.role DESC, User.name

