
import urllib2
from bs4 import BeautifulSoup
import re

"""
Script to fetch the contents of all the articles from huanqiu news site and save them by name.
"""

main_page = urllib2.urlopen("http://www.huanqiu.com/")

main_soup = BeautifulSoup(main_page)

#find all articles (denoted by date format)
all_links = main_soup.findAll('a', href=re.compile('http://\w+\.huanqiu\.com/\S*\d\d\d\d-\d\d/\d+\.html'))

for link in all_links:
    #get each article
    article = urllib2.urlopen(link.get('href').encode('utf-8'))
    soup = BeautifulSoup(article)

    title = soup.title.string.encode('utf-8')
    print title

    outfile = file(title, "w")

    text_divs = soup.findAll("div", { "class" : "text" })
    for div in text_divs:
        paragraphs = div.findAll("p")
        for p in paragraphs:
            if p.string:
                outfile.write(p.string.encode('utf-8'))

    outfile.close()
