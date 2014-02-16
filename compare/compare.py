import diff_match_patch
import sys
from sys import argv

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
