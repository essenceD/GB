# import time
# from time import sleep, wake, run
# import time as t
# from math import *   no good!
import math as m
import test as n

n.sh_ms()
#print(n.sm_c())

print(m.sqrt(121))
print(m.pi)

# запуск скрипта с параметрами
# делается через cmd
'''from sys import argv

print(argv)

name, s1, s2, s3 = argv
print(s1)
print(s2)
print(s3)'''

#GENERATORS
my_list = [1, 2, 3, 4, 5, 6]
print(my_list)
new_list = [i + 20 if i % 2 == 0 else i + 10 for i in my_list]
print(new_list)
new_set = {i * 2 for i in range(7)}
print(new_set)
new_dict = {i: i * 5 for i in range(10)}
print(new_dict)
new_tuple = tuple(i for i in range(5))
print(new_tuple)
for i in my_list:
    print(i, end=' ')
print()

# random()
from random import randint
print(randint(1, 20))
from random import randrange
print(randrange(7, 20, 3))

# yield
def gen():
    for i in [1, 2, 3]:
        yield i
print(gen())

# functools
import functools as ft
def foo(prev, el):
    return prev + el


print(ft.reduce(foo, [1, 2, 3, 4, 5]))
print(list(map(int, ['1', '2', '3', '4', '5'])))

import itertools as itt
for i in itt.count(7, 10):
    print(i, end=' ')
    if i > 15:
        break
print()
from itertools import cycle
c = 0
for i in cycle(['ADC', 34, False, [1, 2]]):
    if c > 10:
        break
    print(i, end=' ')
    c += 1