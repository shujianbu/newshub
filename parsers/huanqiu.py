import requests
from bs4 import BeautifulSoup as BS
import re
import time
import scraper
# from scraper import *

"""
huanqiu_scraper.py

scrapes http://www.huanqiu.com/ for article content and information.
"""

def get_links(soup):
    """Get all the links to articles (with date in them)"""
    links = soup.findAll('a', href=re.compile('http://\w+\.huanqiu\.com/\S*\d\d\d\d-\d\d/\d+\.html'))
    links = [l.get('href').encode('utf-8') for l in links]
    return links

def get_category(link):
    category = re.findall('http://\w+\.huanqiu\.com/(\w+)/\d\d\d\d-\d\d/\d+\.html', link)
    if category:
        return category[0]
    else:
        return None

def get_content(soup):
    """Return the encoded text in the article"""
    text_divs = soup.findAll("div", { "class" : "text" })
    if text_divs: #some articles only pics
        for div in text_divs:
            paragraphs = div.findAll("p")
            for p in paragraphs:
                if p.string and (len(p.string) > 0):
                    yield p.string.encode('utf-8') 

def get_author(soup):
    author_text = soup.find("meta", {"name": "author"})

    if author_text:
        author = author_text.get("content").encode("utf-8")
    else:
        author = None
    
    return author

def get_publishdate(soup):
   publishdate_text = soup.find("meta", {"name": "publishdate"})
   if publishdate_text:
        publishdate = publishdate_text.get("content")
   else:
        publishdate = None
   return publishdate


def test_all():
    """Test scraper on all articles"""
    main = scraper.get_soup("http://www.huanqiu.com/")
    if main:    
        print "got the main soup"
        all_links = get_links(main)
        num_links = len(all_links)

        i = 0
        for link in all_links:
            category = get_category(link)
            print category
            soup = scraper.get_soup(link)
            if soup:
                encoded_content = [line for line in get_content(soup)]
                all_meta = scraper.get_meta(soup)
                author = get_author(soup)
                publishdate = get_publishdate(soup)
                parsedate = time.strftime("%Y-%m-%d %H:%M:%S")

                #for testing
                if encoded_content:
                    for p in encoded_content:
                        print p
                print all_meta
                print author
                print publishdate
                print parsedate

                print "ARTICLE NUMBER", i
                i += 1

    print "NUMBER OF SUCCESSFULLY FETCHED ARTICLES: ", i
    print "TOTAL NUMBER OF ARTICLES", num_links
    #TODO: Create class for above, format SQL

test_all()
