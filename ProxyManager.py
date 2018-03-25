URL = "http://httpbin.org/ip"
# URL = "http://pv.sohu.com/cityjson?ie=utf-8"
#  http://www.mogumiao.com/moitor
import requests
import random

a = ["113.121.241.132:42040","49.64.176.254:23441","113.121.241.44:39747","121.224.86.232:45113","100.76.186.17:44993"]
de = random.choice(a)
fr = random.choice(a)
print(de)
# proxies = {
#   "http": "http://"+de,
#   "https": "http://"+fr,
# }
# print(proxies)
ip = "113.121.242.225"
port = "48930"
proxies = {"https":ip+":"+ port,"http":ip+":"+ port}
for i in range(5):
    try:
        r = requests.get(URL,proxies = proxies)
        data = r.text
        print(ip in data)
        print(data)
    except requests.exceptions.ProxyError as e:
        print(proxies,"这个代理有问题啊")
        print(e)
    except requests.exceptions.ConnectTimeout as e:
        print(proxies,"请求超时")
        print(e)
    except requests.exceptions.ConnectionError as e:
        print("连接错误",e)
    else:
        print("其他问题")
        continue
    finally:
        print("---------------------")

