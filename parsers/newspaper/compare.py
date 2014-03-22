import diff_match_patch
import sys
import xml.etree.ElementTree as ET

from sys import argv

reload(sys)
sys.setdefaultencoding('UTF8')

def get_articles():
	tree = ET.parse("DB_updated.xml")
	root = tree.getroot()

	# initialization
	url_a = None
	content_a = None
	title_a = None
	domain_a = None
	time_check_a = None
	time_pub_a = None
	#author_a = None
	target_a = None

	for entry in root.findall("./row"):
		url_b = entry.find("field[@name='url']").text
		content_b = entry.find("field[@name='Content']").text
		title_b = entry.find("field[@name='Title']").text
		domain_b = entry.find("field[@name='Domain']").text
		time_check_b = entry.find("field[@name='Time_Check']").text
		time_pub_b = entry.find("field[@name='Time_Publish']").text
		#author_b = entry.find("field[@name='Author']").text
		
		target_b = "URL:\n" + url_b + '\n\n'
		target_b = target_b + "Title:\n" + str(content_b) + '\n\n'
		target_b = target_b + "Domain:\n" + domain_b + '\n\n'
		target_b = target_b + "Time_Publish:\n" + time_pub_b + '\n\n'
		target_b = target_b + "Time_Check:\n" + time_check_b + '\n\n'
		target_b = target_b + "Content:\n" + str(content_b) + '\n\n'

		print target_b

		if(url_a == url_b):
			dmp = diff_match_patch.diff_match_patch()
			
			if(target_a == None):
				target_a = "#### This article is empty ####"
			if(target_b == None):
				target_b = "#### This article is empty ####"

			compare_articles(target_a, target_b)
		
		url_a = url_b
		content_a = content_b
		title_a = title_b
		domain_a = domain_b
		time_check_a = time_check_b
		time_pub_a = time_pub_b
		target_a = target_b

	return


def compare_articles(target_a, target_b):
	##f_output = open(arg_0, 'w')
	f_output = open("output.html", 'a')

	dmp = diff_match_patch.diff_match_patch()
	diffs = dmp.diff_main(target_a, target_b)
	output_html = dmp.diff_prettyHtml(diffs)

	f_output.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/>")
	f_output.write(output_html)

	return


get_articles()

'''
*********************************************

reload(sys)
sys.setdefaultencoding('UTF8')

arg_0, arg_1, arg_2, arg_3 = argv

f_read_1 = open(arg_1, 'r')
f_read_2 = open(arg_2, 'r')
f_write = open(arg_3, 'w')


data1 = f_read_1.read()
data2 = f_read_2.read()

dmp = diff_match_patch.diff_match_patch()

def comp(t1, t2):
        diffs = dmp.diff_main(t1, t2)
        dmp.diff_cleanupSemantic(diffs)
        output_html = dmp.diff_prettyHtml(diffs)
        #output_html.decode('utf-8')
        #output_html.encode('utf-8')

        f_write.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/>")
        f_write.write(output_html)
        return

comp(data1, data2)

f_read_1.close()
f_read_2.close()
f_write.close()
'''