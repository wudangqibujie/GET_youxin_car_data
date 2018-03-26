import hashlib

m = hashlib.md5()
f = open("md5_test.txt")
aa=[f.readline().strip() for _ in range(20)]
print(aa)
def A(url):
    m.update(url.strip().encode("utf-8"))
    return m.hexdigest()
bb = [A(url) for url in aa]
print(bb)
print(A(aa[5]) in bb)

