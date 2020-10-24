from Lesson_8.Source import HW8_classes as Src


storage = Src.Warehouse()
while True:
    print('\t\t********** MAIN MENU **********')
    com = input('Press 1 to SHOW DataBase\n'
                'Press 2 to ADD new product\n'
                'Press 3 to MOVE product\n'
                'Press 4 to EXIT DataBase\n'
                'COMMAND: ')
    try:
        int(com) + 1
    except ValueError:
        print('Choose something by pressing similar button!')
    else:
        if int(com) == 1:
            storage.show()
        elif int(com) == 2:
            storage.add_prod()
        elif int(com) == 3:
            storage.move_prod()
        elif int(com) == 4:
            print('\t\t********** GOOD BYE! **********')
            break
        else:
            print('Choose something by pressing similar button!')






