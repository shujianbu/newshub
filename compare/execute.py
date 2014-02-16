import os

aFolder = os.listdir("./articles")
folderNum = len(aFolder)

print folderNum

aPath = []
for i in range(folderNum):
	_aPath = "./articles/sample_" + str(i)
	aPath.append(_aPath)

aSet = []
for i in range(folderNum):
	_aSet = os.listdir(aPath[i])
	_aSet.sort()
	aSet.append(_aSet)

if os.system("cd output") == 0:
	os.system("rm -r output")
os.mkdir("output")

for i in range(folderNum):
	dirPath = "output/" + str(i)
	os.mkdir(dirPath)

	for j in range(len(aSet[i])-1):
		articlePath_A = aPath[i] + '/' + aSet[i][j]
		articlePath_B = aPath[i] + '/' + aSet[i][j+1]

		print "##############" + str(i) + "____" + str(j)
	
		outputFile = dirPath + "/output_" + str(j) + '_' + str(j+1) + ".html"
		command = "python compare.py %s %s %s" %(articlePath_A, articlePath_B, outputFile)
		print command
		os.system(command)

os.system("rm *.pyc")
