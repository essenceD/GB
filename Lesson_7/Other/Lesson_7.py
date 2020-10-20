#https://github.com/vitalygilev/AI_Python_Base/pull/6/commits/bdbcc33c76a13bcbb787e67d1d43becdd96833c6

'''class MyClass:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __del__(self):
        print('Deleted object!')'''

#my_1 = MyClass(77)
#del my_1
#print(my_1.p_1)

# __str__
'''class MyClass:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def __str__(self):
        return f'{self.p_1}, {self.p_2}'


my_1 = MyClass(77, 88)
print(my_1)
print('HI!')'''

# __add__


class MyClass:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    def __str__(self):
        return f'{self.p_1}, {self.p_2}'

    def __add__(self, other):
        return MyClass(self.p_1 + other.p_1, self.p_2 + other.p_2)


my_1 = MyClass(55, 66)
my_2 = MyClass(11, 22)
my_3 = MyClass(44, 33)
my_4 = MyClass(1001, 2101)
print(my_1 + my_2 + my_3 + my_4)
















