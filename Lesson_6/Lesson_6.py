class Transport:
    # atributes
    def __init__(self, name, model, year):
        self.name = name
        self._model = model
        self.__year = year
        print(f'{name}, {model}, {year}')

    # methods
    def on_start(self):
        print(f'Go car {self.name}!')

    def __on_stop(self):
        print('Stop!')



class Auto(Transport):
    def __init__(self, name, model, year, pass_):
        super().__init__(name, model, year)
        self.pass_ = pass_


auto_1 = Auto('Lada', 'Niva 4x4', 2019)
auto_1.on_start()
print(auto_1.name)
print(auto_1._model)
print(auto_1._Auto__year())

auto_1._Auto__on_stop()

auto_2 = Auto('Mazda', 'CX9', 2020)
print(auto_2.name)





