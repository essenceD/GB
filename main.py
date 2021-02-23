import Product as Pr
import Warehouse as Wh
import funcs as fn
from datetime import datetime as dt


storage = Wh.Warehouse()
fn.update_log(action=f'----{dt.today().strftime("%d.%m.%Y")}----Database launched.--------')
while True:
    print('\n\t\t********** MAIN MENU **********')
    com = input('Press 1 to SHOW\n'
                'Press 2 to CREATE\n'
                'Press 3 to ADD new product\n'
                'Press 4 to MOVE\n'
                'Press 5 to DO\n'
                'Press 6 to EXIT DataBase\n'
                'COMMAND: ')
    try:
        isinstance(com, int)
    except ValueError:
        print('Choose something by pressing similar button!')
    else:
        if int(com) == 1:
            storage.show()
        elif int(com) == 2:
            storage.create()
        elif int(com) == 3:
            while True:
                ask = input('Press 0 to go back\nPress 1 to go next\nCOMMAND: ')
                if ask == '0':
                    break
                elif ask == '1':
                    new_prod = Pr.Product()
                    break
        elif int(com) == 4:
            storage.move_prod()
        elif int(com) == 5:
            print('DONE!')
        elif int(com) == 6:
            print('\t\t********** GOOD BYE! **********')
            break
        else:
            print('Choose something by pressing similar button!')
