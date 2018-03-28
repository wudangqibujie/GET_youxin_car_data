import logging
logging.basicConfig(level=logging.INFO)
import numpy
import re


def file_out():
    f = open("test_data.txt",encoding="utf-8")
    return [eval(i) for i in f.readlines()]

def fil_func(car_name):
    def car_fil(data):
        return car_name in data["车型名字"]
    return car_fil

def create_data(func,raw_data_lists):
    return list(filter(func,raw_data_lists))
def data_map(dic):
    a=[dic["车型名字"],dic["里程"],dic["年份"][0],dic["原价"][0]]
    return a
def main(car):
    car_func = fil_func(car)
    data_lis = file_out()
    logging.info(data_lis)
    data_lis = create_data(car_func,data_lis)
    format_data = map(data_map,data_lis)
    return list(format_data)
def data_clean(unclean_data):
    def clean_func(item):
        # print(item)
        item[1] = float(item[1].replace("万公里",""))
        if "年" in item[2] and "月" in item[2]:
            a = item[2].split("个月")[0].split("年")
            item[2] = 12*int(a[0])+int(a[1])
        elif "年" not in item[2]:
            item[2] = int(item[2].split("个月")[0])
        else:
            item[2] = int(item[2].split("年")[0])*12
        item[3] = float(item[3].replace("新车含税","").replace("万",""))
        return item
    after_clean = map(clean_func,unclean_data)
    return list(after_clean)

if __name__ == '__main__':
    data = main("奔驰")
    after_clea = data_clean(data)
    print(numpy.array(after_clea))
    print(after_clea)










# [
#     [],
#     [];
#     []
# ]
