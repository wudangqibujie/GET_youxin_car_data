import sys
sys.path.append("..")
import redis_or
#导入模块的姿势
A = redis_or.Redis_Data()
f = open("md5_test.txt","w")
for i in range(9000):
    f.write(A.pop_data("quanzhou_youxin")+"\n")
f.close()