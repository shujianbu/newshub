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
    content = re.findall("<p>[<.+?>]*(.*?)[<.+?>]*</p>", str(s1))
    return content

def get_meta(soup):
    all_meta = soup.findAll('meta')
    return all_meta

def test_all():
    pass

"""
def test_all():
    "Test scraper on all articles"
    main = get_soup("http://www.huanqiu.com/")
    if main:    
        print "got the main soup"
        all_links = get_links(main)
        num_links = len(all_links)

        i = 0
        for link in all_links:
            category = get_category(link)
            print category
            soup = get_soup(link)
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
"""
