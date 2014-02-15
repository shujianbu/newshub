import diff_match_patch
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

'''
with open("Shujian-A1-V1-2014-02-10-1644.txt", 'r') as text1:
	data1 = text1.read()
with open("Shujian-A1-V4-2014-02-11-1502.txt", 'r') as text2:
	data2 = text2.read()
'''

f_read_1 = open("Shujian-A1-V1-2014-02-10-1644.txt", 'r')
f_read_2 = open("Shujian-A1-V4-2014-02-11-1502.txt", 'r')
f_write = open("output.html", 'w')

data1 = f_read_1.read()
data2 = f_read_2.read()

dmp = diff_match_patch.diff_match_patch()

def comp(t1, t2):
	diffs = dmp.diff_main(t1, t2)
	dmp.diff_cleanupSemantic(diffs)
	output_html = dmp.diff_prettyHtml(diffs)
	output_html.encode('utf-8')

	f_write.write("<meta http-equiv=\"Content-Type\" CONTENT=\"text/html; charset=UTF-8\"/>")
	f_write.write(output_html)
#	f_write.write(dmp.diff_prettyHtml(diffs).encode('utf-8'))
	return
'''
	for str in diffs:
		# this is to take into consideration of the '\n' situation
		if len(str[1]) > 1:
			print "*************************"
			print str[0]
			print str[1].encode('utf-8')
'''

comp(data1, data2)

f_read_1.close()
f_read_2.close()
f_write.close()
