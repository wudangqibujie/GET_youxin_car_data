import multiprocessing as mp
import aiohttp
import asyncio
class A():
    async def HAHA(self,q,url):
        async with aiohttp.ClientSession() as resp:
            async with resp.get(url) as resp:
                page  = await resp.text()
                # print(resp.status)
                q.put(page)
    def RUN(self,urls,q):
        loop = asyncio.get_event_loop()
        task = [self.HAHA(q,i) for i in urls]
        loop.run_until_complete(asyncio.wait(task))
        loop.close()
if __name__ == '__main__':
    a = A()
    q = mp.Queue()
    urls = ["https://www.xin.com/shanghai/baoma/?channel=a49b117c44837d110753e751863f53","https://www.xin.com/shanghai/biaozhi/?channel=a49b117c44837d110753e751863f53"]
    p1 = mp.Process(target=a.RUN,args=(urls,q))
    p1.start()
    p1.join()
    print(q.get())
    print(q.get())
    print(q.get())
#

