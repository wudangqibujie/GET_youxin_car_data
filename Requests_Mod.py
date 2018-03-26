from selenium import webdriver
import time
import asyncio
import aiohttp
from lxml import etree
import requests
import threading
import logging
from multiprocessing import Process
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Req():
    def Browser_get(self,url):
        br = webdriver.Chrome()
        br.get(url)
        time.sleep(10)
        print(br.page_source)
    def common_get(self,url):
        logging.info("正在进行常规requests请求")
        try:
            r = requests.get(url)
            return r.text
        except requests.exceptions.ConnectionError as e:

    def multi_threa_get(self,url):
        pass
    def test_parse(self,res):
        html = etree.HTML(res)
        car_urls = []
        items = html.xpath('//div[@class="carlist-show"]/div[1]/ul/li')
        for i in items:
            url = i.xpath('div[@class="across"]/a/@href')
            car_urls += url
        return car_urls

    async def getPage(self,url,car_lists):
        async with aiohttp.ClientSession() as resp:
            async with resp.get(url) as resp:
                data = await resp.text()
                car_list = self.test_parse(data)
                car_lists += car_list
    def common_run(self):
        url = "https://www.xin.com/shenzhen/baoma/i{page}/"
        car_lists=[]
        for i in range(1,21):
            resp = self.common_get(url.format(page = i))
            car_list = self.test_parse(resp)
            car_lists += car_list
        print(car_lists)
        print(len(car_lists))

    def asyn_run(self):
        url = "https://www.xin.com/shenzhen/baoma/i{page}/"
        car_lists = []
        page_urls = [url.format(page = i) for i in range(1,21)]
        loop = asyncio.get_event_loop()
        tasks = [self.getPage(host,car_lists) for host in page_urls]
        loop.run_until_complete(asyncio.wait(tasks))
        print(len(car_lists))
if __name__ == '__main__':
    we = Req()
    we.



    # a2 = time.time()
    # we.common_run()
    # print("requests方法耗时",time.time()-a2)
    #
    #
    # a1 = time.time()
    # we.asyn_run()
    # print("异步的耗时",time.time()-a1)
    #




