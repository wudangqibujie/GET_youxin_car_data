import sys
sys.path.append("..")
import redis_or
#导入模块的姿势
A = redis_or.Redis_Data()
f = open("../guangzhou.txt")
for i in f:
    A.set_into_data("bloon_youxin",i)
