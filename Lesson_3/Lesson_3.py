def my_foo(s_1, s_2, s_3=7):
    # pass  # заглушка
    print('hi!')
    sub = s_1 + s_2 + s_3
    print('SUM: {}'.format(sub))
    return s_2 * s_3


# my_foo(4, 7)
print(my_foo(4, 3))


def ma_foo_2(*args):
    return args
print(ma_foo_2(4, 5, 'fgfdg', False))

def my_foo_1(**kwargs):
    return kwargs

print(my_foo_1(s_1=4, s_2=False))

my_f = lambda s_1, s_2: s_1 - s_2

print(my_f(45, 8))
print((lambda s_1, s_2: s_1 - s_2, (45, 8)))
print((lambda *args: args)(45, 8, False, 'PRIVET'))

print(ord('A'))
print(ord('Z'))
print(ord('F'))

print(chr(1237))
print(chr(888))
print(chr(221))

print(abs(-90))
print(round(4.6663))
print(round(6.4444, 2))
print(divmod(8, 5))
print(pow(2, 10))
print(max([1, 31, -5, 34]))
print(min([1, 31, -5, 34]))
print(sum([5, 33, -5, -33]))
print(list(range(0, 20, 2)))
print(set(range(0, 20, 2)))

def full_s_calc():
    global r_val, s_circle
    r_val = float(input('Radius: '))
    h_val = float(input('Hight: '))
    s_side = 2 * 3.14 * r_val * h_val
    s_circle = 2 * 3.14 * r_val * h_val
    s_full: float = s_side + 2 * s_circle
    return s_full

print(full_s_calc())
print(r_val, s_circle)

def ext_func():
    my_var = 10
    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var
    return int_func()

print(ext_func())

print(pow(2, -3))
