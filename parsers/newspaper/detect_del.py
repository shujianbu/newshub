import os
import sys
import diff_match_patch
import MySQLdb
import xml.etree.ElementTree as ET
import urllib2
from multiprocessing import Pool


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

		cursor.execute("delete from articles where URL=%s", url)
		conn.commit()
		cursor.close()
		conn.close()

		print "move a deleted article"

def move2deletion(url_urls):
	tree_stored = ET.parse("DB_stored.xml")
	root_stored = tree_stored.getroot()
	detected = False

	#print "move2deletion executed"

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
def f(url):
	url_urls = url.text
	try:
		response = urllib2.urlopen(url_urls)
		status = response.code

		#print "detected webpage code:", status

		if(status == 404):
			move2deletion(url_urls)
		else:
			print "url lives"
			pass

	except:
		pass

def get_article():
	tree_urls = ET.parse("DB_urls.xml")
	root_urls = tree_urls.getroot()


	NUMBER_OF_THREADS = 100
	urls = root_urls.findall("./row/field")
	print "Start Detecting"
	pool = Pool(processes=NUMBER_OF_THREADS)
	pool.map(f, urls)
	thread_size = len(urls)/NUMBER_OF_THREADS

	# The problem with English and Chinese can be solved with 
	# for field_urls in root_urls.findall("row"):
	# 	url_urls = field_urls.find("field").text

	# 	try:
	# 		response = urllib2.urlopen(url_urls)
	# 		status = response.code

	# 		#print "detected webpage code:", status

	# 		if(status == 404):
	# 			move2deletion(url_urls)
	# 		else:
	# 			print "url lives"
	# 			continue

	# 	except:
	# 		pass


if __name__ == "__main__":
	get_article()
