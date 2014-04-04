import diff_match_patch
import sys
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
	encodingMark = True
	counter = 0

	dict_a['url_a'] = None
	dict_a['content_a'] = None
	dict_a['title_a'] = None
	dict_a['domain_a'] = None
	dict_a['time_check_a'] = None
	dict_a['time_pub_a'] = None

	for entry in root.findall("./row"):
		url_b = entry.find("field[@name='url']").text
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
			if(encodingMark == True):
				f_output = open("output.html", 'w')
				f_output.truncate();

				f_output.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/> \n")
				f_output.write("<link href=\"style.css\" rel=\"stylesheet\"> \n\n")
				f_output.close()

				encodingMark = False

			compare_articles(dict_a, dict_b, newArticle, counter)
			counter = counter + 1
			newArticle = False

			print newArticle

		else:
			newArticle = True
			print newArticle

		dict_a['url_a'] = dict_b['url_b']
		dict_a['content_a'] = dict_b['content_b']
		dict_a['title_a'] = dict_b['title_b']
		dict_a['domain_a'] = dict_b['domain_b']
		dict_a['time_check_a'] = dict_b['time_check_b']
		dict_a['time_pub_a'] = dict_b['time_pub_b']

	return


def compare_articles(dict_a, dict_b, newArticle, counter):
	##f_output = open(arg_0, 'w')
	f_output = open("output.html", 'a')

	if(dict_a['content_a'] == None):
		dict_a['content_a'] = "#### This article is empty ####"
	if(dict_b['content_b'] == None):
		dict_b['content_b'] = "#### This article is empty ####"

	content_a = dict_a['content_a']
	content_b = dict_b['content_b']

	dmp = diff_match_patch.diff_match_patch()
	diffs = dmp.diff_main(content_a, content_b)
	output_html = dmp.diff_prettyHtml(diffs)

	url = dict_a['url_a']
	title = dict_a['title_a']
	domain = dict_a['domain_a']
	time_pub = dict_a['time_pub_a']
	time_check = dict_b['time_check_b']
	articleID = "arcDiff_" + str(counter)

	if(newArticle == True):
		f_output.write("<section id=\"header\"> \n<div class=\"articleUrl\"> \nURL: <span>")	
		f_output.write(url)
		f_output.write("</span> \n</div> \n<br> \n<div class=\"articleTitle\"> \nTitle: ")
		f_output.write(title)
		f_output.write("</span> \n</div> \n<br> \n<div class=\"articleDomain\"> \nDomain: ")
		f_output.write(domain)
		f_output.write("\n</div> \n<br> \n</section> \n\n")

	f_output.write("<section id=\"")
	f_output.write(articleID)
	f_output.write("\"> \n<div class=\"articleDiff\"> \n")
	f_output.write(output_html)
	f_output.write("\n</div> \n\n")

	f_output.write("\n<div class=\"articleMeta\"> \n<br> \nTime_Publish:<br> \n<div class=\"articleMeta_publishTime\">")
	f_output.write(time_pub)
	f_output.write("</div><br> \n")
	
	f_output.write("\nTime_Check:<br> \n<class=\"articleMeta_checkTime\">")
	f_output.write(time_check)

	#f_output.write("</span><del style=\"background:#ffe6e6;\">19</del><ins style=\"background:#e6ffe6;\">22</ins><span> </span><ins style=\"background:#e6ffe6;\">2</ins><span>0</span><del style=\"background:#ffe6e6;\">1</del><span>:</span><del style=\"background:#ffe6e6;\">4</del><span>1</span><ins style=\"background:#e6ffe6;\">5</ins><span>:</span><del style=\"background:#ffe6e6;\">22</del><ins style=\"background:#e6ffe6;\">30</ins></div><br><br> \n</div> \n</section>\n\n\n")
	f_output.write("</div><br> \n</div> \n</section>\n\n\n")

	return


get_articles()