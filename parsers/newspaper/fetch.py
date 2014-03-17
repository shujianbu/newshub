import newspaper
import os
import sys
import re
import MySQLdb

from time import gmtime, strftime
from newspaper import Config

reload(sys)
sys.setdefaultencoding('utf-8')



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

	upload_meta(url, title, domain, text)

def get_articles():

	# get Chinese articles
	for url in open("list_ch.txt", 'r'):
		try: 
			paper = newspaper.build(url, memoize_articles = True, language = 'zh')
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)

			for article in paper.articles:
				get_meta(article, domain)
		
		except:
			pass

	# get English articles
	for url in open("list_en.txt", 'r'):
		try:
			paper = newspaper.build(url, memoize_articles = True, language = 'en')
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)

			for article in paper.articles:
				get_meta(article, domain)
		
		except:
			pass

	print "success!"
	return

get_articles()