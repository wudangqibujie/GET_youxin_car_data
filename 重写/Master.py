import create_init_task
import multiprocessing as mp
want_cars= {"奥迪":"aodi","阿尔法罗密欧":"aerfaluomiou","阿斯顿马丁":"asidunmading","本田":"bentian","别克":"bieke","奔驰":"benchi","宝马":"baoma","标致":"biaozhi","比亚迪":"biyadi","保时捷":"baoshijie","宾利":"binli","宝沃":"baowo","长城":"changcheng","大众":"dazhong","东南":"dongnan","道奇":"daoqi","东风":"dongfeng","DS":"ds","东风小康":"dongfengxiaokang","丰田":"fengtian","福特":"fute","菲亚特":"feiyate","福田":"futian","法拉利":"falali","广汽传祺":"guangqichuanqi","观致":"guanzhi","哈弗":"hafu","吉利":"jiliqiche","JEEP":"jeep","江淮":"jianghuai","捷豹":"jiebao","金杯":"jinbei","凯迪拉克":"kaidilake","克莱斯勒":"kelaisile","路虎":"luhu","铃木":"lingmu","雷克萨斯":"leikesasi","陆风":"lufeng","雷诺":"leinuo","林肯":"linken","兰博基尼":"lanbojini","劳斯莱斯":"laosilaisi","路特斯":"lutesi","领克":"lingke","马自达":"mazida","MINI":"mini","玛莎拉蒂":"mashaladi","迈凯伦":"maikailun","迈巴赫":"maibahe","讴歌":"ouge","欧宝":"oubao","起亚":"qiya","奇瑞":"qirui","日产":"richan","荣威":"rongwei","斯柯达":"sikeda","三菱":"sanling","smart":"smart","斯巴鲁":"sibalu","特斯拉":"tesila","五菱":"wuling","沃尔沃":"woerwo","五十铃":"wushiling","现代":"xiandai","雪佛兰":"xuefulan","雪铁龙":"xuetielong","野马汽车":"yemaqiche","英菲尼迪":"yingfeinidi","众泰":"zhongtai"}
import Url_Manager
import Req
import logging
import Parse
logging.basicConfig(level=logging.INFO)

def create_start_urls():
    c = create_init_task.INIT_task()
    city = c.get_city()
    city_name = list(city.values())
    cars_name = list(want_cars.values())
    start_urls = [r"https://www.xin.com{city}{car}/".format(city=city,car=cars) for city in city_name for cars in cars_name]
    logging.info("初始任务生成完毕准备进入任务队列")
    return start_urls
def data_filter():
    pass
def A(q):
    while True:
        try:
            it = q.get(timeout = 10)
            print(it)
        except:
            print("获取完毕")
            break
def B(q1,q2):
    while True:
        try:
            print("BBBB")
            ht = q1.get(timeout=10)
            print(ht[0])
            p_mas.master_parse(ht[1],q2)
        except:
            print("over")
if __name__ == '__main__':
    spider_name = "youxin"
    rq = Req.Req(spider_name)
    r1 = Url_Manager.UrlMana(spider_name)
    p_mas = Parse.Parse()
    html_queue = mp.Queue()
    item_queue = mp.Queue()
    r1.init_task(create_start_urls())
    tasks = r1.task_create_filter(10)
    print(tasks)
    p1 = mp.Process(target=rq.cun,args=(tasks,html_queue))
    p1.start()
    p2 = mp.Process(target=A,args=(item_queue,))
    p2.start()
    p3 = mp.Process(target=B,args=(html_queue,item_queue))
    p3.start()



















    #
    # r = Req.Req()
    # p = Parse.Parse()
    # urls = ["https://www.xin.com/shenzhen/baoma/i{}/".format(i) for i in range(1,3)]
    # q1 = mp.Queue()
    # q2 = mp.Queue()
    # r.cun(urls,q1)
    # while not q1.empty():
    #     a = q1.get()
    #     p.master_parse(a[1],q2)
    # while not q2.empty():
    #     c = q2.get()
    #     print(c)
    #



