import heapq

def create_data_set():
    f = open("test_data.txt",encoding="utf-8")
    da = [eval(i) for i in f.readlines()]
    return da
def sort_data():
    data = create_data_set()
    data = [float(i["里程"].replace("万公里","")) for i in data]
    sort_ = heapq.nlargest(5,create_data_set(),lambda s:s["里程"])
    print(sort_)

if __name__ == '__main__':
    sort_data()
