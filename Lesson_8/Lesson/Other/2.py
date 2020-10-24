class MyClass:
    def __init__(self, f_name, l_name):
        self.f_name = f_name
        self.l_name = l_name

    @classmethod
    def set_fio(cls, data):
        print(data)
        name_1, name_2 = data
        print(name_1)
        print(name_2)
        return cls(name_1, name_2)

    @staticmethod
    def get_fio_2(obj):
        return f'{obj.f_name} {obj.l_name}'


my_list = ['Chilly', 'Willy']
my_1 = MyClass.set_fio(my_list)
print(my_1.get_fio_2(my_1))







