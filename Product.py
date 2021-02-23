import files as fl
import funcs as fn
import os
import random as rd

cats = 'categories'
ind = 'index'
lines = 'lines'
bars = 'bars'
sample_line = fr'{lines}\sample.txt'
sample_prod = r'base\sample.txt'


class Product:

    bar_code = '0'
    units = {1: 'pcs', 2: 'kilos', 3: 'liters'}
    cur = {1: 'RUR', 2: 'USD', 3: 'EUR'}
    brand = 'New Brand'
    prod = 'Default product'
    model = 'New Model'
    name = 'New Brand_New Model'
    quantity = [0, units[1]]
    p_price = [0, cur[1]]
    r_price = [0, cur[1]]
    location = 'base'

    def __str__(self):      # To show data from class

        info = [self.bar_code, self.prod, self.name, self.quantity, self.r_price, self.store]
        return ' '.join([str(i) for i in info])

    def __init__(self):

        req_prod = fn.choose(fn.get_dict(fl.cat), title=cats)
        if req_prod == '__empty__':
            print('You have to create category first.')
            return
        else:
            self.prod = req_prod
        self.brand = self.get_brand(self.prod)
        self.model = self.get_model(f'{self.prod} {self.brand}')
        self.name = f'{self.brand}_{self.model}'
        self.quantity = self.get_quantity()
        self.p_price = self.get_price_pur()
        self.r_price = self.get_price_rit()
        self.store = fn.choose(fn.get_dict(fl.lines), title=lines)
        self.bar_code = self.get_bar()
        self.info = {'bar': self.bar_code,
                     'type': self.prod,
                     'brand': self.brand,
                     'model': self.model,
                     'p_price': f'{self.p_price[0]} {self.p_price[1]}',
                     'r_price': f'{self.r_price[0]} {self.r_price[1]}',
                     'specs': ['None']}
        self.to_line = [self.bar_code,
                        self.brand,
                        self.model,
                        f'{self.p_price[0]}',
                        f'{self.p_price[1]}',
                        f'{self.r_price[0]}',
                        f'{self.r_price[1]}',
                        f'{self.quantity[0]}',
                        f'{self.quantity[1]}']
        fn.create_file(self.location, self.name, sample_prod)
        fn.update_prod(self.info, fn.get_file_name(self.location, self.name))
        fn.update_index(bar=self.bar_code, type_=self.prod, name=self.name, folder=self.location)
        fn.update_line(fn.get_file_name('lines', self.store), self.to_line)
        fn.update_log(action=f'ADD SUCCESSFUL  New product ~{self.prod} {self.name}~ bar ~{self.bar_code}~ '
                             f'added and placed to ~{self.store}~ in quantity of '
                             f'~{self.quantity[0]} {self.quantity[1]}~ successfully.')

    @staticmethod       # To set brand
    def get_brand(type_):

        name = input(f'Enter brand of new {type_}: ')
        print(f'Name has been set: {name}\n')
        return name

    @staticmethod       # To set model
    def get_model(type_):

        name = input(f'Enter model of new {type_}: ')
        print(f'Model has been set: {name}\n')
        return name

    def get_bar(self):      # to set bar-code returns str(bar)

        if not os.path.isfile(fn.get_file_name(self.location, self.name)):
            with open(fl.bar, 'r', encoding='utf-8') as file_r:
                data = file_r.readlines()
            existing_bars = []
            for i in data:
                existing_bars.append(str(i.split()[0]))
            while True:
                bar = str(rd.randint(1000000, 9999999))
                if bar not in existing_bars:
                    break
            with open(fl.bar, 'a', encoding='utf-8') as file_a:
                print(f'{bar} {self.name}', file=file_a)
            fn.update_log(action=f'CREATED Bar code ~{bar}~ has been created for {self.prod} {self.name}.')
        else:
            with open(fn.get_file_name(self.location, self.name), 'r', encoding='utf-8') as file_r:
                bar = file_r.readlines()[0].split()[1]
        return bar

    def get_quantity(self):      # To set quantity

        quantity = [fn.get_float(name='Quantity', attachment=self.brand, unit=self.model),
                    fn.choose(self.units, title='Units', new=False)]
        print(f'Quantity has been set: {quantity[0]} {quantity[1]}\n')
        return quantity

    def get_price_pur(self):      # To set purchase price

        self.p_price = [fn.get_float(name='Purchase price', attachment=self.prod, unit=self.name),
                        fn.choose(self.cur, title='Currency', new=False)]
        print(f'Purchase price has been set: {self.p_price[0]} {self.p_price[1]}\n')
        return self.p_price

    def get_price_rit(self):      # To set retail price

        self.r_price = [fn.get_float(name='Retail price', attachment=self.prod, unit=self.name),
                        fn.choose(self.cur, title='Currency', new=False)]
        print(f'Retail price has been set: {self.r_price[0]} {self.r_price[1]}\n')
        return self.r_price
