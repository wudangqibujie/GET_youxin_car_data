import asyncio
import aiohttp
import Url_Manager
import logging
logging.basicConfig(level=logging.INFO)
class Req(object):
    def __init__(self):
        self.redi = Url_Manager.UrlMana()
    async def get(self,url,q):
        async with aiohttp.ClientSession() as resp:
            try:
                async with resp.get(url) as resp:
                    page = await resp
                    q.put([url,resp])
            except:
                logging.info(url+"请求出错")
                self.redi.new_task(url)
    def cun(self,urls):
        loop = asyncio.get_event_loop()
        tasks = [self.get(i) for i in urls]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()




