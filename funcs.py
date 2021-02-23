import files as fl
import os
import Product as Pr
import Warehouse as Wh
from datetime import datetime as dt


# ------------------------------------------------- CHOOSE_* FUNCS -----------------------------------------------------
''' Implementation of choosing procedure. Expected dictionary with choose options, title is a choosing subject,
switch parameter "new" to False if you don\'t need user could create a new parameter.
LOG UPDATED'''


def choose(dict_, title='One of these', new=True):
    if len(dict_) > 0:
        if new:
            print(f'Choose the {title}:\n')
            for i, j in dict_.items():
                print(f'Choose {i} to set ~{j.upper()}~')
            while True:
                try:
                    choice = int(input('Or type 0 to create new...\nYour choice: '))
                except ValueError:
                    print('Enter a number, please!')
                else:
                    if choice in dict_.keys():
                        return dict_[choice]
                    elif int(choice) == 0:
                        choice = input(f'Enter new {title}: ')
                        eval(f'update_{title}("{choice}")')
                        return choice
        else:
            print(f'Choose the {title}:\n')
            for i, j in dict_.items():
                print(f'Choose {i} to set ~{j.upper()}~')
            while True:
                try:
                    choice = int(input('\nYour choice: '))
                except ValueError:
                    print('Enter a number, please!')
                else:
                    if int(choice) > 0 and choice in dict_.keys():
                        return dict_[choice]
                    else:
                        print('Choose a number from proposed!')
    else:
        return '__empty__'

# ------------------------------------------------- UPDATE_* FUNCS -----------------------------------------------------


''' It writes new product\'s categories into categories.txt. It is necessary to add new Product examples in future.'''


def update_categories(new_data):
    with open(fl.cat, 'r', encoding='utf-8') as file_r:
        data = file_r.readlines()
    if new_data in data:
        print(f'Unable to create new category. Category {new_data} already exists.')
    elif len(data) == 0:
        with open(fl.cat, 'a', encoding='utf-8') as file_a:
            print(new_data, file=file_a)
        update_log(action=f'UPDATED file categories.txt. New value: ~{new_data}~')
    else:
        with open(fl.cat, 'a', encoding='utf-8') as file_a:
            print(new_data, file=file_a)
    update_log(action=f'UPDATED file categories.txt. New value: ~{new_data}~')


''' It adds new storages to storage-list and creates new storage file in \\lines folder by sample.txt
LOG UPDATED'''


def update_lines(name):
    with open(fl.lines, 'r', encoding='utf-8') as file_r:
        data = file_r.readlines()
    storages = [i.split()[0] for i in data]
    if name not in storages:
        with open(fl.lines, 'a', encoding='utf-8') as file_a:
            print(name, file=file_a)
        create_file(Pr.lines, name, Wh.sample_line)
        update_log(action=f'CREATED. New storage ~{name}~ successfully created')
    else:
        print(f'Storage {name} already exists!')


''' It adds new products to matching storage or increase quantity if product was added before.
LOG UPDATED'''


def update_line(line, to_add, log=True):
    with open(line, 'r', encoding='utf-8') as file_r:
        data = file_r.readlines()
    to_write = ''
    clone = ''
    for i in to_add:
        clone += i + ' '
    clone += '\n'
    jump = False
    match = False
    for i in data:
        acc = i
        res = i.split()[0]
        if str(to_add[0]) == res:
            match = True
            new_str = ''
            rew = ''
            for j in i.split():
                if i.split().index(j) == 7:
                    jump = True
                    rew = str(float(j) + float(to_add[7])) + ' '
                if jump:
                    new_str += rew
                    jump = False
                else:
                    new_str += to_add[i.split().index(j)] + ' '
            acc = new_str + '\n'
        to_write += acc
    if not match:
        to_write += clone
    with open(line, 'w', encoding='utf-8') as file_w:
        print(to_write[:-1], file=file_w)
    if log:
        update_log(action=f'UPDATED. Line ~{line}~ updated. ~{to_add}~ added successfully.')


''' It adds new unique bar-codes to data\\bars.txt '''


def update_bars(bar):
    with open(fl.bar, 'a', encoding='utf-8') as file_a:
        print(bar, file=file_a)


''' It updates cross-files information. Adds only unique values.
LOG UPDATED '''


def update_index(bar, name='file_name', type_='product_type', folder='base'):
    with open(fl.index, 'r', encoding='utf-8') as file_r:
        data = file_r.readlines()
    exist_bars = []
    for i in data:
        exist_bars.append(i.split()[0])
    if bar not in exist_bars:
        with open(fl.index, 'a', encoding='utf-8') as file_a:
            print(f'{bar} {type_} {get_file_name(folder, name)}', file=file_a)
        update_log(action=f'UPDATED INDEX. Product ~{type_}~ ~{name}~.')


''' It records every procedure to LOG file. '''


def update_log(action='Default action completed...'):
    with open(fl.log, 'r', encoding='utf-8') as file_r:
        order = str(int(file_r.readlines()[-1].split()[0]) + 1)
    with open(fl.log, 'a', encoding='utf-8') as file_a:
        print(f'{order} {action} DATE:{dt.today().strftime("%d.%m.%Y  TIME: %H:%M:%S")}', file=file_a)


''' It adds product info to product_name.txt file in base folder. 
LOG UPDATED '''


def update_prod(params_dict, file_name='Product_address'):
    sample = ['bar',
              'type',
              'brand',
              'model',
              'p_price',
              'r_price',
              'specs']
    res, to_write = '', ''
    with open(file_name, 'r', encoding='utf-8') as file_r:
        file = file_r.readlines()
    if len(file) > 1:
        for i in file:
            res = i[0]
            if i.split()[0] in params_dict.keys():
                res = f'{i.split()[0]} {params_dict[i.split()[0]]}\n'
            to_write += res
        with open(file_name, 'w', encoding='utf-8') as file_w:
            print(to_write[:-1], file=file_w)
        update_log(action=f'UPDATED. Product ~{file_name}~ has been updated: ~{params_dict}~')
    else:
        for i in sample:
            to_write += f'{i} {params_dict[i]}\n'
        with open(file_name, 'w', encoding='utf-8') as file_w:
            print(to_write[:-1], file=file_w)
        update_log(action=f'UPDATED. Product ~{file_name}~ has been updated: ~{params_dict}~')


# ----------------------------------------------- GET_* FUNCS ----------------------------------------------------------
''' It gets float number '''


def get_float(name='Parameter', attachment='ClassName', unit='Regular Brand'):
    while True:
        try:
            new_data = float(input(f'Enter {name} for {attachment} {unit}: '))
        except ValueError:
            print(f'{name}" Should be a number!')
        else:
            if new_data > 0:
                return new_data
            else:
                print(f'{name}" Should be positive!')


''' It assembles full file name to open it automatically '''


def get_file_name(folder, name):
    return f'{folder}\\{name}.txt'


''' It gets dictionary from files with 1 column '''


def get_dict(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_r:
        data = file_r.readlines()
    counter = 0
    new_dict = {}
    for i in data:
        new_dict[counter] = i.strip()
        counter += 1
    return {i: new_dict[i] for i in new_dict if i != 0}


''' It gets dictionary from files with 2 columns '''


def get_dict_2(file_name):
    with open(file_name, 'r', encoding='utf-8') as file_r:
        new_dict = {}
        for i in file_r.readlines():
            new_dict[i.split()[1]] = i.split()[0]
        return new_dict


# ----------------------------------------------- CREATE_* FUNCS -------------------------------------------------------
''' It creates new file with NAME in FOLDER from SAMPLE 
LOG UPDATED'''


def create_file(folder, name, sample_adr):
    if not os.path.isfile(get_file_name(folder, name)):
        with open(sample_adr, 'r', encoding='utf-8') as file_r:
            data = file_r.readlines()
        sample = ''
        for i in data:
            sample += i + ' '
        with open(get_file_name(folder, name), 'w', encoding='utf-8') as file_w:
            print(sample[:-1], file=file_w)
        update_log(action=f'CREATED File ~{get_file_name(folder, name)}~ successfully.')
    else:
        update_log(action=f'CREATE FAIL. Unable to create file ~{get_file_name(folder, name)}~. File already exists.')
