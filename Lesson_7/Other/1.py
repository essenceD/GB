class MyClass:
    def __init__(self, p_1):
        self.p_1 = p_1

    def __str__(self):
        return f'{self.p_1}'

    def __call__(self, new_):
        self.p_1 = new_


my_1 = MyClass(55)
my_2 = MyClass(11)
print(my_1, my_2)

my_1('one')
my_2('two')
print(my_1, my_2)



