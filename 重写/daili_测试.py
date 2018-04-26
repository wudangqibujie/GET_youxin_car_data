import requests
import redis
test_url = "http://httpbin.org/ip"
r = redis.Redis(host="localhost",port=6379)
while True:
    try:
        proxies = {"http":r.srandmember("free_ip",1)[0].decode("utf-8"),"https":r.srandmember("free_ip",1)[0].decode("utf-8")}
        print(proxies)

        r = requests.get(test_url,proxies=proxies,timeout = 5)
        print(r.text)
    except:
        print("有误",proxies)
        continue
