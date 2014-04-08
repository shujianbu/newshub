import os

domain = raw_input("Please input the domain for specific news source, or \"ALL\" for all news sources:\n")

db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
db_authenticate = " -u newshub -pcolumbiacuj -e \"use Newshub; "

# build the query for database
db_query_distinct = "select distinct url from articles order by url ASC\""
db_query_all = "select * from articles order by url ASC, Time_Check DESC\""
if(domain == "ALL"):
	db_query_selected = "select * from articles order by url ASC, Time_Check DESC\""
else:
	db_query_selected = "select * from articles where Domain= \\\"" + domain + "\\\" order by url ASC, Time_Check DESC\""

# get all distinct urls stored in the DB
db_connect = db_identify + db_authenticate + db_query_distinct + " > DB_urls.xml"
os.system(db_connect)

# get all entries in the DB ordered by their urls and time_check
db_connect = db_identify + db_authenticate + db_query_all + " > DB_stored.xml"
os.system(db_connect)

# get entries of the selected domain
db_connect = db_identify + db_authenticate + db_query_selected + " > DB_updated.xml"
os.system(db_connect)