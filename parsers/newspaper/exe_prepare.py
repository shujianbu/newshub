import os

db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
db_authenticate = " -u newshub -pcolumbiacuj -e \"use Newshub; "

db_query_distinct = "select distinct url from sampleTable order by url ASC\""
db_query_order = "select * from sampleTable order by url ASC, Time_Check DESC\""

# get all distinct urls stored in the DB
db_connect = db_identify + db_authenticate + db_query_distinct + " > DB_urls.xml"
#print db_connect
os.system(db_connect)

# get all entries in the DB ordered by their urls and time_check
db_connect = db_identify + db_authenticate + db_query_order + " > DB_stored.xml"
#print db_connect
os.system(db_connect)




# after the execution of fetching new articles and updating existing articles
# we can now compared the different versions of articles that are stored in the DB

db_query_order = "select * from sampleTable order by url ASC, Time_Check DESC\""
db_connect = db_identify + db_authenticate + db_query_order + " > DB_updated.xml"
#print db_connect
os.system(db_connect)