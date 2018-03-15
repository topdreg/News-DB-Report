# Database API code for connection to the "news" database. 

import psycopg2 
import datetime

DBNAME = "news" 

db = psycopg2.connect(database=DBNAME) 
cursor = db.cursor() 

# Print views of top 3 articles. 

query1 = """select articles.title, count(log.path) as num 
from articles, log 
where log.path like concat('%', articles.slug) 
group by articles.title
order by num desc
limit 3;""" 

cursor.execute(query1) 
info = cursor.fetchall() 
print("The most popular articles of all time are: ") 
for item in info: 
    print(item[0] + " — " + str(item[1]) + " views")
print("\n")

# Print the most popular article authors of all time. 

query2 = """select authors.name, count(articles.author) as numTitle
from authors, articles, log  
where log.path like concat('%', articles.slug) 
and authors.id = articles.author
group by authors.name 
order by numTitle desc;"""

cursor.execute(query2) 
info = cursor.fetchall()
print("The most popular authors of all time are: ") 
for item in info: 
    print(item[0] + " — " + str(item[1]) + " views") 
print("\n")

# Show the days where more than 1% of requests lead to errors. 

query3 = """select date(log.time) as day, 
(sum(case when log.status like '4%' then 1 else 0 end) * 100)::float / 
count(*) as numtime
from log
group by day
having (sum(case when log.status like '4%' then 1 else 0 end) * 100)::float 
/ count(*) > 1;"""

cursor.execute(query3) 
info = cursor.fetchall() 
print("The days where more than 1% of requests lead to errors are: ")  
for item in info: 
    print(datetime.datetime.strptime(str(info[0][0]), 
    '%Y-%m-%d').strftime('%B %d, %Y') + " — " 
    + str(round(item[1], 2)) + "% errors") 
print("\n")
