import os

db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
db_authenticate = " -u newshub -pcolumbiacuj"
db_query = "\"use Newshub; select * from sampleTable\"" # can be modified
db_connect = db_identify + db_authenticate + " -e " + db_query + " > a.xml"

print db_connect
os.system(db_connect)

#os.system("mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com\
# -u newshub -pcolumbiacuj -e \"use Newshub; select * from sampleTable;\" > a.xml")