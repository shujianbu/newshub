import MySQLdb
import sys
from time import gmtime, strftime

gTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

reload(sys)
sys.setdefaultencoding('utf-8')

conn = MySQLdb.connect(host="newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com",
			user="newshub", passwd="columbiacuj", db="Newshub", charset="utf8")

curs = conn.cursor()
curs.execute("SHOW TABLES")

count = curs.execute("SELECT * FROM sampleTable")
print "there are %s records" % count

result = curs.fetchall()
print "*****"
print result
print "*****"

#value = ['', 'title', 'author', 'category', 'url', 'pub_time', 'cur_time', 'content']
value = ['', 'title', 'author', 'category', 'url', 'pub_time', gTime, 'content']
curs.execute("insert into sampleTable values (%s, %s, %s, %s, %s, %s, %s, %s)", value);

conn.commit()
curs.close()
conn.close()

print "success"
