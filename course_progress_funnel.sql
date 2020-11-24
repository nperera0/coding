WITH dates AS (
SELECT date FROM UNNEST(GENERATE_DATE_ARRAY('2016-01-01', '2016-12-31', INTERVAL 1 DAY)) AS date),

courses AS (
SELECT DISTINCT course_id FROM course-funnel-assignment.data.raw_data),

started_cur_7_day AS (
SELECT dates.date, course_id, module_id, user_id FROM `course-funnel-assignment.data.raw_data` JOIN dates
ON DATE(item_start_ts) >= DATE_SUB(dates.date, INTERVAL 6 DAY) AND DATE(item_start_ts) <= dates.date
GROUP BY dates.date, course_id, module_id, user_id ),

started_prev_7_day AS (
SELECT dates.date, course_id, user_id FROM `course-funnel-assignment.data.raw_data` JOIN dates
ON DATE(item_start_ts) >= DATE_SUB(dates.date, INTERVAL 13 DAY) AND DATE(item_start_ts) <= DATE_SUB(dates.date, INTERVAL 7 DAY)
GROUP BY dates.date, course_id, user_id ),

completed_modules_in_past AS (
SELECT * EXCEPT (rank) FROM (
  SELECT dates.date, course_id, module_id, user_id, item_complete_ts, DENSE_RANK() OVER (PARTITION BY course_id, module_id, user_id ORDER BY item_complete_ts) AS rank
  FROM `course-funnel-assignment.data.raw_data` JOIN dates
  ON DATE(item_complete_ts) <= dates.date )
WHERE rank = 4),

weekly_course_actives AS (
SELECT date, course_id, COUNT(DISTINCT user_id) AS cnt FROM started_cur_7_day
GROUP BY date, course_id ),

weekly_course_retained_learners AS (
SELECT cur.date, cur.course_id, COUNT(DISTINCT cur.user_id) AS cnt FROM started_cur_7_day cur JOIN started_prev_7_day prev
ON cur.date = prev.date AND cur.course_id = prev.course_id AND cur.user_id = prev.user_id
GROUP BY cur.date, cur.course_id ),

weekly_course_progressed_learners AS (
SELECT  cur.date, cur.course_id, COUNT(DISTINCT cur.user_id) AS cnt FROM started_cur_7_day cur JOIN completed_modules_in_past comp
ON cur.date = comp.date AND cur.course_id = comp.course_id
  AND cur.user_id = comp.user_id AND cur.module_id != comp.module_id
GROUP BY cur.date, cur.course_id ),

weekly_course_passed_learners AS (
SELECT date, course_id, COUNT(user_id) AS cnt FROM (
  SELECT dates.date, course_id, user_id FROM completed_modules_in_past JOIN dates
  ON DATE(item_complete_ts) >= DATE_SUB(dates.date, INTERVAL 6 DAY) AND DATE(item_complete_ts) <= dates.date
  GROUP BY dates.date, course_id, user_id
  HAVING COUNT(module_id) >= 4 )
GROUP BY date, course_id )

SELECT dates.date, courses.course_id,
  weekly_course_actives.cnt AS Weekly_Course_Actives,
  weekly_course_retained_learners.cnt AS Weekly_Course_Retained_Learners,
  weekly_course_progressed_learners.cnt AS Weekly_Course_Progressed_Learners,
  weekly_course_passed_learners.cnt AS Weekly_Course_Passed_Learners
FROM dates CROSS JOIN courses
  LEFT JOIN weekly_course_actives ON dates.date = weekly_course_actives.date AND courses.course_id = weekly_course_actives.course_id
  LEFT JOIN weekly_course_retained_learners ON dates.date = weekly_course_retained_learners.date AND courses.course_id = weekly_course_retained_learners.course_id
  LEFT JOIN weekly_course_progressed_learners ON dates.date = weekly_course_progressed_learners.date AND courses.course_id = weekly_course_progressed_learners.course_id
  LEFT JOIN weekly_course_passed_learners ON dates.date = weekly_course_passed_learners.date AND courses.course_id = weekly_course_passed_learners.course_id
ORDER BY dates.date, courses.course_id
