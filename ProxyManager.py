import requests
ip_url = "http://www.mogumiao.com/web"
from lxml import etree
import time
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)



headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36"}
def get_html(url):
    try:
        r = requests.get(url,headers = headers)
        if r.status_code == 200:
            data = r.text
            logger.info("请求回来的")
            return data
        else:
            print("响应码异常！")
    except:
        print("请求异常!")
def parse_ip(html):
    print(html)
    ip = eval(html)

    logger.debug("出问题的IP源代码",html)
    ip_port = ip["msg"]
    logger.info("解析出来的IP数据")
    return ip_port

def ip_test(ip_port):
    URL = "http://httpbin.org/ip"
    proxies = {"http":ip_port,"https":ip_port}
    f_valid = open("valid_ip.txt","a")
    f_timeout_ip = open("timeout_ip.txt","a")
    f_invalid_ip = open("invalid_ip.txt","a")
    try:
        r = requests.get(URL,proxies = proxies,timeout = 5)
        res = r.text
        logger.info("测试的返回代码")
        logger.info("正在使用的代理")
        logger.debug("返回源代码")
        if ip_port.split(":")[0] in res:
            print(ip_port+"IP有效")
            f_valid.write(ip_port+"\n")
            print(res)
        else:
            print("没有用到代理IP。")
    except requests.exceptions.ProxyError as e:
        # print(ip_port,"这个代理有问题啊")
        logger.info("这个代理有问题")
        print(e)
        f_invalid_ip.write(ip_port+"\n")
    except requests.exceptions.ConnectTimeout as e:
        # print(proxies,"请求超时")
        logger.info("请求超时")
        print(e)
        f_timeout_ip.write(ip_port+"\n")
    except requests.exceptions.ConnectionError as e:
        print("连接有误")
        print(e)
        f_invalid_ip.write(ip_port+"\n")
    except:
        pass
    finally:
        f_valid.close()
        f_invalid_ip.close()
        f_timeout_ip.close()

def main():
    html = get_html("http://www.mogumiao.com/proxy/free/listFreeIp")
    ip = parse_ip(html)
    for i in ip[:]:
        port = i["port"]
        ip = i["ip"]
        ip_port = ip+":"+port
        ip_test(ip_port)


if __name__ == '__main__':
    main()
    # for i in range(10):
    #     main()
    #     time.sleep(300)







# URL = "http://httpbin.org/ip"
# # URL = "http://pv.sohu.com/cityjson?ie=utf-8"
# #  http://www.mogumiao.com/moitor
# import requests
# import random
#
# a = ["113.121.241.132:42040","49.64.176.254:23441","113.121.241.44:39747","121.224.86.232:45113","100.76.186.17:44993"]
# de = random.choice(a)
# fr = random.choice(a)
# print(de)
# ip = "113.121.242.225"
# port = "48930"
# proxies = {"https":ip+":"+ port,"http":ip+":"+ port}
# for i in range(5):
#     try:
#         r = requests.get(URL,proxies = proxies)
#         data = r.text
#         print(ip in data)
#         print(data)
#     except requests.exceptions.ProxyError as e:
#         print(proxies,"这个代理有问题啊")
#         print(e)
#     except requests.exceptions.ConnectTimeout as e:
#         print(proxies,"请求超时")
#         print(e)
#     except requests.exceptions.ConnectionError as e:
#         print("连接错误",e)
#     else:
#         print("其他问题")
#         continue
#     finally:
#         print("---------------------")

