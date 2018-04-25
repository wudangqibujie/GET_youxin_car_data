from lxml import etree
import requests
import multiprocessing as mp
import logging
import re
logging.basicConfig(level=logging.INFO)
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

class Parse(object):
    def __init__(self):
        pass
    def master_parse(self,page_source,q,ad_new):
        html = etree.HTML(page_source)
        item_data = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
        next_item = html.xpath('//div[@class="con-page search_page_link"]/a')
        if next_item:
            if "下一页" in next_item[-1].xpath('text()')[0]:
                next_url = next_item[-1].xpath('@href')
                logging.info("下一页连接"+next_url)
                ad_new.sadd("new_master_task",next_url)
        for i in item_data:
            item = dict()
            item["title"] = i.xpath('@data-title')
            item["price"] = i.xpath('@data-price')
            item["link"] = i.xpath('div[@class="across"]/a/@href')
            item["year_age"] = i.xpath('div[@class="across"]/div[@class="pad"]/span[1]/text()')
            logging.info(item)
            q.put(item)
    def slave_master(self,page_source):
        item = dict()
        html = etree.HTML(page_source)
        item["title"] = html.xpath('//div[@class="cd_m_info_it2"]/div[1]/span/text()')
        item["now_price"] = html.xpath('//span[@class="cd_m_info_jg"]/b/text()')
        item["ex_price"] = html.xpath('//span[@class="cd_m_cursor"]/b/text()')
        item["year"] = html.xpath('//ul[@class="cd_m_info_desc"]/li[1]/span[1]/text()')
        item["age"] = html.xpath('//ul[@class="cd_m_info_desc"]/li[2]/a/text()')
        item["emmision_standard"] = html.xpath('//ul[@class="cd_m_info_desc"]/li[3]/span[1]/text()')
        item["pailiang"] = html.xpath('//ul[@class="cd_m_info_desc"]/li[4]/span[1]/text()')
        you_report = html.xpath('//div[@class="MD-cardetail-car_quality_examining_report-jp-flaw-im-box  MD-cardetail-car_quality_examining_report-car_quality_report_wrap"]')
        if you_report:
            refer_link = html.xpath('//link[@rel="canonical"]/@href')
            print(refer_link)
            car_id = html.xpath('//a[@class="p-favorite"]/@data-carid')
            print(car_id)
            if car_id and refer_link:
                item["you_report"] = self.get_you_report(refer_link[0],car_id[0])
        comm_report = html.xpath('//div[@class="damage"]')
        if comm_report:
            error_num = html.xpath('//div[@class="nor_ab_head"]/span[1]/text()')
            el = html.xpath('//div[@class="nor_abnormal"]/div[@class="yc_list"]/ul/li')
            if el:
                error_list = [i.xpath('text()') for i in el]
                item["common_report"] = [error_num,error_list]
        return item

    def get_you_report(self,refer_link,car_id):
        headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36",
                   "Referer":refer_link}

        url = "https://www.xin.com/apis/ajax_report/get_chake_report/?carid="+car_id
        print(url)
        r = requests.get(url,headers=headers)
        return r.text.encode('latin-1').decode('unicode_escape')
if __name__ == '__main__':
    r = requests.get("https://www.xin.com/40d0358dy9/che77280557.html",headers=headers)
    p = Parse()
    p.slave_master(r.text)










