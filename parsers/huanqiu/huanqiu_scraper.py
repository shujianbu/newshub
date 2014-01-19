
import requests
from bs4 import BeautifulSoup as BS
import re
from time import strftime

"""
huanqiu_scraper.py

scrapes http://www.huanqiu.com/ for article content and information.

Extend functions for multiple sites.
"""

def get_pages_with_retry(url):
    """Try to get page with 5 retries"""
    for i in range(5):
        print "attempt", i+1
        while True:
            try:
                r = requests.get(url)
                return r
            except requests.exceptions.Timeout:
                print "Your request timed out."
                continue
            except requests.exceptions.TooManyRedirects:
                print "Too Many Redirects. Check your URL. Stopping."
            except requests.exceptions.RequestException as e:
                print e
            break


def get_soup(url):
    """load html page given url"""
    page = get_pages_with_retry(url)
    if page:
        soup = BS(page.content) 
        return soup
    else:
        print "Failed to get page."

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
    author_text = soup.find("meta", {"name": "author"})
    publishdate_text = soup.find("meta", {"name": "publishdate"})

    if author_text:
        author = author_text.get("content").encode("utf-8")
    else:
        author = None
    if publishdate_text:
        publishdate = publishdate_text.get("content")
    else:
        publishdate = None

    return all_meta, author, publishdate

def current_time():
    return strftime("%Y-%m-%d %H:%M:%S")


def test_all():
    """Test scraper on all articles"""
    main = get_soup("http://www.huanqiu.com/")
    if main:    
        all_links = get_links(main)
        num_links = len(all_links)

        i = 0
        for link in all_links:
            soup = get_soup(link.get('href').encode('utf-8'))
            if soup:
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

    print "NUMBER OF SUCCESSFULLY FETCHED ARTICLES: ", i
    print "TOTAL NUMBER OF ARTICLES", num_links
    #TODO: Create class for above, format SQL



