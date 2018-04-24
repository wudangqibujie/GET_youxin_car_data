import redis
import logging
logging.basicConfig(level=logging.INFO)

class UrlMana(object):
    def __init__(self):
        self.r = redis.Redis()
    def init_task(self,urls):
        for i in urls:
            self.r.sadd("new_master_task",i)
    def new_task(self,url):
        self.r.sadd("new_master_task",url)
    def old_task(self,url):
        self.r.sadd("old_master_task",url)
    def is_old(self,url):
        return self.r.sismember("old_task",url)
    def url_filter(self,task_num):
        raw = [self.r.spop("new_master_task") for _ in range(task_num)]
        logging.info("未处理"+raw)
        flesh_task = [i.decode("utf-8") for i in raw if not self.r.sismember("old_master_task",i) and i != None]
        print("已经处理",flesh_task)
        logging.info("已经处理"+flesh_task)


