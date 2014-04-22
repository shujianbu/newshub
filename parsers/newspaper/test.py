import os
import sys
import diff_match_patch
import MySQLdb
import xml.etree.ElementTree as ET

from newspaper import Article
from time import gmtime, strftime

url_urls = 'http://china.caixin.com/2013-12-30/100623243.html'

a_zh = Article(url_urls, language = 'zh')
a_zh.download()
a_zh.parse()
content_urls = a_zh.text

print "** ", content_urls

if(content_urls == ''):
	a_en = Article(url_urls, language = 'en')
	a_en.download()
	a_en.parse()
	content_urls = content_urls + a_en.text

print "######### ", content_urls