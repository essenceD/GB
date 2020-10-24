class MyClass:
    def __init__(self, p_1):
        self.p_1 = p_1

    def m_1(self):
        print('Hi!')


    @staticmethod
    def m_2():
        #print('Hi! Hi! Hi!'
        return MyClass().m_1()

    @staticmethod
    def m_2_2():
        #print('Hi! Hi! Hi!'
        return MyClass(78).p_1


    @classmethod
    def m_3(cls):
        print(cls.m_2_2())
        print(cls('666').m_1())



my_1 = MyClass(9)
#my_1.m_1()
#MyClass.m_1()   # doesnt work
#MyClass.m_2()
#my_1.m_2()
#my_1.m_2_2()
my_1.m_3()






