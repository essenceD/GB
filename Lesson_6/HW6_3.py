class Worker:
    def __init__(self, f_name, l_name, position, income):
        self.f_name = str(f_name)
        self.l_name = str(l_name)
        self.position = position
        self._income = {'wage': income[0], 'bonus': income[1]}

    @property
    def income(self):
        return self._income


class Position(Worker):
    def get_full_name(self):
        print(self.l_name, self.f_name, sep=' ')

    def get_total_income(self):
        print('Total income is: {}'.format(self._income['wage'] + self._income['bonus']))


a = Position('Ivan', 'Ivanov', 'Director', [10000, 5000])
print(a.f_name)
print(a.l_name)
print(a.position)
print(a.income, '\n')
Position.get_full_name(a)
Position.get_total_income(a)

