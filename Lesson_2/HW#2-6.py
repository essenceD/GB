dbase, specification = [(1, {'Name': 'laptop', 'Price': 500.0, 'Quantity': 9, 'Units': 'pcs'}),
                        (2, {'Name': 'Cell Phone', 'Price': 200.0, 'Quantity': 13, 'Units': 'pcs'}),
                        (3, {'Name': 'Tv', 'Price': 900.0, 'Quantity': 4, 'Units': 'pcs'}),
                        (4, {'Name': 'PS 4 Pro', 'Price': 450.0, 'Quantity': 13, 'Units': 'pcs'}),
                        (5, {'Name': 'Sound Bar', 'Price': 450.0, 'Quantity': 9, 'Units': 'pcs'}),
                        (6, {'Name': 'Kettle', 'Price': 35.0, 'Quantity': 10, 'Units': 'pcs'}),
                        (7, {'Name': 'Vacuum', 'Price': 450.0, 'Quantity': 13, 'Units': 'pcs'}),
                        (8, {'Name': 'Printer', 'Price': 200.0, 'Quantity': 4, 'Units': 'pcs'}),
                        (9, {'Name': 'Fridge', 'Price': 900.0, 'Quantity': 4, 'Units': 'pcs'}),
                        (10, {'Name': 'Potatoes', 'Price': 7.0, 'Quantity': 1500, 'Units': 'kilos'})], \
                       {'Name': '', 'Price': 0, 'Quantity': 0, 'Units': ''}
count = 0
num = len(dbase)
#
while True:
    print('\n\tCommand list:\n1. Use "create" to create new product\n'
          '2. Use "change" to change any product\n'
          '3. Use "delete" to delete any product\n'
          '4. Use "find" to find any product\n'
          '5. Use "exit" to quit data base\n\n\t\t\t\t\t\t\tPRODUCTS\n')
    for i in dbase:
        print(*i)
    command = input('\n\t\tCOMMAND: ')
    if command.lower() == 'create':
        num = len(dbase) + 1
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
        print('\nNew product has been added to data base! Now you have following products:\n')
        for i in dbase:
            print(*i)

    elif command.lower() == 'change':
        product_in_db = False

        while True:
            num_to_change = input('\nEnter an index of product you want to make changes with: ')
            if num_to_change.isdigit():
                break
            else:
                print('This index should be an integer: ')

        for i in dbase:
            if int(num_to_change) in i:
                product_in_db = True
                print('\nThis is a chosen product specification: \n\t\t{}'.format((i[1])).title())

        while True:
            command = input('Enter an attribute you\'d like to change! (Name/Price/Quantity/Units)\n\t\tCOMMAND: ')\
                            .title()
            if command in specification.keys():
                break

        for i in dbase:
            if command in i[1].keys():
                if command.title() == 'Quantity':
                    i[1][command] = int(input('Enter a new value for attribute "{}": '.format(command.title())))
                elif command.title() == 'Price':
                    i[1][command] = float(input('Enter a new value for attribute "{}": '.format(command.title())))
                else:
                    i[1][command] = input('Enter a new value for attribute "{}": '.format(command.title()))
                print('\nUpdated info:\n\t\t{}'.format(i[1]))
                break

        if not product_in_db:
            print('Product with this index does not exist!')
            a = input('Press Enter!')

    elif command.lower() == 'delete':
        product_in_db = False
        while True:
            num_to_delete = input('Enter an index number of product you want to delete from data base: ')
            if num_to_delete.isdigit():
                break
            else:
                print('This index should be an integer: ')

        for i in dbase:
            if int(num_to_delete) in i:
                product_in_db = True
                while True:
                    final_req = input('Product {} will be deleted FOREVER. Confirm? (yes\\no) '.format(i[1])). \
                        lower()
                    if final_req == 'yes':
                        dbase.remove(i)
                        print('Product successfully deleted!')
                        a = input('Press Enter!')
                        break
                    elif final_req == 'no':
                        print('Nothing deleted!')
                        a = input('Press Enter!')
                        break
        if not product_in_db:
            print('Product with this index does not exist!')
            a = input('Press Enter!')

    elif command.lower() == 'find':
        while True:
            command = input('Enter an attribute to find products! (Name/Price/Quantity/Units)\n\t\tSearch by: ')

            if command.title() == 'Price':
                while True:
                    name_to_find = input('Enter a value for attribute "Price": ')
                    if name_to_find.isdigit():
                        name_to_find = float(int(name_to_find))
                        for i in dbase:
                            count += 1
                            if i[1]['Price'] == name_to_find:
                                print(*i)
                        break
                    else:
                        print('Price should be positive float!')
                break

            elif command.title() == 'Quantity':
                while True:
                    name_to_find = input('Enter a value for attribute "Quantity": ')
                    if name_to_find.isdigit():
                        name_to_find = int(name_to_find)
                        for i in dbase:
                            count += 1
                            if i[1]['Quantity'] == name_to_find:
                                print(*i)
                        break
                    else:
                        print('Quantity should be positive integer!')

            elif command.title() == 'Name' or command.title() == 'Units':
                name_to_find = input('Enter a value for attribute "{}": '.format(command.title()))
                for i in dbase:
                    count += 1
                    if name_to_find in i[1].values():
                        print(*i)
                    '''if count == len(dbase) - 1:
                        break'''
                a = input('Press any key')
                break
            else:
                print('Wrong attribute!')

    elif command.lower() == 'exit':
        print('\n\t\t\t\t***********GOOD BYE!***********')
        break
