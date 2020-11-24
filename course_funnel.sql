SELECT
  *
  FROM
    UNNEST(GENERATE_DATE_ARRAY('2016-01-01', '2016-12-31', INTERVAL 1 DAY)) AS example


    WITH dates AS (
SELECT date FROM UNNEST(GENERATE_DATE_ARRAY('2016-01-01', '2016-12-31', INTERVAL 1 DAY)) AS date),

Weekly_Course_Actives AS (
SELECT dates.date, course_id, COUNT(DISTINCT user_id) AS Weekly_Course_Actives FROM `course-funnel-assignment.data.raw_data` JOIN dates
ON DATE(item_start_ts) >= DATE_SUB(dates.date, INTERVAL 6 DAY) AND DATE(item_start_ts) <= dates.date
GROUP BY dates.date, course_id
ORDER BY dates.date, course_id )



'''
ans #b
SELECT started_cur_7_day.date, started_cur_7_day.course_id, COUNT(DISTINCT started_cur_7_day.user_id) FROM started_cur_7_day JOIN started_prev_7_day
ON started_cur_7_day.date = started_prev_7_day.date AND started_cur_7_day.course_id = started_prev_7_day.course_id AND started_cur_7_day.user_id = started_prev_7_day.user_id
GROUP BY started_cur_7_day.date, started_cur_7_day.course_id
ORDER BY started_cur_7_day.date, started_cur_7_day.course_id
'''

'''
ans #c
SELECT  started_cur_7_day.date, started_cur_7_day.course_id, COUNT(DISTINCT started_cur_7_day.user_id) FROM started_cur_7_day JOIN completed_modules_in_past
ON started_cur_7_day.date = completed_module_in_past.date AND started_cur_7_day.course_id = completed_modules_in_past.course_id
  AND started_cur_7_day.user_id = completed_modules_in_past.user_id AND started_cur_7_day.module_id != completed_modules_in_past.module_id
GROUP BY started_cur_7_day.date, started_cur_7_day.course_id
ORDER BY started_cur_7_day.date, started_cur_7_day.course_id
'''

'''
#passed the course
SELECT dates.date, course_id, module_id, user_id FROM completed_modules_in_past JOIN dates
ON DATE(item_start_ts) >= DATE_SUB(dates.date, INTERVAL 6 DAY) AND DATE(item_start_ts) <= dates.date
GROUP BY dates.date, course_id, module_id, user_id
ORDER BY dates.date, course_id, module_id, user_id
'''



WITH dates AS (
SELECT date FROM UNNEST(GENERATE_DATE_ARRAY('2016-01-01', '2016-12-31', INTERVAL 1 DAY)) AS date),

started_cur_7_day AS (
SELECT dates.date, course_id, module_id, user_id FROM `course-funnel-assignment.data.raw_data` JOIN dates
ON DATE(item_start_ts) >= DATE_SUB(dates.date, INTERVAL 6 DAY) AND DATE(item_start_ts) <= dates.date
GROUP BY dates.date, course_id, module_id, user_id
ORDER BY dates.date, course_id, module_id, user_id ),


started_prev_7_day AS (
SELECT dates.date, course_id, user_id FROM `course-funnel-assignment.data.raw_data` JOIN dates
ON DATE(item_start_ts) >= DATE_SUB(dates.date, INTERVAL 13 DAY) AND DATE(item_start_ts) <= DATE_SUB(dates.date, INTERVAL 7 DAY)
GROUP BY dates.date, course_id, user_id
ORDER BY dates.date, course_id, user_id)#,

#completed_modules_in_past AS (
SELECT dates.date, course_id, module_id, user_id,  FROM `course-funnel-assignment.data.raw_data` JOIN dates
ON DATE(item_complete_ts) <= dates.date
GROUP BY dates.date, course_id, module_id, user_id
HAVING COUNT(item_id) >= 4
ORDER BY dates.date, course_id, module_id, user_id
#)
