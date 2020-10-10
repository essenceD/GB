import itertools as itt


def get_int(_start, _fin):
    res = []
    for i in itt.count(_start, 1):
        res.append(i)
        if i == _fin:
            return res


def set_clone(origin):
    '''clone = [i for i in origin]
    return clone'''
    clone = []
    for i in itt.cycle(origin):
        clone.append(i)
        if clone.index(i) == len(origin) - 1:
            return clone


while True:
    start = input('Start from: ')
    fin = input('Enter final: ')
    try:
        int(start)
        int(fin)
        break
    except ValueError:
        print('Not a number!')
a = get_int(int(start), int(fin))
print('All integer from {} to {} is: {}'.format(start, fin, a))
print('Cloned list is: ', set_clone(a))
