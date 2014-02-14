import requests
from bs4 import BeautifulSoup as BS
import re
import scraper

"""
http://news.cyol.com/content/2014-02/10/content_9649228.htm
http://qnck.cyol.com/html/2014-01/29/nw.D110000qnck_20140129_2-25.htm
http://digi.cyol.com/content/2014-02/08/content_9643468.htm
http://zqb.cyol.com/html/2014-01/23/nw.D110000zgqnb_20140123_1-10.htm
http://qnsl.cyol.com/html/2014-02/07/nw.D110000qnslb_20140207_1-06.htm
http://chuangye.cyol.com/content/2014-01/28/content_9623168.htm
http://life.cyol.com/content/2014-02/11/content_9649728.htm
"""
def get_links(soup):
    """Returns a list of tuples (url, category, date)"""
    links = re.findall("href=\"(http://(\w+)\.cyol\.com/\w+/(\d{4}-\d{2}/\d{2})/.+?\.htm)", str(soup))
    return links

def get_author(soup):
    author = re.findall('<author>(.*)</author>', str(soup), re.DOTALL)
    if author:
        author = author[0]
    return author

def get_content(soup):
    enpcontent = re.findall('<!--enpcontent-->(.*)<!--enpcontent-->',str(soup), re.DOTALL)
    if enpcontent:
        enpcontent = enpcontent[0]
        contentsoup = BS(enpcontent)
        text = contentsoup.getText().encode('utf-8')
        return text

def test_all():
    main = scraper.get_soup("http://cyol.com")
    links = get_links(main)
    num_links = len(links)
    #import pdb; pdb.set_trace()
    i = 0
    for link in links:
        print i
        url, category, date = link
        print url
        print category
        print date
        article = scraper.get_soup(url)
        meta = scraper.get_meta(article)
        print meta
        author = get_author(article)
        print author
        content = get_content(article)
        print content
        i += 1

    print("SUCCESFULLY RETRIEVED " + str(i) + "/" + str(num_links))

test_all()
