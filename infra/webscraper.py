import requests
from bs4 import BeautifulSoup

HEADERS = {
    'User-Agent': ('Mozilla/5.0 (X11; Linux x86_64)'
                    'AppleWebKit/537.36 (KHTML, like Gecko)'
                    'Chrome/44.0.2403.157 Safari/537.36'),
    'Accept-Language': 'en-US, en;q=0.5'
}

class Webscraper():
    
    def beautifuler(self, url, headers=HEADERS):
        res = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(res.content, "lxml")
        return soup


    def soupParser(self, soup, tag=None, attib=None, strip=None, all='n'):
        if all.upper() != 'N':
            element = soup.find_all(tag, class_= attib)
        else:
            element = soup.find(tag, class_= attib)

        if strip=='text':
            element_val = element.text.strip()
        elif strip=='src':
            element_val = element[strip]
        else:
            element_val = element

        return element_val