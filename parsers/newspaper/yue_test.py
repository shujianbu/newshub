import newspaper
import re
i =0
for domain in open('list_ch.txt','r'):
	paper = newspaper.build(domain)
	domain = re.search('http\:\/\/([^\/]+)\/', domain)
	domain = domain.group(1)
	print domain

	result = open(domain.strip()+'.output', 'w+')
	for article in paper.articles:
		# print f.url
		result.write(article.url + '\n')
	result.close()
	
