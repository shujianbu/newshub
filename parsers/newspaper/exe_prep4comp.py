import os

domain = raw_input("Please input the domain for specific news source, or \"ALL\" for all news sources:\n")

db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
db_authenticate = " -u newshub -pcolumbiacuj -e \"use Newshub; "

# build the query for database table articles
if(domain == "ALL"):
	db_query_selected = "select * from articles order by url ASC, Time_Check DESC\""
else:
	db_query_selected = "select * from articles where Domain= \\\"" + domain + "\\\" order by url ASC, Time_Check DESC\""

# get entries of the selected domain from articles
db_connect = db_identify + db_authenticate + db_query_selected + " > DB_updated.xml"
os.system(db_connect)


# build the query for database table deletions
if(domain == "ALL"):
	db_query_selected = "select * from deletions order by url ASC, Time_Check DESC\""
else:
	db_query_selected = "select * from deletions where Domain= \\\"" + domain + "\\\" order by url ASC, Time_Check DESC\""

# get entries of the selected domain from deletions
db_connect = db_identify + db_authenticate + db_query_selected + " > DB_deleted.xml"
os.system(db_connect)