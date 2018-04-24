from lxml import etree
import requests
import Item
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36"}

class Parse(object):
    def __init__(self):
        pass
    def master_parse(self,page_source):
        item = Item.Item()
        html = etree.HTML(page_source)
        item_data = html.xpath('//div[@class="_list-con list-con clearfix ab_carlist"]/ul/li')
        for i in item_data:
            item["title"] = i.xpath('@data-title')
            item["price"] = i.xpath('@data-price')
            item["link"] = i.xpath('div[@class="across"]/a/@href')
            item["year_age"] = i.xpath('div[@class="across"]/div[@class="pad"]/span[1]/text()')
            print(item)




if __name__ == '__main__':
    r = requests.get("https://www.xin.com/shenzhen/baoma/",headers=headers)
    p = Parse()
    p.master_parse(r.text)





