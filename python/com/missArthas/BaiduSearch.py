#coding=utf-8
import urllib
import re
from bs4 import BeautifulSoup as BS

class BaiduSearch(object):
    target=0
    def search(self, word, page):
        """
        :type page: int
        :type word: str
        :rtype: List[str]
        """
        baseUrl='http://www.baidu.com/s'
        data = {'wd': word, 'pn': str(page - 1) + '0', 'tn': 'baidurt', 'ie': 'utf-8', 'bsst': '1'}
        data = urllib.parse.urlencode(data)
        url = baseUrl + '?' + data

        try:
            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
        except urllib.HttpError as e:
            print(e.code)
            exit(0)
        except urllib.URLError as e:
            print(e.reason)
            exit(0)

        html = response.read()
        print("html源码")
        print(html)
        soup = BS(html, "lxml")
        td = soup.find_all(class_='f')

        urls=[]
        titles=[]
        for t in td:
            urls.append(t.h3.a['href'])
            titles.append(t.h3.a.get_text().strip())
            print(t.h3.a.get_text().strip())
            print(t.h3.a['href'])
            #print ""
        return urls,titles



