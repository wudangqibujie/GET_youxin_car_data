import redis
class A():
    def puter(self,set_name):
        def red(func):
            r = redis.Redis(host="localhost",port=6379)
            def inner():
                list = func()
                for i in list:
                    r.sadd(set_name,i)
                return func()
            return inner
        return red

a=A()

@a.puter("M6")
def create_list():
    a= ["https://blog.csdn.net/liu88010988/article/details/50789960","http://www.pythontip.com/coding/code_oj_case/163"]
    return a

create_list()

# if __name__ == '__main__':
#     create_list()
