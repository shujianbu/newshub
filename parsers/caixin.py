import requests
from bs4 import BeautifulSoup as BS
import re
import scraper
"""
<a href="http://economy.caixin.com/2014-02-08/100636431.html">

link format: <category>.caixin.com/<YYYY-MM-DD>/<\d+>.html
"""

def get_links(soup):
    """Get article links with categories and date
        Returns links, a list of tuples (url, category, date)
    """
    links = re.findall("<a href=\"(http://(\w+)\.caixin\.com/(\d{4}-\d{2}-\d{2})/\d+\.html)\">", str(soup))
    return links

def get_content(soup):
    if soup.find("div", {"id":"Main_Content_Val", "class":"text"}):
        content_div = soup.find("div", { "id":"Main_Content_Val", "class":"text"})
    elif soup.find("span", {"id":"Main_Content_Val"}): 
        content_div = soup.find("span", {"id":"Main_Content_Val"})
    elif soup.find("div", {"class":"textCon", "id":"text_con"}):
        content_div = soup.find("div", {"class":"textCon", "id":"text_con"})
    else:
        return None

    paragraphs = content_div.findAll("p")
    return [p.getText().encode("utf-8") for p in paragraphs]
    
def get_reporter(soup):
    """If there is a listed reporter for the article, then it will be in
    round brackets in the first line of the story before the text"""
    if soup.find("div", {"id":"Main_Content_Val", "class":"text"}):
        content_div = soup.find("div", { "id":"Main_Content_Val", "class":"text"})
    elif soup.find("span", {"id":"Main_Content_Val"}): 
        content_div = soup.find("span", {"id":"Main_Content_Val"})
    elif soup.find("div", {"class":"textCon", "id":"text_con"}):
        content_div = soup.find("div", {"class":"textCon", "id":"text_con"})
    else:
        return None

            content = [line for line in get_content(article)]
            content = [line for line in get_content(article)]
            content = [line for line in get_content(article)]
            content = [line for line in get_content(article)]
            content = [line for line in get_content(article)]
    first_para = content_div.find("p").encode('utf-8')
    LEFT_BRAC = '\xef\xbc\x88'
    RIGHT_BRAC = '\xef\xbc\x89'
    reporter = re.findall(LEFT_BRAC + "(.+)" + RIGHT_BRAC, first_para)
    
    return reporter

def test_all():
    main = scraper.get_soup("http://caixin.com/")
    links = get_links(main)
    num_links = len(links)

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
        content = get_content(article)
        if content:
            for line in get_content(article):
                print line
        else:
            print "PHOTOS ONLY"
        i += 1

    print("SUCCESFULLY RETRIEVED " + str(i) + "/" + str(num_links))



