import requests
from lxml import etree
import DataBase.redis_or
import time
import re
import city_name

START_URL = "https://www.xin.com/"
CITY = "shenzhen"
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

class Master_Spider():
    def __init__(self,city):
        self.start_url = "https://www.xin.com/"
        self.city = city

    def get_html(self,url):
        try:
            r = requests.get(url,headers = HEADERS)
            if r.status_code == 200:
                return etree.HTML(r.text)
            else:
                print("相应状态码有异常！")
        except:
            print("请求存在异常!")
#获取设定城市下的url
    def get_city_urls(self):
        return self.start_url+self.city
#获得具体城市具体车型页面的最大页面数
    def get_max_page(self,html):
        max= html.xpath('//div[@class="con-page search_page_link"]')
        print(max)
        # if  max:
        #     max_page = max[-2]
        #     max_page_num = max_page.xpath('text()')[0]
        #     print(max_page_num)
        #     if max_page_num:
        #         return max_page_num
        #     else:
        #         print("解析最大页数有问题！!!")
        # else:
        #     print("解析最大页数有问题！")
#带上页数的URL
    def get_page_urls(self,page,car_name):
        url_page = self.get_city_urls()+car_name+"i%s/"%str(page)
    def get_car_model(self,html):
        data = dict()
        alpha_items = html.xpath('//ul[@class="brand-cars clearfix"]/li')[1:]
        if alpha_items:
            for alpha_item in alpha_items:
                a=alpha_item.xpath('dl/dd')
                for i in a:
                    car_url = i.xpath('a/@href')
                    car_name = i.xpath('a/@title')
                    # car_name =/
                    if car_name and car_url:
                        data[car_name[0]] = "http://" + car_url[0][2:]
                    else:
                        print("解析型号和连接失败！")
        else:
            print("字母车型列表解析错误！")
        return data
#获取详情页面的链接
    def get_detail_url(self,html):
        detail_urls = []
        try:
            car_items = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
            for car_item in car_items:
                car_url = car_item.xpath('div[@class="across"]/a/@href')
                # print(car_url)
                if car_url:
                    if str(car_url[0]).startswith(r'//'):
                        detail_urls.append(car_url[0][2:])

                    else:
                        print("有误")
                        continue
                        print("有误")
                else:
                    print("youwu")
                    continue
                    print("youwu")
        except:
            print("获取详情面链接有误")
        return detail_urls
    def urls_into_redis(self,url_list,city):
        B = redis_or.Redis_Data()
        if url_list:
            for i in url_list:
                # pattern = re.compile(r'%s/(.*?)/$'%self.city)
                # key_name = re.findall(pattern,i)
                # print(key_name)
                try:
                    B.set_into_data("%s_youxin"%city,i)
                except:
                    print("进Redis数据库异常",i)
                    continue
        else:
            print("空列表")


    def loop_page(self,brand_url):
        detail_urls = []
        for i in range(200):
            url = brand_url+r'i{page}/'.format(page=i)
            print("易出问题的连接",url)
            try:
                html = self.get_html(url)
                time.sleep(2)
                urls = self.get_detail_url(html)
                if urls:
                    detail_urls.extend(urls)
                else:
                    break
            except ArithmeticError as e:
                print(e,url)
                continue
        return detail_urls

    def get_brand_urls(self):
        u = self.get_city_urls()
        html = self.get_html(u+"/baoma/")
        # html = self.get_html(A_url + "/baoma/")
        brand_url_dic = self.get_car_model(html)
        brand_urls = []
        for key, value in brand_url_dic.items():
            brand_urls.append(value)
        return brand_urls

def main(city):
    A = Master_Spider(city)
    brand_urls = A.get_brand_urls()
    print(brand_urls)
    for i in brand_urls:
        details = A.loop_page(i)
        print(details)
        print(len(details))
        A.urls_into_redis(details,city)

#爬去到汕头
if __name__ == '__main__':
    b = city_name.json2citydict()
    # b = json2citydict()
    for city in b.values():
        if city not in ["beijing", "guangzhou", "shanghai","changsha","hangzhou","shenzhen","haerbin","hefei","anqing","bengbu","huainan","fuyang"]:
            print(city)
            main(city)
        else:
            continue





