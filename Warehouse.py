import files as fl
import funcs as fn
import os

cats = 'categories'
ind = 'index'
lines = 'lines'
bars = 'bars'
sample_line = fr'{lines}\sample.txt'
sample_prod = r'base\sample.txt'


class Warehouse:
    show_case = {1: 'SHOW products Everywhere',
                 2: 'SHOW products in Specific line',
                 3: 'SHOW available storages',
                 4: 'SHOW available categories',
                 5: '<< BACK TO MAIN MENU'}

    create_case = {1: 'CREATE product\'s category',
                   2: 'CREATE storage place',
                   3: '<< BACK TO MAIN MENU'}

    add_case = {1: 'ADD new product',
                2: '<< BACK TO MAIN MENU'}

    do_case = {1: 'DO sell product',
               2: 'DO refund product',
               3: 'DO change product',
               4: 'DO delete product',
               5: 'DO delete storage',
               6: '<< BACK TO MAIN MENU'}

    delete_case = {1: 'DELETE categories',
                   2: 'DELETE product',
                   3: 'DELETE storage',
                   4: '<< BACK TO MAIN MENU'}

    def create(self):
        cr = fn.choose(self.create_case, title='what do you want to create', new=False)
        if cr == self.create_case[1]:
            name = input('Enter new category\'s name: ')
            fn.update_categories(name)

        elif cr == self.create_case[2]:
            self.add_storage()

        elif cr == self.create_case[3]:
            return

    def add_storage(self):
        while True:
            name = input('Enter name for new storage: ')
            with open(fl.lines, 'r', encoding='utf-8') as file_r:
                data = file_r.readlines()
            samples = []
            for i in data:
                samples.append(i)
            if name not in samples:
                fn.update_lines(name)
                break
            else:
                print(f'Unable to create storage ~{name}~. Storage already exists.')

    def show(self):
        shw = fn.choose(self.show_case, title='Display method', new=False)

        if shw == self.show_case[1]:
            locations = []
            with open(fl.lines, 'r', encoding='utf-8') as file_r:
                data = file_r.readlines()
            for i in data:
                locations.append(i.split()[0])
            if len(locations) > 0:
                for j in locations[1:]:
                    print(f'\nStorage ~{j.upper()}~ contents:')
                    with open(fn.get_file_name(lines, j), 'r', encoding='utf-8') as file_r:
                        data = file_r.readlines()
                    for x in data:
                        print(x[:-1])
                fn.update_log(action=f'VIEWED DataBase in case ~{shw}~.')
            else:
                print('There is nothing to show!')

        elif shw == self.show_case[2]:
            shw = fn.choose(fn.get_dict(fl.lines), title=self.show_case[2], new=False)
            if shw == '__empty__':
                print('There is nothing to show!')
            else:
                with open(fn.get_file_name(lines, shw), 'r', encoding='utf-8') as file_r:
                    data = file_r.readlines()
                print(f'\nStorage ~{shw.upper()}~ contents:\n')
                for i in data:
                    print(i[:-1])
                fn.update_log(action=f'VIEWED DataBase in case ~{shw}~.')

        elif shw == self.show_case[3]:
            with open(fl.lines, 'r', encoding='utf-8') as file_r:
                data = file_r.readlines()
            for i in data:
                print(i[:-1])
            fn.update_log(action=f'VIEWED DataBase in case ~{shw}~.')

        elif shw == self.show_case[4]:
            with open(fl.cat, 'r', encoding='utf-8') as file_r:
                data = file_r.readlines()
            for i in data:
                print(i[:-1])
            fn.update_log(action=f'VIEWED DataBase in case ~{shw}~.')

        elif shw == self.show_case[5]:
            return

    def move_prod(self):      # to do!!!!!!
        # what = bar_code
        with open(fl.lines, 'r', encoding='utf-8') as file_r:
            data = file_r.readlines()
        locations = [data[i][:-1] for i in range(len(data)) if i != 0]
        contains = {}
        moving = {}
        units = {}
        if len(locations) > 0:
            for j in locations:
                print(f'\nStorage ~{j.upper()}~ contents:')
                with open(fn.get_file_name(lines, j), 'r', encoding='utf-8') as file_r:
                    data = file_r.readlines()
                contains[j] = {i.split()[0]: i.split()[-2] for i in data[1:]}
                moving[j] = [i.strip() for i in data]
                units[j] = {i.split()[0]: i.split()[-1] for i in data[1:]}
                for x in data:
                    print(x[:-1])
        else:
            print('There is nothing to show!')
        with open(fl.bar, 'r', encoding='utf-8') as file_r:
            data = file_r.readlines()
        bar = {i.split()[0]: i.split()[1] for i in data[1:]}
        while True:
            ask = input('\nPress 0 to go back\nPress 1 to go next\nCOMMAND: ')
            if ask == '0':
                return
            elif ask == '1':
                break
        what = fn.choose(fn.get_dict(fl.bar), title='PRODUCT you want to move', new=False).split()[0]
        stock = [i for i in locations if what in contains[i].keys()]
        storage_from = {i: stock[i - 1] for i in range(1, len(stock) + 1)}
        from_ = fn.choose(storage_from, title='FROM where to move', new=False)
        while True:
            quantity = fn.get_float(name='Number of products', attachment='moving', unit='')
            if 0 <= quantity <= float(contains[from_][what]):
                break
            else:
                if quantity > 0:
                    print(f'Not enough {bar[what]} on {from_}. Maximum to move: {contains[from_][what]}')
                elif quantity < 0:
                    print('Enter positive integer!')
        locations.remove(from_)
        storage_to = {i: locations[i - 1] for i in range(1, len(locations) + 1)}
        to_ = fn.choose(storage_to, title='TO there to move', new=False)
        to_add_from = []
        to_add_to = []
        for i in moving[from_]:
            if i.split()[0] == what:
                to_add_from = [f'-{quantity}' if i.split().index(j) == 7 else j for j in i.split()]
                to_add_to = [f'{quantity}' if i.split().index(j) == 7 else j for j in i.split()]
        fn.update_line(fn.get_file_name(lines, from_), to_add_from, log=False)
        fn.update_line(fn.get_file_name(lines, to_), to_add_to, log=False)
        fn.update_log(action=f'MOVED ~{what}~ from ~{from_}~ to ~{to_}~ in quantity ~{quantity}~')
        print('MOVING COMPLETE')
