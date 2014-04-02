import os
import sys
import diff_match_patch
import MySQLdb
import xml.etree.ElementTree as ET

from newspaper import Article
from time import gmtime, strftime

# this file is used to traver DB_urls and return the article content from newspaper
# then compare the content with the corresponding ones in DB_stored

reload(sys)
sys.setdefaultencoding('utf-8')

def upload_meta(url, title, author, domain, time_pub, text):
	gTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	conn = MySQLdb.connect(host="newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com",
			user="newshub", passwd="columbiacuj", db="Newshub", charset="utf8")
	cursor = conn.cursor()

	# since we cannot get the author attribute, so we use the word "author" instead
	value = ['', title, author, domain, url, time_pub, gTime, text]
	cursor.execute("insert into sampleTable values (%s, %s, %s, %s, %s, %s, %s, %s)", value);

	conn.commit()
	cursor.close()
	conn.close()

	print "upload an updated article"


def compare_article(url_urls, content_urls):
	tree_stored = ET.parse("DB_stored.xml")
	root_stored = tree_stored.getroot()

	for entry in root_stored.findall("./row"):
			url_stored = entry.find("field[@name='url']").text

			if(url_stored == url_urls):
				content_stored = entry.find("field[@name='Content']").text

				# This is to compare the two articles to see if there are changes
				dmp = diff_match_patch.diff_match_patch()

				# check if the article is empty or not
				if(content_urls != None and content_stored != None):
					diffs = dmp.diff_main(content_urls, content_stored)
					changes = dmp.diff_levenshtein(diffs)
				else:
					changes = 1

				if(changes > 0):
					title_stored = entry.find("field[@name='Title']").text
					author_stored = entry.find("field[@name='Author']").text
					domain_stored = entry.find("field[@name='Domain']").text
					time_pub_stored = entry.find("field[@name='Time_Publish']").text

					upload_meta(url_stored, title_stored, author_stored, domain_stored, \
						time_pub_stored, content_urls)

				break
			else:
				continue

def get_article():
	tree_urls = ET.parse("DB_urls.xml")
	root_urls = tree_urls.getroot()

	# The problem with English and Chinese can be solved with 
	for field_urls in root_urls.findall("row"):
		url_urls = field_urls.find("field").text

		a = Article(url_urls, language='zh')
		a.download()
		a.parse()
		content_urls = a.text
		
		compare_article(url_urls, content_urls)

get_article()