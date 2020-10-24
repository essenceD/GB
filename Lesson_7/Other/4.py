class MyClass:
    def __init__(self, p_1, p_2):
        self.p_1 = p_1
        self.p_2 = p_2

    @property
    def my_method(self):
        return f'params to class: {self.p_1}, {self.p_2}'


mc = MyClass('TEXT_1', 'TEXT_2')
print(mc.p_1)
print(mc.p_2)





