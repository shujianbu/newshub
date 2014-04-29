import os
import sys
import diff_match_patch
import MySQLdb
import xml.etree.ElementTree as ET
import httplib2

from newspaper import Article
from time import gmtime, strftime

# this file is used to traver DB_urls and return the article content from newspaper
# then compare the content with the corresponding ones in DB_stored

reload(sys)
sys.setdefaultencoding('utf-8')

def upload_meta(articleExists, url, title, author, domain, time_pub, text):
	gTime = strftime("%Y-%m-%d %H:%M:%S", gmtime())

	conn = MySQLdb.connect(host="newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com",
			user="newshub", passwd="columbiacuj", db="Newshub", charset="utf8")
	cursor = conn.cursor()

	# since we cannot get the author attribute, so we use the word "author" instead
	value = ['', title, author, domain, url, time_pub, gTime, text]
	
	if(articleExists == True):
		cursor.execute("insert into articles values (%s, %s, %s, %s, %s, %s, %s, %s)", value);
	else:
		cursor.execute("insert into deletions values (%s, %s, %s, %s, %s, %s, %s, %s)", value);

	conn.commit()
	cursor.close()
	conn.close()

	if(articleExists == True):
		print "upload an updated article"
	else:
		conn = MySQLdb.connect(host="newshub.c5dehgoxr0wn.us-west-2.rds.amazonaws.com",
				user="newshub", passwd="columbiacuj", db="Newshub", charset="utf8")
		cursor = conn.cursor()

		cursor.execute("delete from deletions where URL=\'url\'")
		conn.commit()
		cursor.close()
		conn.close()

		print "move a deleted article"

def compare_article(url_urls, content_urls):
	tree_stored = ET.parse("DB_stored.xml")
	root_stored = tree_stored.getroot()
	detected = False

	for entry in root_stored.findall("./row"):
		url_stored = entry.find("field[@name='URL']").text

		if(url_stored == url_urls):
			detected = True

			content_stored = entry.find("field[@name='Content']").text

		#	print content_stored
			# This is to compare the two articles to see if there are changes
			dmp = diff_match_patch.diff_match_patch()

			'''
			if(content_urls == ''):
				content_urls = None
			'''

			# check if the article is empty or not
			if(content_urls != None and content_stored != None):
				diffs = dmp.diff_main(content_urls, content_stored)
				changes = dmp.diff_levenshtein(diffs)
			
			'''
			elif(content_urls == None and content_stored == None):
				changes = 0					
			else:
				changes = 1
			'''

			if(changes > 0):
				title_stored = entry.find("field[@name='Title']").text
				author_stored = entry.find("field[@name='Author']").text
				domain_stored = entry.find("field[@name='Domain']").text
				time_pub_stored = entry.find("field[@name='Time_Publish']").text

				articleExists = True
				upload_meta(articleExists, url_stored, title_stored, author_stored, domain_stored, \
					time_pub_stored, content_urls)
			
		elif(detected == False):
			continue
		else:
			break

def move2deletion(url_urls):
	tree_stored = ET.parse("DB_stored.xml")
	root_stored = tree_stored.getroot()
	detected = False

	print "move2deletion executed"

	for entry in root_stored.findall("./row"):
		url_stored = entry.find("field[@name='URL']").text

		if(url_stored == url_urls):
			detected = True

			title_stored = entry.find("field[@name='Title']").text
			author_stored = entry.find("field[@name='Author']").text
			domain_stored = entry.find("field[@name='Domain']").text
			time_pub_stored = entry.find("field[@name='Time_Publish']").text
			content_stored = entry.find("field[@name='Content']").text

			articleExists = False
			upload_meta(articleExists, url_stored, title_stored, author_stored, domain_stored, \
				time_pub_stored, content_stored)
			break

		elif(detected == False):
			continue
		else:
			break


def get_article():
	tree_urls = ET.parse("DB_urls.xml")
	root_urls = tree_urls.getroot()

	# The problem with English and Chinese can be solved with 
	for field_urls in root_urls.findall("row"):
		url_urls = field_urls.find("field").text
	#	url_urls = 'http://news.sina.com.cn/c/2014-04-21/204729980947.shtml'
	#	url_urls = 'http://china.caixin.com/2013-12-30/100623243.html'

		try:
			h = httplib2.Http()
			resp = h.request(url_urls, 'HEAD')
			status = int(resp[0]['status'])

			if(status >= 500 or status == 400 or status == 404 or status == 408 or status == 410):
				a_zh = Article(url_urls, language = 'zh')
				a_zh.download()
				a_zh.parse()
				content_urls = a_zh.text

				if(content_urls == ''):
					a_en = Article(url_urls, language = 'en')
					a_en.download()
					a_en.parse()
					content_urls = content_urls + a_en.text

				if(content_urls != ''):
					compare_article(url_urls, content_urls)
			else:
				move2deletion(url_urls)
		except:
			pass


if __name__ == "__main__":
	get_article()