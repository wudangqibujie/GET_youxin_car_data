import hashlib

f = open("guangzhou.txt")
g = open("md5.txt","w")
def hash_md5(url):
    m = hashlib.md5()
    m.update(url.encode("utf-8"))
    md5_url = m.hexdigest()
    return md5_url

if __name__ == '__main__':
#     for i in f:
#         print(i)
#         j = hash_md5(i)
#         g.write(j)
# f.close()
# g.close()
    print(hash_md5("www.baidu.com"))