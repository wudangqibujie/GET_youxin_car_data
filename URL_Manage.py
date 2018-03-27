from collections import deque
class URL_Manager():
    new_all = {}
    old_all = {}
    def __init__(self,city):
        self.old_urls = deque([])
        self.new_urls = deque([])
        self.new_all[city] = self.new_urls
        self.old_all[city] = self.old_urls
    def add_url(self,new_url):
        self.new_urls.append(new_url)
    def pop_url(self):
        n = self.new_urls.popleft()
        self.old_urls.append(n)
        return n
    @property
    def old_urls_set(self):
        return self.old_urls
    @property
    def new_urls_set(self):
        return self.new_urls
    @classmethod
    def get_all(cls):
        return cls.new_all,cls.old_all
if __name__ == '__main__':
    a = URL_Manager("shenzhen")
    a.add_url("BMW")
    a.add_url("M5")
    a.pop_url()
    b = URL_Manager("guangzhou")
    b.add_url("BENZ")
    b.add_url("AMG")
    c,d = URL_Manager.get_all()
    print(c)
    print(d)




