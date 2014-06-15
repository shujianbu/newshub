import time
import os

# get the date for the first day of the month
current_month = time.strftime('%Y-%m',time.localtime(time.time()))
first_date = current_month + "-01"

# get the month of the year
current_month_only = time.strftime('%m',time.localtime(time.time()))

db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
db_authenticate = " -u newshub -pcolumbiacuj -e \"use Newshub; "

# build the query for database table articles
db_query_selected = "delete from articles where Time_Publish<\"" + first_date + "\";"
db_connect = db_identify + db_authenticate + db_query_selected
os.system(db_connect)

# build the query for database table deletions
'''
if(current_month_only == 01 or current_month_only == 07):
	db_query_selected = "delete from deletions where Time_Publish<\"" + first_date + "\";"
	db_connect = db_identify + db_authenticate + db_query_selected
	os.system(db_connect)
'''
