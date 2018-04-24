import redis
import aiohttp
import asyncio
# r = redis.Redis(host="localhost",port=6379)
# for i in range(10):
#     r.sadd("youxin",i)
#
# print(r.sismember("youxin",5))
# while True:
# a = [r.spop("youxin") for _ in range(15)]
# print(a)
# b = [i.decode("utf-8") for i in a if i !=None]
# print(b)
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.1.17291"}

class TEST:
    def __init__(self):
        self.r = redis.Redis(host="localhost",port=6379)
    def task_sys(self):
        url = "https://www.xin.com/beijing/baoma/i{}/"
        for i in range(21,31):
            self.r.sadd("new_task",url.format(i))
    def old_task(self):
        url = "https://www.xin.com/beijing/baoma/i{}/"
        for i in range(1,21):
            self.r.sadd("old_task",url.format(i))
    def test(self):
        url = "https://www.xin.com/beijing/baoma/i{}/"
        for i in range(10,30):
            if self.r.sismember("old_task",url.format(i)):
                print("重复了")
            else:
                print("没有重复")
class REQ:
    async def getPage(self,url):
            async with aiohttp.ClientSession() as resp:
                try:
                    async with resp.get(url,headers= HEADERS) as resp:
                        page_source = await resp.text()
                        print(resp.status)
                except:
                    print("出错了",url)
    def run_async(self,urls):
        loop = asyncio.get_event_loop()
        tasks = [self.getPage(i) for i in urls]
        loop.run_until_complete(asyncio.wait(tasks))
        loop.close()


if __name__ == '__main__':
    re = REQ()
    re.run_async(["https://www.xin.csdfergering/baoma/i{}/".format(i) for i in range(2,4)])




