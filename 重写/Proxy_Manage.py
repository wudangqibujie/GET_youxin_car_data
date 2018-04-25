import requests
import redis
import time
import logging
#格式{'code': '0', 'msg': [{'port': '41891', 'ip': '27.157.128.140'}, {'port': '39446', 'ip': '171.13.37.90'}, {'port': '26771', 'ip': '125.104.237.238'}, {'port': '48122', 'ip': '182.42.47.108'}, {'port': '28414', 'ip': '113.121.166.75'}, {'port': '49566', 'ip': '222.95.36.157'}, {'port': '32723', 'ip': '114.230.96.108'}, {'port': '23932', 'ip': '122.237.240.118'}, {'port': '48786', 'ip': '61.143.20.46'}, {'port': '47525', 'ip': '123.161.152.49'}, {'port': '32976', 'ip': '114.239.2.233'}, {'port': '24336', 'ip': '122.4.45.212'}, {'port': '23738', 'ip': '180.107.57.124'}, {'port': '35513', 'ip': '49.85.5.137'}, {'port': '34595', 'ip': '123.163.128.82'}, {'port': '34185', 'ip': '218.66.151.60'}, {'port': '39164', 'ip': '171.11.229.52'}, {'port': '38790', 'ip': '117.26.186.45'}, {'port': '22321', 'ip': '27.158.148.254'}, {'port': '47925', 'ip': '180.113.80.217'}]}

class Proxy(object):
        def __init__(self):
            self.r = redis.Redis(host="localhost",port=6379)
            self.url = "http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=c69b1816b29b43ea9dba7a1cbf1e1161&count=20&expiryDate=1&format=1"
        def get_ip(self):
            r = requests.get(self.url)
            raw_ip = eval(r.text)
            print(raw_ip)
            ip_list = []
            for i in raw_ip["msg"]:
                ip = i["ip"] +":"+ i["port"]
                ip_list.append(ip)
            return ip_list
        def ip2redis(self):
            for i in self.get_ip():
                self.r.sadd("ip_queue",i)
        def proxy_run(self):
            while True:
                try:
                    self.ip2redis()
                    time.sleep(360)
                    self.r.delete("ip_queue")
                except:
                    print("IP提取有问题")
                    break

if __name__ == '__main__':
    pass
    # r = redis.Redis(host="localhost",port=6379)
    # r.sadd("BMW","M5")
    # r.delete("BMW")





