def get_fact(base):
    res = 1
    for i in range(1, base + 1, 1):
        res *= i
    return res


def list_gen():
    for i in range(1, fin + 1):
        yield i


while True:
    fin = input('Enter length of list: ')
    try:
        fin = int(fin)
        if fin > 0:
            break
        else:
            print('Positive numbers only!')
    except ValueError:
        print('Not a number!')

my_list = [get_fact(i) for i in list_gen()]
print('List with factorials up to {} is {}:'.format(fin, my_list))
