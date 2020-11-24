
'''Creating Tables'''

CREATE OR REPLACE TABLE data.Users (
  user_id INT64 NOT NULL, # primary_key
  first_name STRING,
  last_name STRING,
  email STRING,
  gender STRING,
  join_date DATE,
  country STRING,
  city STRING,
  language STRING
)

CREATE OR REPLACE TABLE data.Courses (
  course_id STRING NOT NULL, # primary_key
  instructor_id STRING NOT NULL, # forign key to instructors table
  title STRING,
  description STRING,
)

CREATE OR REPLACE TABLE data.Instructors (
  instructor_id INT64 NOT NULL, # primary_key
  first_name STRING,
  last_name STRING,
  email STRING,
  institution STRING,
  bio STRING,
  join_date DATE
)

CREATE OR REPLACE TABLE data.Modules (
  course_id STRING NOT NULL, # super_key, forign key to courses table
  module_id STRING NOT NULL, # super_key
  module_order INT64,
  module_description STRING,
)

CREATE OR REPLACE TABLE data.Items (
  module_id STRING NOT NULL, # super_key, forign key to modules table
  item_id STRING NOT NULL, # super_key
  item_type STRING,
  item_week STRING,
  item_order INT64,
  item_content STRING,
)

CREATE OR REPLACE TABLE data.Offerings (
  course_id STRING NOT NULL, # super_key, forign key to courses table
  start_date DATE NOT NULL, # super_key
  end_date DATE,
)


CREATE OR REPLACE TABLE data.Registrations (
  user_id INT64 NOT NULL, # super_key, forign key to users table
  course_id STRING NOT NULL, # super_key, forign key to courses table
  registration_date DATE,
  completion_date DATE
)

CREATE OR REPLACE TABLE data.Activity (
  user_id INT64 NOT NULL, # super_key, forign key to users table
  course_id STRING NOT NULL, # super_key, forign key to courses table
  module_id STRING NOT NULL, # super_key, forign key to modules table
  item_id STRING NOT NULL, # super_key, forign key to items table
  activity_type STRING, # ex: start, complete, view
  activity_ts TIMESTAMP
)

'''Load raw data from course_funnel_assignment.csv to course-funnel-assignment.data.raw_data first.
Then insert results of each of below query to populate the tables'''

# populate Users table
SELECT DISTINCT user_id FROM course-funnel-assignment.data.raw_data

# populate Courses table
SELECT DISTINCT course_id FROM course-funnel-assignment.data.raw_data

# populate Modules table
SELECT DISTINCT course_id, module_id, module_order FROM course-funnel-assignment.data.raw_data

# populate Items table
SELECT DISTINCT module_id , item_id FROM course-funnel-assignment.data.raw_data

# populate Offerings table
SELECT course_id, MIN(DATE(item_start_ts)) AS start_date , MAX(DATE( item_complete_ts )) AS end_date
FROM course-funnel-assignment.data.raw_data
GROUP BY course_id

# populate Registrations table
SELECT user_id, course_id, MIN(DATE(item_start_ts)) AS registration_date FROM course-funnel-assignment.data.raw_data
GROUP BY user_id, course_id

# populate Activity table
SELECT user_id, course_id, item_id, module_id, item_start_ts AS activity_ts, 'start' AS activity_type FROM course-funnel-assignment.data.raw_data
UNION ALL
SELECT user_id, course_id, item_id, module_id, item_complete_ts AS activity_ts, 'complete' AS activity_type FROM course-funnel-assignment.data.raw_data
WHERE item_complete_ts IS NOT NULL
