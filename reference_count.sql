page_views:

cookie_id    page_ts             url                                     referrer
abc          2018-09-01 1:30     www.coursera.org/learn/ml               online.stanford.edu/courses
abc          2018-09-11 2:40     www.coursera.org/browse                 gmail.com
def          2018-09-05 5:40     www.coursera.org                        NULL
ghi          2018-09-15 14:10    www.coursera.org/spn/ds                 m.facebook.com
ghi          2018-09-15 14:20    www.coursera.org                        www.coursera.org/spn/ds


users:

user_id      reg_cookie_id    reg_ts
123          abc              2018-09-01 2:10
456          ghi              2018-09-15 15:20



SELECT referrer, COUNT(DISTINCT cookie_id) cnt FROM page_views
WHERE referrer NOT LIKE `%www.coursera.org%` AND referrer IS NOT NULL
GROUP BY referrer
ORDER BY cnt DESC


SELECT referrer, (CAST(COUNT(DISTINCT users.user_id), FLOAT)/CAST(COUNT(DISTINCT cookie_id), FLOAT))*100.00  percent
FROM page_views LEFT JOIN users
ON page_views.cookie_id = users.reg_cookie_id
GROUP BY referrer
ORDER BY percent DESC





referrer                 reg_users_cnt    reg_rate
paypal.com               100K             98%
github.com               500K             91%
freeonlinetextbooks.com  400K             85%
...
google.com               1M               11%
...
