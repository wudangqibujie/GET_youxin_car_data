import requests
from lxml import etree
import mongo_or
import master
import redis_or
import json
import time
class Slave_Spisder():
    def parse_detail_data(self,html):
        data = dict()
        model_name = html.xpath('//div[@class="cd_m_info cd_m_info_zjf"]/div[2]/div[1]/span/text()')[0].strip()
        data["车型名字"] = model_name
        car_mileage = html.xpath('//ul[@class="cd_m_info_desc"]/li[2]/a/text()')[0].strip()
        data["里程"] = car_mileage
        emission_stand = html.xpath('//ul[@class="cd_m_info_desc"]/li[3]/span[1]/text()')
        data["排放标准"] = emission_stand
        displa = html.xpath('//ul[@class="cd_m_info_desc"]/li[4]/span[1]/text()')
        data["排量"] = displa
        raw_price1 = html.xpath('//p[@class="cd_m_info_price"]/span[2]/span/span/span/b/text()')
        raw_price2 = html.xpath('//b[@class="new-noline"]/text()')
        if raw_price1:
            data["原价"] = raw_price1
        elif raw_price2:
            data["原价"] = raw_price2
        else:
            print("草，还是空的 ")
        getcar_time = html.xpath('//ul[@class="cd_m_info_desc"]/li[5]/span[1]/text()')
        data["车龄"] = getcar_time
        yearly_check_due = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[4]/span[2]/text()')
        data["年检到期"] = yearly_check_due
        insurance_due = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[5]/span[2]/text()')
        data["保险到期"] = insurance_due
        mainten_situ = html.xpath('//div[@class="cd_m_i_pz"]/dl[1]/dd[6]/span[2]/text()')
        data["保养情况"] = mainten_situ
        car_made = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[1]/span[2]/a/text()')[0].strip()
        data["制造商"] = car_made
        car_mod = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[2]/span[2]/a/text()')[0].strip()
        data["车型"] = car_mod
        color = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[3]/span[2]/a/text()')[0].strip()
        data["颜色"] = color
        struct = html.xpath('//div[@class="cd_m_i_pz"]/dl[2]/dd[4]/span[2]/a/text()')[0].strip()
        data["车身结构"] = struct
        engin = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[1]/span[2]/text()')
        data["发动机"] = engin
        transmiss = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[2]/span[2]/a/text()')[0].strip()
        data["变速箱"] = transmiss
        fuel_mode = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[4]/span[2]/text()')
        data["燃油类型"] = fuel_mode
        drive_mode = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[5]/span[2]/text()')
        data["驱动形式"] = drive_mode
        fuel_consum = html.xpath('//div[@class="cd_m_i_pz"]/dl[3]/dd[6]/span[2]/text()')
        data["油耗"] = fuel_consum
        car_year = html.xpath('//ul[@class="cd_m_info_desc"]/li[1]/span[1]/text()')
        data["年份"] = car_year
        return data
    def get_pro_data(self,html):
        pass


        # return data
        #以下爬取的是车辆的质量检测报告项目
if __name__ == '__main__':
    red= redis_or.Redis_Data()
    s = Slave_Spisder()
    # url = "https://www.xin.com/40d0a41wy9/che59723067.html?channel=a49b117c44837d110753e751863f53"
    f = open("graph_test_data","a",encoding="utf-8")
    for i in range(600):
        try:
            url = red.pop_data("shenzhen_youxin")
            r = requests.get("http://"+url)
            time.sleep(1)
            print(url)
            html = etree.HTML(r.text)
            data = s.parse_detail_data(html)
            f.write(str(data)+"\n")
            print(data)
        except:
            continue





    # red= redis_or.Redis_Data()
    # h = master.Master_Spider("shenzhen")
    # s = Slave_Spisder()
    # f = open("shenzhen_new_data", "a",encoding="utf-8")
    # for i in range(1000):
    #     try:
    #         data = r.pop_data("shenzhen_youxin")
    #         html = h.get_html("http://"+data)
    #         time.sleep(1.9)
    #         detai = s.parse_detail_data(html)
    #         print(detai)
    #         f.write(str(detai)+"\n")
    #     except:
    #         # f.close()
    #         print("异常的连接",data)
    #         continue
    #
    # f.close()











