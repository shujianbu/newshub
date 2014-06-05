import os

db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
db_authenticate = " -u newshub -pcolumbiacuj -e \"use Newshub; "

# build the query for database table articles
db_query_selected = "select * from articles order by url ASC, Time_Check DESC\""

# get entries of the selected domain from articles
db_connect = db_identify + db_authenticate + db_query_selected + " > DB_updated.xml"
os.system(db_connect)


# build the query for database table deletions
db_query_selected = "select * from deletions order by url ASC, Time_Check DESC\""

# get entries of the selected domain from deletions
db_connect = db_identify + db_authenticate + db_query_selected + " > DB_deleted.xml"
os.system(db_connect)

os.system("python compare.py")
