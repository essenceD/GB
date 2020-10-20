from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, name, size, height):
        self.name = name
        self.size = size
        self.height = height

    def __str__(self):
        return f'model: {self.name}\nsize: {self.size}\nheight: {self.height}'

    @abstractmethod
    def get_stuff(self):
        pass

    @abstractmethod
    def show_type(self):
        print(f'{self.name}')


class Suite(Clothes):
    @property
    def get_stuff(self):
        return round(2 * self.height / 100 + 0.3, 2)

    def __str__(self):
        return f'{self.name} is Suite'

    def show_type(self):
        pass


class Coat(Clothes):
    @property
    def get_stuff(self):
        return round(self.size / 6.5 + 0.5, 2)

    def __str__(self):
        return f'{self.name} is Coat'

    def show_type(self):
        pass


stuff = 0
a = Suite('Fellini', 54, 190)
b = Suite('Brioni', 48, 186)
c = Coat('Massimo Dutti', 42, 174)
d = Coat('Brunello Cucinelli', 44, 168)
e = Suite('Corneliani', 44, 162)
wardrobe = [a, b, c, d, e]
for i in wardrobe:
    stuff += i.get_stuff
    print(f'{i}')
    print(f'\t{i.get_stuff} sq.meters')
print(f'\nTotally you need: {round(stuff, 2)} sq.meters of stuff')






