import newspaper
import sys
import re
import MySQLdb
import urllib2
import feedparser

from time import gmtime, strftime
from newspaper import Article
#from newspaper import Config
#from xml.dom.minidom import parse

reload(sys)
sys.setdefaultencoding('utf-8')

def upload_meta(url, title, domain, text):
	gTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	conn = MySQLdb.connect(host="newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com",
			user="newshub", passwd="columbiacuj", db="Newshub", charset="utf8")
	cursor = conn.cursor()

	# since we cannot get the author attribute, so we use the word "author" instead
	value = ['', title, 'author', domain, url, gTime, gTime, text]
	cursor.execute("insert into articles values (%s, %s, %s, %s, %s, %s, %s, %s)", value);

	conn.commit()
	cursor.close()
	conn.close()

	print "upload an article"

def get_meta_rss(link, domain, chinese):
	if(chinese):
		a = Article(link, language = "zh")
	else:
		a = Article(link, language = "en")

	a.download()
	a.parse()

	url = link
	title = a.title
	text = a.text

	if(text != '' and text != None and len(str(text)) > 0):
		upload_meta(url, title, domain, text)
	else:
		print "content of the article is empty"

def get_meta(article, domain):
	article.download()
	article.parse()

	url = article.url
	title = article.title
	text = article.text

	# if the content is empty, the article will not be uploaded
	if(text != '' and text != None and len(str(text)) > 0):
		# if the content is merely 404 information, the article will not be uploaded either
		response = urllib2.urlopen(url)
		status = response.code

		if(status != 404):
			upload_meta(url, title, domain, text)
	else:
		print "content of the article is empty"

def get_articles():
	# get Chinese articles from domain
	for url in open("list_ch.txt", 'r'):
		try: 
			paper = newspaper.build(url, memoize_articles = True, language = 'zh')
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)

			for article in paper.articles:
				get_meta(article, domain)

		except:
			pass


	# get English articles from domain
	for url in open("list_en.txt", 'r'):
		try:
			paper = newspaper.build(url, memoize_articles = True, language = 'en')
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)

			for article in paper.articles:
				get_meta(article, domain)

		except:
			pass


	# get articles from RSS
	for url in open("list_rss_ch.txt", 'r'):
		try:
			feed = feedparser.parse(url)
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)
			chinese = True

			for post in feed.entries:
				link = post.link
				get_meta_rss(link, domain, chinese)

		except:
			pass

	for url in open("list_rss_en.txt", 'r'):
		try:
			feed = feedparser.parse(url)
			match_object = re.search('http\:\/\/([^\/]+)\/', url)
			domain = match_object.group(1)
			chinese = False

			for post in feed.entries:
				link = post.link
				get_meta_rss(link, domain, chinese)

		except:
			pass

	print "success!"
	return


if __name__ == "__main__":
	get_articles()
