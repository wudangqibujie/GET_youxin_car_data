class A():
    a = 2
    def m1(self,n):
        print(self)
    @classmethod
    def m2(cls):
        cls.a = 5
    @staticmethod
    def m3(n):
        print(n)
if __name__ == '__main__':
    print(A.a)
    A.m2()
    print(A.a)

