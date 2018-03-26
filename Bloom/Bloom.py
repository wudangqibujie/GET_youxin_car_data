import random
from bitmap import BitMap

#https://blog.csdn.net/chndata/article/details/49817795
class BloomFilter:
    def __init__(self, mapsize=160000, max_node_size=10000, random_num=8):
        self.m = mapsize
        self.n = max_node_size
        self.k = random_num
        self.bitmap = BitMap(maxnum=self.m)
        self.count = 0;
        pass

    def set(self, string):
        calcmap = self.calcMap(string)
        for x in calcmap:
            self.bitmap.set(x)
        pass

    def test(self, string):
        calcmap = self.calcMap(string)
        for x in calcmap:
            if not self.bitmap.test(x):
                return False
        return True

    def calcMap(self, string):
        r = random.Random(string)
        lv1random = [r.random() for x in range(self.k)]
        return [int(random.Random(x).random()*self.m) for x in lv1random]
if __name__ == '__main__':
    c = BloomFilter()
    f = open("guangzhou.txt")
    g = open("we.txt")
    for i in f:
        c.set(i.strip())

    for i in g:
        print(c.test(i.strip()))
    # c.set("BMW")
    # print(c.test("AMG"))
    # print(c.calcMap("BENZ"))