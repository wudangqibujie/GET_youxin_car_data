f = open("sibalu.txt",encoding="utf-8")
de = eval(f.read())
print(de)
a = zip(de.values(),de.keys())
print(sorted(a))

