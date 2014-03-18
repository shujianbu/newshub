import newspaper
import os
import sys
import re
import MySQLdb

from time import gmtime, strftime
from newspaper import Config
from xml.dom.minidom import parse

reload(sys)
sys.setdefaultencoding('utf-8')

def get_table():
	db_identify = "mysql -X --default-character-set=utf8 -h newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com"
	db_authenticate = " -u newshub -pcolumbiacuj"
	db_query = "\"use Newshub; select * from sampleTable order by url, Time_Check\""
	db_connect = db_identify + db_authenticate + " -e " + db_query + " > DB_initial.xml"

	# the DB file is ordered by url and Time_Check.
	os.system(db_connect)
	print "DB_initial is downloaded"

def upload_meta(url, title, domain, text):
	gTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	conn = MySQLdb.connect(host="newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com",
			user="newshub", passwd="columbiacuj", db="Newshub", charset="utf8")
	cursor = conn.cursor()

	# since we cannot get the author attribute, so we use the word "author" instead
	value = ['', title, 'author', domain, url, gTime, gTime, text]
	cursor.execute("insert into sampleTable values (%s, %s, %s, %s, %s, %s, %s, %s)", value);

	conn.commit()
	cursor.close()
	conn.close()

	print "upload an article"

def get_meta(article, domain):
	article.download()
	article.parse()

	url = article.url
	title = article.title
	text = article.text

	# need to detect whether the article is in the table or not

	upload_meta(url, title, domain, text)

def get_articles():
	# get the initial table before detecting new papers
	get_table()

	# get Chinese articles
	i = 0
	for url in open("list_ch.txt", 'r'):
		try: 
			paper = newspaper.build(url, memoize_articles = True, language = 'zh')
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)

			for article in paper.articles:
				get_meta(article, domain)

				i = i + 1
				if(i > 2):
					break
		except:
			pass

		if(i > 2):
			break

	# get English articles
	j = 0
	for url in open("list_en.txt", 'r'):
		try:
			paper = newspaper.build(url, memoize_articles = True, language = 'en')
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)

			for article in paper.articles:
				get_meta(article, domain)

				j = j + 1
				if(j > 2):
					break
		except:
			pass

		if(j > 2):
			break

	print "success!"
	return

get_articles()