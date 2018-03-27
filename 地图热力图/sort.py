def A(text_path):
    f = open(text_path,encoding="utf-8")
    de = eval(f.read())
    # print(de)
    a = zip(de.values(),de.keys())
    print(sorted(a))

if __name__ == '__main__':
    a = ["aodi.txt","baoma.txt","benchi.txt"]
    for i in a:
        A(i)

