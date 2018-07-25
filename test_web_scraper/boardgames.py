from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

def simple_get(url):
    """
    Attempts to get the content from url, returns raw html
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None
    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None
def is_good_response(resp):
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 and content_type is not None and content_type.find('html') > -1)
def log_error(e):
    print(e)

def js_get(url):
    """
    Attempts to get content from url, parsed through browser with javascript
    """
    options = Options()
    options.set_headless(headless=True)
    driver = webdriver.Firefox(firefox_options=options)
    driver.get(url)
    return driver.page_source

def parse_data(html):
    """
    parses data
    """
    soup = BeautifulSoup(html, "html.parser")
    final = []
    data = soup.find_all("div", {"class": "gameitem_baseline gamename"})
    for n in data:
        final.append(n.string.strip())
    return final


if __name__== '__main__':
    url = 'https://en.boardgamearena.com/#!gamelist?section=all'
    raw_html = js_get(url)
    final = parse_data(raw_html)
    print(final)
