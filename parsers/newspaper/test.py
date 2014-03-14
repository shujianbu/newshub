import newspaper
import re
import os

#os.mkdir("output4")

paper = newspaper.build("http://www.scmp.com", memoize_articles=True)
#paper = newspaper.build("http://www.huanqiu.com", memoize_articles=False, language = 'zh')

#article = paper.articles[5]

i = 0
for article in paper.articles:
	print article.url
	#print paper.category_urls()

	article.download()

	article.parse()
	print article.text
	print "************************"
	print "author: " + str(article.authors)
	print "************************"
	print article.title
	print "########################"

	i = i + 1
	if i > 5:
		break

j=0
for category in paper.category_urls():
	print category
	j + 1
	if j > 5:
		break
'''
i =0
for domain in open('list','r'):
	# in reality, we need to set this to TRUE
	paper = newspaper.build(domain, memoize_articles=False)
	domain = re.search('http\:\/\/([^\/]+)\/', domain)
	domain = domain.group(1)
	print domain

	result = open('./output4/' + domain.strip()+'.output', 'w+')
	result.write("this is the first line" + '\n')
	for article in paper.articles:
#		print f.url
		result.write(article.url + '\n')
	result.close()
'''
