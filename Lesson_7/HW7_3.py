from abc import ABC, abstractmethod
import math as m


class Cell(ABC):
    def __init__(self, name, size):
        self.name = name
        self.size = size

    @abstractmethod
    def __str__(self):
        row = round(m.sqrt(self.size))
        res = '\n\t'.join([' '.join(['*' for i in range(row)]) if self.size - (j * row) > row else ' '.
                          join(['*' for i in range(self.size - (j * row))]) for j in range(row + 1)])
        return f"{self.name}(POWER={self.size})\n\t{res}\n"

    def __add__(self, other):
        print(f'Result of fusion of {self.name}(POWER={self.size}) and {other.name}(POWER={other.size}) is:')
        win_size = [self.size, other.size].index(max([self.size, other.size]))
        win_name = [self.name, other.name]
        new_cell = self.size + other.size
        return Fused(win_name[win_size], new_cell)

    def __sub__(self, other):
        print(f'Result of fission of {self.name}POWER=({self.size}) and {other.name}(POWER={other.size}) is:')
        try:
            if self.size > other.size:
                return f"{Amoeba(self.name, self.size - other.size)}\r\t~AND~\n{Amoeba(f'{self.name}.Jr', other.size)}"
            else:
                return f'I can\'t make {self.name}.Jr!'
        except AttributeError:
            return f'I can\'t make {self.name}.Jr!'

    def __mul__(self, other):
        print(f'Result of reproduction of {self.name}(POWER={self.size}) and {other.name}(POWER={other.size}) is:')
        win_name = f'{self.name} - {other.name}'
        new_cell = self.size * other.size
        return Reproduced(win_name, new_cell)

    def __truediv__(self, other):
        if self.size // other.size > 0:
            print(f'Result of evolution of {self.name}(POWER={self.size}) and {other.name}(POWER={other.size}) is:')
            win_name = f'{self.name} -><- {other.name}'
            new_cell = self.size // other.size
            return Evolved(win_name, new_cell)
        else:
            return f'Probably, {self.name} will die because of this division. Try different pair!'

    def make_order(self, lane):
        row = lane
        res = '\n'.join([' '.join([self.unit for i in range(row)]) if self.size - (j * row) > row else ' '.
                        join([self.unit for i in range(self.size - (j * row))]) for j in range(row + 1)])
        return f"{self.name}(POWER={self.size}) by {lane} in a row:\n{res}\n"


class Amoeba(Cell):
    unit = chr(1995)

    def __str__(self):
        row = round(m.sqrt(self.size))
        res = '\n\t'.join([' '.join([self.unit + ' ' for i in range(row)]) if self.size - (j * row) > row else ' '.
                          join([self.unit + ' ' for i in range(self.size - (j * row))]) for j in range(row + 1)])
        return f"{self.name}(POWER={self.size})\n\t{res}\n"


class Evolved(Cell):
    unit = chr(2951)

    def __str__(self):
        row = round(m.sqrt(self.size))
        res = '\n\t'.join([' '.join([self.unit + ' ' for i in range(row)]) if self.size - (j * row) > row else ' '.
                          join([self.unit + ' ' for i in range(self.size - (j * row))]) for j in range(row + 1)])
        return f"{self.name}(POWER={self.size})\n\t{res}\n"


class Reproduced(Cell):
    unit = chr(2039)

    def __str__(self):
        row = round(m.sqrt(self.size))
        res = '\n\t'.join([' '.join([self.unit + ' ' for i in range(row)]) if self.size - (j * row) > row else ' '.
                          join([self.unit + ' ' for i in range(self.size - (j * row))]) for j in range(row + 1)])
        return f"{self.name}(POWER={self.size})\n\t{res}\n"


class Fused(Cell):
    unit = chr(1995)

    def __str__(self):
        row = round(m.sqrt(self.size))
        res = '\n\t'.join([' '.join([self.unit * 2 + ' ' for i in range(row)]) if self.size - (j * row) > row else ' '.
                          join([self.unit * 2 + ' ' for i in range(self.size - (j * row))]) for j in range(row + 1)])
        return f"{self.name}(POWER={self.size})\n\t{res}\n"


a = Amoeba('Batman', 3)
print(a)
b = Amoeba('Robin', 4)
print(b)
c = a + b
print(c)
d = b - a
print(d)
e = a * b
print(e)
f = e / a
print(f)
print(e.make_order(7))
