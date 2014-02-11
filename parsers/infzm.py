import requests
from bs4 import BeautifulSoup as BS
import re
import scraper

"""
Parse infzm.com
"""

def get_links(soup):
    """Articles have url format like
    <http://www.infzm.com/content/98014>
    """
    links = re.findall("href=\"(http://www\.infzm\.com/content/\d+)\"", str(soup))
    return links

def get_tags(soup):
    tag_links = soup.findAll('li', {'class' : 'tagContent'})
    if tag_links:
        tags = [tag.getText().encode('utf-8') for tag in tag_links]
        return tags

def get_author(soup):
    author = soup.find("span", {"class":"author"})
    if author:
        text = author.getText().encode("utf-8")
        return text[18:]

def get_date(soup):
    date = soup.find("em", {"class":"pubTime"})
    if date:
        text = date.getText().encode("utf-8")
        return text[22:]

def get_content(soup):
    content = soup.find("section", {"id":"articleContent"})
    if content:
        content = content.getText().encode("utf-8")
    
    return content

def test_all():
    main = scraper.get_soup("http://www.infzm.com")
    links = get_links(main)
    num_links = len(links)

    i = 0
    for link in links:
        print i
        print link
        article = scraper.get_soup(link)
        meta = scraper.get_meta(article)
        print meta
        content = get_content(article)
        print content
        i += 1

    print("SUCCESFULLY RETRIEVED " + str(i) + "/" + str(num_links))
