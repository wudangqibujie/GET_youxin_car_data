import time
from functools import wraps
from timeit import timeit
#时间测试
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start))
        return r
    return wrapper

@timethis
def countdown(n):
    while n > 0:
        n -= 1
        print(n)


if __name__ == '__main__':
    # print(timeit("requests.get('http://www.baidu.com')","import requests",number=50))
    print(timeit("countdown(10)",number=50))

