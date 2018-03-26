import requests
from lxml import etree
import threading
from multiprocessing import Process
import time
from PIL import Image
HEADERS = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36","Accept":"*/*","Accept-Encoding": "gzip, deflate, br","X-Requested-With": "XMLHttpRequest","Referer": "http://www.xin.com/checker/?redirect=%2F%3Fchannel%3Da49b117c44837d110753e751863f53","Connection": "keep-alive","Host": "www.xin.com","Content-Length": "26"}

def yan():
    url = "https://www.xin.com/"
    r = requests.get(url)
    # print(r.text)
    html = etree.HTML(r.text)
    itm = html.xpath('/html/body/div/div/div[2]/p[1]/span/img/@src')
    get_img = requests.get("http://www.xin.com/"+itm[0])

    f = open("ma.jpg","wb")
    f.write(get_img.content)
    f.close()
    im = Image.open('ma.jpg')
    im.show()
    print(itm)
def multi_thread():
    aa = []
    for i in range(50):
        thread = threading.Thread(target=yan,args=(i,))
        aa.append(thread)
    for i in aa:
        i.start()
def multi_proce():
    aa = []
    for i in range(50):
        p = Process(target=yan, args=(i,))
        aa.append(p)
    for i in aa:
        i.start()
def main1():
    import time
    # a1 = time.time()
    # multi_thread()
    # a2 = time.time()
    # print("多线程", a2 - a1)

    b1 = time.time()
    multi_proce()
    b2 = time.time()
    print("多进程", b2 - b1)
def post_data():
    s = requests.Session()
    yan()
    r2 = s.get("https://www.xin.com/",headers = HEADERS)
    print(r2.url)
    yanma = input()
    post_data = {"vcode":yanma,"t":str(int(time.time()*1000))}
    print(post_data)
    r1 = requests.post("http://www.xin.com/checker/validate/",data=post_data,headers = HEADERS)
    print(r1.url)
    print(r1.text)

if __name__ == '__main__':







    post_data()
# 1521809738678
# 1521809844840
# 152180865053
# 1521808507653
# 1521808607742
# 1521808666011
# 1521808707171