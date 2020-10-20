from abc import ABC, abstractmethod


class MyAbstractMethod(ABC):
    @abstractmethod
    def my_method_1(self):
        pass

    @abstractmethod
    def my_method_2(self):
        pass


class MyClass(MyAbstractMethod):
    def my_method_1(self):
        pass

    def my_method_2(self):
        pass

my_1 = MyClass()
print(my_1)
