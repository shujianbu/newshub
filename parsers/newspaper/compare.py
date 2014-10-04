import diff_match_patch
import sys
import json
import xml.etree.ElementTree as ET

from sys import argv

reload(sys)
sys.setdefaultencoding('UTF8')

def get_articles():
	tree = ET.parse("DB_updated.xml")
	root = tree.getroot()

	dict_a = {}
	dict_b = {}
	newArticle = True
	firstComma = True
	counter = 0

	dict_a['url_a'] = None
	dict_a['content_a'] = None
	dict_a['title_a'] = None
	dict_a['domain_a'] = None
	dict_a['time_check_a'] = None
	dict_a['time_pub_a'] = None

	f_output = open("output_compare.json", 'w')
	f_output.truncate()
	f_output.write("{\"compare\":[")
	f_output.close()

	for entry in root.findall("./row"):
		url_b = entry.find("field[@name='URL']").text
		content_b = entry.find("field[@name='Content']").text
		title_b = entry.find("field[@name='Title']").text
		domain_b = entry.find("field[@name='Domain']").text
		time_check_b = entry.find("field[@name='Time_Check']").text
		time_pub_b = entry.find("field[@name='Time_Publish']").text

		dict_b['url_b'] = url_b
		dict_b['content_b'] = content_b
		dict_b['title_b'] = title_b
		dict_b['domain_b'] = domain_b
		dict_b['time_check_b'] = time_check_b
		dict_b['time_pub_b'] = time_pub_b

		if(dict_a['url_a'] == dict_b['url_b']):
			
			"""
			if(encodingMark == True):
				f_output = open("output_compare.html", 'w')
				f_output.truncate();

				f_output.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/> \n")
				f_output.write("<link href=\"style.css\" rel=\"stylesheet\"> \n\n")
				f_output.close()

				encodingMark = False
			"""

			if(firstComma == True):
				compare_articles(dict_a, dict_b, newArticle, counter, True)
				firstComma = False
			else:
				compare_articles(dict_a, dict_b, newArticle, counter, False)
			counter = counter + 1
			newArticle = False

		else:
			newArticle = True

		dict_a['url_a'] = dict_b['url_b']
		dict_a['content_a'] = dict_b['content_b']
		dict_a['title_a'] = dict_b['title_b']
		dict_a['domain_a'] = dict_b['domain_b']
		dict_a['time_check_a'] = dict_b['time_check_b']
		dict_a['time_pub_a'] = dict_b['time_pub_b']

	f_output = open("output_compare.json", 'a')
	f_output.write("]}")

	return

def get_deletions():
	tree = ET.parse("DB_deleted.xml")
	root = tree.getroot()

	dict_del = {}
	firstComma = True

	dict_del['url_a'] = None
	dict_del['content_a'] = None
	dict_del['title_a'] = None
	dict_del['domain_a'] = None
	dict_del['time_check_a'] = None
	dict_del['time_pub_a'] = None

	f_output = open("output_deleted.json", 'w')
	f_output.truncate()
	f_output.write("{\"deleted\":[")
	#f_output.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/> \n")
	#f_output.write("<link href=\"style.css\" rel=\"stylesheet\"> \n\n")
	f_output.close()

	for entry in root.findall("./row"):
		url = entry.find("field[@name='URL']").text
		content = entry.find("field[@name='Content']").text
		title = entry.find("field[@name='Title']").text
		domain = entry.find("field[@name='Domain']").text
		time_check = entry.find("field[@name='Time_Check']").text
		time_pub = entry.find("field[@name='Time_Publish']").text

		dict_del['url'] = url
		dict_del['title'] = title
		dict_del['domain'] = domain
		dict_del['content'] = content
		dict_del['time_pub'] = time_pub
		dict_del['time_check'] = time_check

		if(firstComma == True):
			get_deleted_articles(dict_del, True)
			firstComma = False
		else:
			get_deleted_articles(dict_del, False)

	f_output = open("output_deleted.json", 'a')
	f_output.write("]}")
	#f_output.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/> \n")
	#f_output.write("<link href=\"style.css\" rel=\"stylesheet\"> \n\n")
	f_output.close()

	return

def get_deleted_articles(dict_del, firstComma):
	f_output = open("output_deleted.json", 'a')

	if(dict_del['content'] == None):
		dict_del['content'] = "#### This article is empty ####"

	encoded_del = json.dumps(dict_del)

	#f_output.write('\n')
	if(firstComma == False):
		f_output.write(',')
	f_output.write(encoded_del)
	#f_output.write('\n')

	'''
	url = dict_del['url']
	title = dict_del['title']
	domain = dict_del['domain']
	content = dict_del['content']
	time_pub = dict_del['time_pub']
	time_check = dict_del['time_check']
	'''

	'''
	f_output.write("<section id=\"header\"> \n<div class=\"articleUrl\"> \nURL: <span>")	
	f_output.write(url)
	f_output.write("</span> \n</div> \n<br> \n<div class=\"articleTitle\"> \nTitle: ")
	f_output.write(title)
	f_output.write("</span> \n</div> \n<br> \n<div class=\"articleDomain\"> \nDomain: ")
	f_output.write(domain)
	f_output.write("\n</div> \n<br> \n</section> \n\n")

	f_output.write("\n<div class=\"articleDiff\"> \n")
	f_output.write(content)
	f_output.write("\n</div> \n\n")

	f_output.write("\n<div class=\"articleMeta\"> \n<br> \nTime_Publish:<br> \n<div class=\"articleMeta_publishTime\">")
	f_output.write(time_pub)
	f_output.write("</div><br> \n")
	
	f_output.write("\nTime_Check:<br> \n<class=\"articleMeta_checkTime\">")
	f_output.write(time_check)

	f_output.write("</div><br> \n</div> \n</section>\n\n\n")
	'''

	f_output.close()

	return

def compare_articles(dict_a, dict_b, newArticle, counter, firstComma):
	##f_output = open(arg_0, 'w')
	f_output = open("output_compare.json", 'a')
	output_json = {}

	
	if(dict_a['content_a'] == None):
		dict_a['content_a'] = "#### This article is empty ####"
	if(dict_b['content_b'] == None):
		dict_b['content_b'] = "#### This article is empty ####"
	
	if(dict_a['title_a'] == None):
		dict_a['title_a'] = "None"
	if(dict_b['title_b'] == None):
		dict_b['title_b'] = "None"


	content_a = dict_a['content_a']
	content_b = dict_b['content_b']

	dmp = diff_match_patch.diff_match_patch()
	diffs_content = dmp.diff_main(content_a, content_b)
	changes = dmp.diff_levenshtein(diffs_content)

	if(changes > 0):
		dmp.diff_cleanupSemantic(diffs_content)
		output_content = dmp.diff_prettyHtml(diffs_content)
		'''
		output_content_ins = dmp.diff_pretty_ins(diffs_content)
		output_content_del = dmp.diff_pretty_del(diffs_content)
		output_content_eql = dmp.diff_pretty_eql(diffs_content)
		'''

		'''
		diffs_title = dmp.diff_main(dict_a['title_a'], dict_b['title_b'])
		output_title_ins = dmp.diff_pretty_ins(diffs_title)
		output_title_del = dmp.diff_pretty_del(diffs_title)
		output_title_eql = dmp.diff_pretty_eql(diffs_title)
		'''

		url = dict_a['url_a']
		domain = dict_a['domain_a']
		title = dict_a['title_a']
		time_pub = dict_a['time_pub_a']
		time_check = dict_a['time_check_a']
		articleID = "arcDiff_" + str(counter)

		'''
		output_content = {}
		output_title = {}


		output_content['content_ins'] = output_content_ins
		output_content['content_del'] = output_content_del
		output_content['content_eql'] = output_content_eql

		output_title['title_ins'] = output_title_ins
		output_title['title_del'] = output_title_del
		output_title['title_eql'] = output_title_eql
		'''

		output_json['url'] = url
		output_json['domain'] = domain
		output_json['title'] = title
		output_json['time_check'] = time_check
		output_json['time_pub'] = time_pub
		output_json['articleID'] = articleID
		#output_json['title'] = output_title
		output_json['content'] = output_content

		encoded_cmp = json.dumps(output_json)

		if(firstComma == False):
			f_output.write(',')

		f_output.write(encoded_cmp)
		#f_output.write(',')

		'''
		if(newArticle == True):
			f_output.write("<section id=\"header\"> \n<div class=\"articleUrl\"> \nURL: <span>")	
			f_output.write(url)
			f_output.write("</span> \n</div> \n<br> \n<div class=\"articleTitle\"> \nTitle: ")
			f_output.write(output_title)
			f_output.write("</span> \n</div> \n<br> \n<div class=\"articleDomain\"> \nDomain: ")
			f_output.write(output_domain)
			f_output.write("\n</div> \n<br> \n</section> \n\n")
		'''

		'''
		f_output.write("<section id=\"")
		f_output.write(articleID)
		f_output.write("\"> \n<div class=\"articleDiff\"> \n")
		f_output.write(output_content)
		f_output.write("\n</div> \n\n")

		f_output.write("\n<div class=\"articleMeta\"> \n<br> \nTime_Publish:<br> \n<div class=\"articleMeta_publishTime\">")
		f_output.write(time_pub)
		f_output.write("</div><br> \n")
		
		f_output.write("\nTime_Check:<br> \n<div class=\"articleMeta_checkTime\">")
		f_output.write(time_check)
		f_output.write("</div><br> \n")

		#f_output.write("</span><del style=\"background:#ffe6e6;\">19</del><ins style=\"background:#e6ffe6;\">22</ins><span> </span><ins style=\"background:#e6ffe6;\">2</ins><span>0</span><del style=\"background:#ffe6e6;\">1</del><span>:</span><del style=\"background:#ffe6e6;\">4</del><span>1</span><ins style=\"background:#e6ffe6;\">5</ins><span>:</span><del style=\"background:#ffe6e6;\">22</del><ins style=\"background:#e6ffe6;\">30</ins></div><br><br> \n</div> \n</section>\n\n\n")
		f_output.write("</div><br> \n</div> \n</section>\n\n\n")
		'''



	f_output.close()

	return firstComma


if __name__ == "__main__":
	# get_articles()
	get_deletions()
