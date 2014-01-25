
import requests
from bs4 import BeautifulSoup as BS
import re
from time import strftime

"""
customized functions for general parsing of news sites
"""

def get_pages_with_retry(url):
    """Try to get page with 5 retries"""
    for i in range(5):
        print "attempt", i+1
        while True:
            try:
                r = requests.get(url, timeout=5)
                return r
            except requests.exceptions.Timeout:
                print "Your request timed out."
                continue
            except requests.exceptions.TooManyRedirects:
                print "Too Many Redirects. Check your URL. Stopping."
                continue
            except requests.exceptions.RequestException as e:
                print e
                continue
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


def current_time():
    return strftime("%Y-%m-%d %H:%M:%S")





















