while True:
    time = input('Enter amount of time in seconds: ')
    if time.isdigit():
        if int(time) > 315359999999:
            print('C\'mon, man! That is too much! Try a smaller number!\n')
            continue
        elif int(time) > 359999:
            print('\nIn our dimension we use this time format:\nyear:ddd:hh:mm:ss\n%.04d:%.03d:%.02d:%.02d:%.02d' %
                  (int(time) // 31536000,
                   int(time) % 31536000 // 86400,
                   int(time) % 86400 // 3600,
                   int(time) % 3600 // 60,
                   int(time) % 60))
            break
        print('\nIn our dimension we use this time format:\nhh:mm:ss\n%.02d:%.02d:%.02d' %
              (int(time) // 3600,
               int(time) % 3600 // 60,
               int(time) % 60))
        break
    else:
        print('Amount of time should be a positive number!')
