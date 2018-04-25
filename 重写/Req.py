import asyncio
import aiohttp
import multiprocessing as mp
import Url_Manager
import logging
logging.basicConfig(level=logging.INFO)
class Req(object):
    def __init__(self):
        self.redi = Url_Manager.UrlMana()
        self.headers = headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}
    async def get(self,url,q):
        async with aiohttp.ClientSession() as resp:
            try:
                async with resp.get(url) as resp:
                    page = await resp.text()
                    q.put([url,page])
            except:
                logging.info(url+"请求出错")
                self.redi.new_task(url)
    def cun(self,urls,q):
        loop = asyncio.get_event_loop()
        tasks = [self.get(i,q) for i in urls]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()
if __name__ == '__main__':
    urls = ["https://www.xin.com/shenzhen/baoma/i{}/".format(i) for i in range(1,3)]
    r = Req()
    q = mp.Queue()
    r.cun(urls,q)
    while not q.empty():
        a = q.get()
        print(a)




