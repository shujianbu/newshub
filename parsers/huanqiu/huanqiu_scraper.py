
import urllib2
from bs4 import BeautifulSoup as BS
import re
from time import strftime

"""
huanqiu_scraper.py

scrapes http://www.huanqiu.com/ for article content and information.

Extend functions for multiple sites.
"""
def get_page(url):
    try:
        page = urllib2.urlopen(url, timeout=5)
        
    except urllib2.URLError as e:
        print "REQUEST TIMED OUT"
        return None  

    return page


def get_soup(url):
    """load html page given url"""
    i = 0
    again = True
    
    while (i < 5) and again:
        page = get_page(url)
        if page:
            again = False
        else:
            i += 1
    
    if i == 5:
        print "NO CONNECTION"
        return 

    soup = BS(page)
    page.close() #memory leaks!
    return soup

def get_title(soup):
    """Return encoded title"""
    if soup.title.string:
        return soup.title.string.encode('utf-8')

def get_links(soup):
    """Get all the links to articles (with date in them)"""
    links = soup.findAll('a', href=re.compile('http://\w+\.huanqiu\.com/\S*\d\d\d\d-\d\d/\d+\.html'))
    return links

def get_content(soup):
    """ Am I yielding right """
    text_divs = soup.findAll("div", { "class" : "text" })
    if text_divs: #some articles only pics
        for div in text_divs:
            paragraphs = div.findAll("p")
            for p in paragraphs:
                if p.string and (len(p.string) > 0):
                    yield p.string.encode('utf-8') 

def get_meta(soup):
    all_meta = soup.findAll('meta')
    author = soup.find("meta", {"name": "author"}).get("content").encode("utf-8")
    publishdate = soup.find("meta", {"name": "publishdate"}).get("content")
    return all_meta, author, publishdate

def current_time():
    return strftime("%Y-%m-%d %H:%M:%S")


def main():
    main = get_soup("http://www.huanqiu.com/")
    if main:    
        all_links = get_links(main)

        i = 0
        for link in all_links:
            soup = get_soup(link.get('href').encode('utf-8'))
            encoded_content = [line for line in get_content(soup)]
            all_meta, author, publishdate = get_meta(soup)
            parsedate = strftime("%Y-%m-%d %H:%M:%S")

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

            #TODO: Create class for above, format SQL








"""
git add REMOVE DELETED !!!!!!!!!!!!!!!!!!!!


"""






