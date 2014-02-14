import requests
from bs4 import BeautifulSoup as BS
import re
import scraper

"""
scmpchinese.com redirects to http://www.nanzao.com/sc
baseurl: http://www.nanzao.com/sc
http://www.nanzao.com/sc/china/20229/jing-tong-guo-fang-zhi-kong-wu-tiao-li-huan-bao-yu-guan-yuan-kao-he-gua-gou

A lot of poorly formatted html-- use regex instead of BS. Unable to find divs with BS.
"""

def get_links(soup):
    """Returns links, a list of tuples (url, category) """
    #root = "http://www.nanzao.com"
    links = re.findall("<a href=\"(/sc/(\w+)/\d+/.+?)\"", str(soup))
    
    return links

def get_publishdate(soup):
    publishdate = re.findall("<div class=\"field field-name-post-date field-type-ds field-label-hidden\"><div class=\"field-items\"><div class=\"field-item even\">(.+?)</div>", str(soup))
    if publishdate:
        publishdate = publishdate[0]
    return publishdate

def get_content(soup):
    content = re.findall("<p>[<.+?>]*(.*?)[<.+?>]*</p>", str(soup))
    if content:
        return content[0]
    return content

def test_all():
    root = "http://www.nanzao.com"
    main = scraper.get_soup(root)
    if main:
        print "Fetched index page"
        all_links = get_links(main)
        num_links = len(all_links)
        print "num_links", num_links

        i = 0
       
        for url, cat in all_links:
            print "URL AND CAT"
            print url, cat
            soup = scraper.get_soup(root + url)
            if soup:
                publishdate = get_publishdate(soup)
                print "PUBLISHDATE"
                print publishdate
                content = get_content(soup)
                print "CONTENT"
                print content
                meta = scraper.get_meta(soup)
                print "META"
                print meta
                print "ARTICLE NUM", i
                i += 1
    print "NUMBER OF SUCCESSFULLY FETCHED ARTICLES: ", i
    print "TOTAL NUMBER OF ARTICLES", num_links

test_all()  
