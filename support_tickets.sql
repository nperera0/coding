
CREATE TABLE events AS (
   user_id INTEGER,
   event_ts TIMESTAMP,
   event_key VARCHAR(255),
   event_value VARCHAR(2000),
);

- assume this is all events for just one single course
- assume that event_key = ‘support’ refers to a support event
- assume that event_key = ‘purchase’ refers to paying for a course.


How do you determine the number of people who end up paying for a course after submitting at least two support tickets?

S
S
P
S

WITH all_support AS (
  SELECT user_id, event_ts FROM events WHERE event_key = ‘support’),

WITH all_purchase AS (
  SELECT user_id, event_ts FROM events WHERE event_key = ‘purchase’),

SELECT user_id FROM all_support JOIN all_purchase
ON all_support.user_id = all_purchase.user_id
WHERE all_support.event_ts <  all_purchase.event_ts
GROUP BY user_id
HAVING COUNT(*) > 2
