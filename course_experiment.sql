

Tables

courses
"course_id","class_size"

course_ownership
"course_id","prof_id"

experiments
"experiment_id","course_id"

professors
"prof_id","name","email","created_at","is_tophat"

responses
"response_id","created_at","course_id","response","correct"


WITH experiment_courses AS (
  SELECT  experiment_id,  course_id FROM experiments
  WHERE experiment_id = '257'
)

correct_responses_test AS (
  SELECT experiment_id, correct FROM responses JOIN experiment_courses ON responses.course_id = experiment_courses.course_id
  WHERE DATE(created_at) >= DATE('2019-3-1') AND DATE(created_at) <= ('2019-5-1')
)


correct_responses_control AS (
  SELECT experiment_id, correct FROM responses
  WHERE DATE(created_at) >= DATE('2019-3-1') AND DATE(created_at) <= ('2019-5-1')
  AND responses.course_id NOT IN  (SELECT course_id FROM experiment_courses)

)

SELECT CAST( COUNT(CASE WHEN correct = 'TRUE' THEN 1 ELSE 0 END), FLOAT) / CAST( COUNT(*), FLOAT) AS correct_percentage
FROM correct_responses_test
GROUP BY experiment_id
