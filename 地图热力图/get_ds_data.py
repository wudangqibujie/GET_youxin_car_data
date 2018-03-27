#https://zhuanlan.zhihu.com/p/25845538
import json
import re
import time
import requests
from lxml import etree
def get_chinese_name(en_city):
    r = requests.get(url.format(city = en_city))
    html = etree.HTML(r.text)
    name = html.xpath('//div[@class="mianbaoxie-box"]/a[2]/text()')[0]
    return name.replace("二手车","")
def location(city_name):
    url = "http://api.map.baidu.com/geocoder/v2/?address={location}&output=json&ak=ESP9WBipoQkGmhR1RP5878A7sk71zX4M&callback=showLocation"
    r = requests.get(url.format(location=city_name))
    return r.text
def car_amount(city):
    url = "https://www.xin.com/{city}/leikesasi/"
    r = requests.get(url.format(city=city))
    html = etree.HTML(r.text)
    if_max = html.xpath('//div[@class="con-page search_page_link"]/a')
    if if_max:
        max_num = if_max[-2].xpath('text()')
        # print(url)
        # print(max_num)
        new_url = url.format(city=city)+"i"+max_num[0]+"/"
        # print(new_url)
        r1 = requests.get(new_url)
        html1 = etree.HTML(r1.text)
        max_page_amount = html1.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
        # print(len(max_page_amount))
        all_amount = 40*(int(max_num[0])-1)+len(max_page_amount)
        return all_amount
    else:
        if_have = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
        if if_have:
            amount = len(if_have)
            return amount
        else:
            return 0
def baidu_api():
    # api_js = '{"lat":' + str(lat) + ',"lng":' + str(lng) +',"count":' + str(c) +'},'
    f = open("leikesasi.txt",encoding="utf-8")
    h = open("leikesasi_fine_data.txt","w")
    city_amount_dict = eval(f.read())
    # print(city_amount_dict)
    g = open("loaction.txt",encoding="utf-8")
    # print(g.readline())
    pattern1 = re.compile(r'{"lng":(.*?),"lat"')
    pattern2 = re.compile(r'"lat":(.*?)},"precis')
    pattern3 = re.compile(r"{'(.*?)': 'sho")
    for ci in g:
        try:
            print(ci)
            lng_ = re.findall(pattern1,ci)[0]
            lat_ = re.findall(pattern2,ci)[0]
            city_name = re.findall(pattern3,ci)[0]
            lng = float(lng_)
            lat = float(lat_)
            c = city_amount_dict[city_name]
            api_js = '{"lng":' + str(lng) + ',"lat":' + str(lat) +',"count":' + str(c) +'},'+"\n"
            h.write(api_js)
            print(api_js)
        except:
            continue

    print(city_amount_dict)

def create_js():
    end_dict = {}
    g = open("leikesasi.txt", "w", encoding="utf-8")
    f = open("result.txt", encoding="utf-8")
    en_chi_dic = eval(f.read())
    i = 0
    for key, value in en_chi_dic.items():
        try:
            amount_num = car_amount(value)
            time.sleep(1)
            end_dict[key] = amount_num
            print(key)
            print(amount_num)
        except:
            i += 1
            print(key)
            continue
    g.write(str(end_dict))
    print(i)
    f.close()
    g.close()

if __name__ == '__main__':
    create_js()
    baidu_api()













