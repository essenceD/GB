from abc import abstractmethod

path = r'Source\base.txt'
strg = r'Source\Storage.txt'
line_1 = r'Source\Line_1.txt'
line_2 = r'Source\Line_2.txt'
line_3 = r'Source\Line_3.txt'


class Warehouse:
    storage = {'Line_1': ['Printer', 0, 'Scanner', 0, 'Copier', 0],
               'Line_2': ['Printer', 0, 'Scanner', 0, 'Copier', 0],
               'Line_3': ['Printer', 0, 'Scanner', 0, 'Copier', 0]}
    capacity = {'Printer': 0, 'Scanner': 0, 'Copier': 0}
    products = {1: 'Printer', 2: 'Scanner', 3: 'Copier'}
    showcase = {1: 'In detail', 2: 'In warehouse', 3: 'In line'}
    line = {1: 'Line_1', 2: 'Line_2', 3: 'Line_3'}

    def add_prod(self):
        prod = self.choose(self.products, title='Product')
        if prod == 'Printer':
            a = Printer()
            a.save()
        elif prod == 'Scanner':
            a = Scanner()
            a.save()
        elif prod == 'Copier':
            a = Copier()
            a.save()

    def show(self):
        shw = self.choose(self.showcase, title='Display method')
        if shw == 'In detail':
            with open(path, 'r', encoding='utf-8') as file_r:
                print(file_r.read())
        elif shw == 'In warehouse':
            with open(strg, 'r', encoding='utf-8') as file_r:
                print(file_r.read())
        elif shw == 'In line':
            ln = self.choose(self.line, title='The storage')
            if ln == 'Line_1':
                with open(line_1, 'r', encoding='utf-8') as file_r:
                    print(file_r.read())
            elif ln == 'Line_2':
                with open(line_2, 'r', encoding='utf-8') as file_r:
                    print(file_r.read())
            elif ln == 'Line_3':
                with open(line_3, 'r', encoding='utf-8') as file_r:
                    print(file_r.read())

    def move_prod(self):
        what = self.choose(self.products, title='PRODUCT you want to move')
        num = self.get_float(name='Number', attachment=what)
        from_ = self.choose(self.line, title='FROM where to move')
        to_ = self.choose(self.line, title='TO where to move')
        print('Not ready yet!')





    @staticmethod
    def choose(dict_, title='One of these'):
        print(f'Choose {title}:')
        for i, j in dict_.items():
            print(f'Choose {i} to set {j}')
        while True:
            try:
                choice = int(input('Your choice: '))
            except ValueError:
                print('Enter a number, please!')
            else:
                if choice in dict_.keys():
                    return dict_[choice]

    @staticmethod
    def get_float(name='Parameter', attachment='ClassName', unit='Any Brand'):
        while True:
            try:
                new_data = float(input(f'Enter {name} for {attachment} {unit}: '))
            except ValueError:
                print(f'{name}" Should be a number!')
            else:
                return new_data


class OfficeEquipment:
    storage = {1: 'Line_1', 2: 'Line_2', 3: 'Line_3'}
    units = {1: 'pcs', 2: 'pages/min', 3: 'dpi', 4: 'pages', 5: 'kilos', 6: 'liters'}
    cur = {1: 'RUR', 2: 'USD', 3: 'EUR', 4: 'BANANAS'}
    name = 'New Product'
    quantity = [0, units[1]]
    price = [0, cur[1]]

    def __init__(self):
        with open(path, 'r', encoding='utf-8') as f:
            counter = int(f.readlines()[-1].strip('\n'))
        self.get_name(type_=self.__class__.__name__)
        self.get_quantity()
        self.get_price()
        self.id = counter

    def get_name(self, type_='ClassName'):
        self.name = input(f'Enter name of new {type_}: ')
        print(f'Name has been set: {self.name}\n')
        return self.name

    def get_quantity(self):
        self.quantity = [self.get_float(name='Quantity', attachment=self.__class__.__name__, unit=self.name),
                         self.choose(self.units, title='Units')]
        print(f'Quantity has been set: {self.quantity}\n')
        return self.quantity

    def get_price(self):  # Enterprise =)
        self.price = [self.get_float(name='Price', attachment=self.__class__.__name__, unit=self.name),
                      self.choose(self.cur, title='Currency')]
        print(f'Price has been set: {self.price}\n')
        return self.price

    @abstractmethod
    def __str__(self):
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price]
        return ' '.join([str(i) for i in info])

    @abstractmethod
    def save(self):
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price]
        with open(path, 'a', encoding='utf-8') as file:
            print(info, file=file)
            print(str(self.id + 1), file=file)


    @staticmethod
    def choose(dict_, title='One of these'):
        print(f'Choose {title}:')
        for i, j in dict_.items():
            print(f'Choose {i} to set {j}')
        while True:
            try:
                choice = int(input('Your choice: '))
            except ValueError:
                print('Enter a number, please!')
            else:
                if choice in dict_.keys():
                    return dict_[choice]

    @staticmethod
    def get_float(name='Parameter', attachment='ClassName', unit='Regular Brand'):
        while True:
            try:
                new_data = float(input(f'Enter {name} for {attachment} {unit}: '))
            except ValueError:
                print(f'{name}" Should be a number!')
            else:
                return new_data


class Printer(OfficeEquipment):

    def __init__(self):
        super().__init__()
        self.print_life = [self.get_float(name='Printing life', attachment=self.__class__.__name__, unit=self.name),
                           self.choose(self.units, title='Printing life')]
        self.store = self.choose(self.storage, title='Storage place')

    def __str__(self):
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price, self.print_life, self.store]
        return ' '.join([str(i) for i in info])

    def save(self):
        # to update base.txt
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price, self.print_life, self.store]
        with open(path, 'a', encoding='utf-8') as file:
            print(info, file=file)
            print(str(self.id + 1), file=file)
        # to update line*.txt
        new_path = 'Source\\' + self.store + '.txt'
        with open(new_path, 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
            content = [x.strip() for x in content]
        with open(new_path, 'w', encoding='utf-8') as reset:
            pass
        with open(new_path, 'a', encoding='utf-8') as file_w:
            for i in content:
                if self.__class__.__name__ in i.split():
                    print(str(i.split()[0]) + ' ' + str(float(i.split()[1]) + self.quantity[0]), file=file_w)
                else:
                    print(str(i.split()[0]) + ' ' + str(i.split()[1]), file=file_w)
        # to update Storage.txt
        total = {}
        with open(strg, 'r', encoding='utf-8') as file_r:
            for i in file_r:
                key, *value = i.split()
                total[key] = value
            for i in total.keys():
                if i == self.store:
                    for k in range(len(total[i]) - 1):
                        if total[i][k] == self.__class__.__name__:
                            _ = total[i][k + 1]
                            total[i][k + 1] = float(_) + self.quantity[0]
        with open(strg, 'w', encoding='utf-8') as reset:
            pass
        with open(strg, 'a', encoding='utf-8') as file_w:
            for i in total.keys():
                res = i
                for j in total[i]:
                    res += ' ' + str(j)
                print(res, file=file_w)


class Scanner(OfficeEquipment):

    def __init__(self):
        super().__init__()
        self.scan_res = [self.get_float(name='Scanning Resolution', attachment=self.__class__.__name__, unit=self.name),
                         self.choose(self.units, title='Scanning Resolution')]
        self.store = self.choose(self.storage, title='Storage place')

    def __str__(self):
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price, self.scan_res, self.store]
        return ' '.join([str(i) for i in info])

    def save(self):
        # to update base.txt
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price, self.scan_res, self.store]
        with open(path, 'a', encoding='utf-8') as file:
            print(info, file=file)
            print(str(self.id + 1), file=file)
        # to update line*.txt
        new_path = 'Source\\' + self.store + '.txt'
        with open(new_path, 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
            content = [x.strip() for x in content]
        with open(new_path, 'w', encoding='utf-8') as reset:
            pass
        with open(new_path, 'a', encoding='utf-8') as file_w:
            for i in content:
                if self.__class__.__name__ in i.split():
                    print(str(i.split()[0]) + ' ' + str(float(i.split()[1]) + self.quantity[0]), file=file_w)
                else:
                    print(str(i.split()[0]) + ' ' + str(i.split()[1]), file=file_w)
        # to update Storage.txt
        total = {}
        with open(strg, 'r', encoding='utf-8') as file_r:
            for i in file_r:
                key, *value = i.split()
                total[key] = value
            for i in total.keys():
                if i == self.store:
                    for k in range(len(total[i]) - 1):
                        if total[i][k] == self.__class__.__name__:
                            _ = total[i][k + 1]
                            total[i][k + 1] = float(_) + self.quantity[0]
        with open(strg, 'w', encoding='utf-8') as reset:
            pass
        with open(strg, 'a', encoding='utf-8') as file_w:
            for i in total.keys():
                res = i
                for j in total[i]:
                    res += ' ' + str(j)
                print(res, file=file_w)


class Copier(OfficeEquipment):

    def __init__(self):
        super().__init__()
        self.consumption = [self.get_float(name='Printing speed', attachment=self.__class__.__name__, unit=self.name),
                            self.choose(self.units, title='Printing speed')]
        self.store = self.choose(self.storage, title='Storage place')

    def __str__(self):
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price, self.consumption, self.store]
        return ' '.join([str(i) for i in info])

    def save(self):
        # to update base.txt
        info = [self.id, self.__class__.__name__, self.name, self.quantity, self.price, self.consumption, self.store]
        with open(path, 'a', encoding='utf-8') as file:
            print(info, file=file)
            print(str(self.id + 1), file=file)
        # to update line*.txt
        new_path = 'Source\\' + self.store + '.txt'
        with open(new_path, 'r', encoding='utf-8') as file_r:
            content = file_r.readlines()
            content = [x.strip() for x in content]
        with open(new_path, 'w', encoding='utf-8') as reset:
            pass
        with open(new_path, 'a', encoding='utf-8') as file_w:
            for i in content:
                if self.__class__.__name__ in i.split():
                    print(str(i.split()[0]) + ' ' + str(float(i.split()[1]) + self.quantity[0]), file=file_w)
                else:
                    print(str(i.split()[0]) + ' ' + str(i.split()[1]), file=file_w)
        # to update Storage.txt
        total = {}
        with open(strg, 'r', encoding='utf-8') as file_r:
            for i in file_r:
                key, *value = i.split()
                total[key] = value
            for i in total.keys():
                if i == self.store:
                    for k in range(len(total[i]) - 1):
                        if total[i][k] == self.__class__.__name__:
                            _ = total[i][k + 1]
                            total[i][k + 1] = float(_) + self.quantity[0]
        with open(strg, 'w', encoding='utf-8') as reset:
            pass
        with open(strg, 'a', encoding='utf-8') as file_w:
            for i in total.keys():
                res = i
                for j in total[i]:
                    res += ' ' + str(j)
                print(res, file=file_w)
