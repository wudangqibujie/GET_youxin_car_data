from selenium import webdriver
import time
import asyncio
import aiohttp
from lxml import etree
import requests
import threading
import logging
import multiprocessing as mp
from queue import Queue
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Req():
    def Browser_get(self,url):
        br = webdriver.Chrome()
        br.get(url)
        time.sleep(10)
        print(br.page_source)
    def common_get(self,url,q=None):
        logging.info("正在进行常规requests请求")
        try:
            r = requests.get(url)
            logger.info("请求成功！")
            return r.text
        except requests.exceptions.ConnectionError as e:
            logger.info("发生连接错误")
        except requests.exceptions.Timeout as e:
            logger.info("发生连接超时")
        except requests.exceptions.ProxyError as e:
            logger.info("代理IP有问题")
        except:
            logger.info("其他异常!")
        finally:
            if q == None:
                pass
            else:
                q.put(r.text)
#用多进程的map方法取结果，返回的是一个列表
    def multi_pro_get1(self,func,urls):
        pool = mp.Pool()
        res = pool.map(func,urls)
        return res
#运用apply_async方法获取结果,输进去单个参数，返回也是返回单个好像好控制一点
    def multi_pro_get2(self,func,url):
        pool = mp.Pool()
        res = pool.apply_async(func,(url,))
        return res.get()
#运用apply_async方法，但是输出多个参数
    def multi_pro_get3(self,func,urls):
        pool = mp.Pool()
        multi_list = [pool.apply_async(func,(url,)) for url in urls]
        return (res.get() for res in multi_list)#这里返回的是一个迭代器

    def multi_pro_run_test(self):
        f = open("guangzhou.txt","a")
        urls = ["https://www.xin.com/shenzhen/baoma/i%s"%str(i) for i in range(16,21)]
        res1 = self.multi_pro_get1(self.common_get,urls)
        for i in res1:
            urls = self.test_parse(i)
            for i in urls:
                f.write(i+"\n")
        f.close()
        # for i in urls:
        #     res2 = self.multi_pro_get2(self.common_get,i)
            # print(res2)
        # res3 = self.multi_pro_get3(self.common_get,urls)
        # for i in res3:
        #     print(i)
    def multi_threa_get(self,func,urls,q):
        # q = Queue()
        result = []
        thre_list = [threading.Thread(target=func,args=(url,q)) for url in urls]
        for i in thre_list:
            i.start()
        for i in thre_list:
            i.join()
        for i in thre_list:
            result.append(q.get())
        return result

    def mul_thre_run_test(self):
        q = Queue()
        f = open("guangzhou.txt","a")
        urls = ["https://www.xin.com/shenzhen/baoma/i%s"%str(i) for i in range(11,16)]
        resp = self.multi_threa_get(self.common_get,urls,q)
        for i in resp:
            urls = self.test_parse(i)
            for j in urls:
                f.write(j+"\n")
        f.close()


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

    def common_run_test(self):
        f = open("guangzhou.txt","a")
        url = "https://www.xin.com/shenzhen/baoma/i{page}/"
        for i in range(6,11):
            resp = self.common_get(url.format(page = i))
            car_list = self.test_parse(resp)
            for i in car_list:
                f.write(i+"\n")
        f.close()

    def asyn_run_test(self):
        f = open("guangzhou.txt","a")
        url = "https://www.xin.com/shenzhen/baoma/i{page}/"
        car_lists = []
        page_urls = [url.format(page = i) for i in range(1,6)]
        loop = asyncio.get_event_loop()
        tasks = [self.getPage(host,car_lists) for host in page_urls]
        loop.run_until_complete(asyncio.wait(tasks))
        for i in car_lists:
            f.write(i+"\n")
        f.close()
if __name__ == '__main__':
    we = Req()
    t1 = time.time()
    we.asyn_run_test()
    print("异步的耗时",time.time()-t1)
    t2 = time.time()
    we.common_run_test()
    print("普通request耗时",time.time()-t2)
    t3 = time.time()
    we.multi_pro_run_test()
    print("多进程耗时",time.time()-t3)
    t4 =time.time()
    we.mul_thre_run_test()
    print("多线程耗时",time.time()-t4)



    # urls = ["https://www.xin.com/shenzhen/baoma/i%s"%str(i) for i in range(1,21)]
    # print(urls)
    # we.multi_threa_get(we.common_get,urls)


    # we.common_get("https://www.xin.com/shenzhen/baoma/i3/")



    # a2 = time.time()
    # we.common_run()
    # print("requests方法耗时",time.time()-a2)
    #
    #
    # a1 = time.time()
    # we.asyn_run()
    # print("异步的耗时",time.time()-a1)
    #




