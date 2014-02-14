import diff_match_patch
import sys
reload(sys)
sys.setdefaultencoding('UTF8')

with open("Shujian-A1-V1-2014-02-10-1644.txt", 'r') as text1:
	data1 = text1.read()
with open("Shujian-A1-V4-2014-02-11-1502.txt", 'r') as text2:
	data2 = text2.read()


dmp = diff_match_patch.diff_match_patch()

def comp(t1, t2):
	diffs = dmp.diff_main(t1, t2)
	dmp.diff_cleanupSemantic(diffs)
	for str in diffs:
		# this is to take into consideration of the '\n' situation
		if len(str[1]) > 1:
			print "*************************"
			print str[0]
			print str[1].encode('utf-8')
	return

comp(data1, data2)
