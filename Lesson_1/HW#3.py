while True:
    num = input('Enter the N number to calculate "N + NN + NNN": ')
    if num.isdigit():
        print('Result is: ', int(num) + int(num * 2) + int(num * 3))
        break
    else:
        print('N should be a positive number!')