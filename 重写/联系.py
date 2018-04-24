import aiohttp
import asyncio
import redis
r = redis.Redis(host="localhost",port=6379)
def urls_filter():
    raw = [r.spop("new_task") for _ in range(10)]
    print("未处理",raw)
    flesh = [i.decode("utf-8") for i in raw if not r.sismember("old_task",i) and i != None]
    print("已经处理",flesh)
    return flesh

async def get(url):
    async with aiohttp.ClientSession() as resp:
        try:
            async with resp.get(url) as resp:
                page = await resp.text()
                print(resp.status)
        except:
            print(url,"出错了")
            r.sadd("new_task",url)

def cun(urls):
    loop = asyncio.get_event_loop()
    tasks = [get(i) for i in urls]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()


tasks = urls_filter()
if tasks:
    cun(tasks)
else:
    print("没有更多任务了")
