'''print('\n\t\tWelcome to products data base!\n\nLet me show you how to use it!')
while command != 'create':
    command = input('First of all, you have to create a new product! Type "create" in field "COMMAND"!\nCOMMAND: ')
    .lower()
num += 1
print('\nGreat! Now you have to complete product specification! Follow instructions:')
for i in specification.keys():
    if i == 'Price':
        while True:
            specification[i] = input('Enter a {} of a new product: '.format(i))
            if specification[i].isdigit():
                specification[i] = float(specification[i])
                break
    elif i == 'Quantity':
        while True:
            specification[i] = input('Enter a {} of a new product: '.format(i))
            if specification[i].isdigit():
                specification[i] = int(specification[i])
                break
    else:
        specification[i] = input('Enter a {} of a new product: '.format(i))
position = (num, specification)
dbase.append(position)
print('\nAwesome! New product has been added to data base! Now you have following products:\n', *dbase)
print('\nLet me teach you how to make changes in your data base!')
command = ''

while command != 'change':
    command = input('Type "change" in field "COMMAND"!\nCOMMAND: ').lower()

print('Now you have a following products:\n', dbase)
num_to_change = input('Enter an index number of product you want to make changes with: ')
check = 0
while check == 0:
    if num_to_change.isdigit():
        for i in dbase:
            for j in i:
                if j == int(num_to_change):
                    check += 1
                    command = input('\nThis is a chosen product specification: '
                                    '\n\t\t{}\nWhich attribute you\'d like to change?'
                                    '\nType name of attribute in field "COMMAND"\nCOMMAND: '.format(i[1])).title()
                    print(command)
                    while True:
                        if command in specification.keys():
                            if command == 'Quantity':
                                specification[command] = int(input('Enter a new value for attribute "{}": '.
                                                                   format(command)))
                            elif command == 'Price':
                                specification[command] = float(input('Enter a new value for attribute "{}": '.
                                                                     format(command)))
                            else:
                                specification[command] = input('Enter a new value for attribute "{}": '.
                                                               format(command))
                            print('\nUpdated info:\n\t\t{}'.format(specification))
                            break
                        else:
                            command = input('This attribute does not exist! Choose a different attribute!\n'
                                            'COMMAND: ').title()
                    break
                else:
                    num_to_change = input('Product with this index does not exist! Try different index!')
                    break
    else:
        num_to_change = input('This index should be an integer!')

print('\nPerfect! Now you know how to create products and how to make changes in data base.\nLet me show you how'
      'to delete products from data base!')
while command != 'delete':
    command = input('\nType "delete" in field "COMMAND"!\nCOMMAND: ').lower()

print('Now you have a following products:\n', dbase)
num_to_delete = input('Enter an index number of product you want to delete from data base: ')
check = 0
while check == 0:
    if num_to_delete.isdigit():
        for i in dbase:
            if int(num_to_delete) in i:
                check += 1
                while True:
                    final_req = input('Product {} will be deleted FOREVER. Confirm? (yes\\no) '.format(i[1])).\
                        lower()
                    if final_req == 'yes':
                        dbase.remove(i)
                        print('Product successfully deleted!\n', dbase)
                        break
                    elif final_req == 'no':
                        print('Nothing deleted.\nYour data base:\n{}'.format(dbase))
                        break
            else:
                num_to_delete = input('Product with this index does not exist! Try different index: ')
    else:
        num_to_delete = input('This index should be an integer: ')'''