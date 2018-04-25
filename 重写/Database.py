import pymongo

class Data2Base(object):
    def __init__(self,db_name):
        self.client = pymongo.MongoClient("localhost",27017)
        self.db = self.client[db_name]
    def insert_coll(self,coll_name,data):
        coll = self.db[coll_name]
        coll.insert(data)

class Data2Txt(object):
    def __init__(self,filename):
        self.f = open(filename,"a",encoding="utf-8")
    def insert_item(self,data):
        data = str(data)
        self.f.write(data+"\n")
    def colse_txt(self):
        self.f.close()
