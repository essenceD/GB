import functools as ft
def multiplicate(cur, nex):
    return cur * nex


my_list = [i for i in range(100, 1000) if i % 2 == 0]
print(my_list)
print(ft.reduce(multiplicate, my_list))