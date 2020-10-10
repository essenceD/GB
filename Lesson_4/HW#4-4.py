from random import randint
print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1])

'''my_list = [randint(0, 9) for i in range(20)]
print([i for i in my_list if my_list.count(i) == 1])'''

