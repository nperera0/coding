-- Any user who has registered
CREATE TABLE users AS (
   user_id INTEGER,
 email VARCHAR,
   PRIMARY KEY (user_id)
);
-- Any user who has enrolled in a course
CREATE TABLE enrollments AS (
   user_id INTEGER,
   course_id INTEGER,
   PRIMARY KEY (user_id, course_id)
);
CREATE TABLE courses_universities AS (
   course_id INTEGER,
   university_id INTEGER,
   PRIMARY KEY (course_id, university_id)
);



SELECT COUNT(1) --200
FROM enrollments;

SELECT COUNT(1) -- 240
FROM enrollments AS e
JOIN courses_universities AS cu
   ON e.course_id = cu.course_id
;


--Enrollments by university

SELECT university_id, COUNT(user_id)
FROM enrollments JOIN courses_universities
ON enrollments.course_id = courses_universities.course_id
GROUP BY university_id


--number of enrollments by user

SELECT user_id, COUNT(course_id)  FROM enrollments
GROUP BY user_id

--overall average number of enrollments

SELECT CAST(COUNT(course_id IS  NOT NULL), FLOAT)/CAST(COUNT(DISTINCT user_id), FLOAT) * 100.00
FROM users  LEFT JOIN enrollments
ON users.user_id = enrollments.user_id


--list the users who have not enrolled

SELECT DISTINCT user_id FROM users WHERE user_id NOT IN (SELECT DISTINCT user_id FROM enrollments)

--total count of users who have not enrolled

SELECT COUNT(user_id) FROM users
WHERE user_id NOT IN (SELECT DISTINCT user_id FROM enrollments)


--overall % of users who have not enrolled in a course

SELECT CAST(COUNT(course_id IS NULL), FLOAT)/CAST(COUNT(*), FLOAT) * 100.00
FROM users  LEFT JOIN enrollments
ON users.user_id = enrollments.user_id
