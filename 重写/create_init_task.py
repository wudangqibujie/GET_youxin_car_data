import requests
from lxml import etree
from selenium import webdriver

class INIT_task(object):
    def __init__(self):
        self.url = "https://www.xin.com/shenzhen/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    def get_city(self):
        city_url = dict()
        brower = webdriver.Chrome()
        brower.get(self.url)
        html = etree.HTML(brower.page_source)
        items = html.xpath('//table/tbody/tr')
        for i in items:
            a = i.xpath('td[2]/dl/dd')
            for j in a:
                u = j.xpath('a/@href')[0]
                n = j.xpath('a/text()')[0]
                city_url[n] = u
        brower.close()
        return city_url



if __name__ == '__main__':
    i = INIT_task()
    a = i.get_city()


