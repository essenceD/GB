from random import randint
my_list = [randint(0, 100) for i in range(10)]
print(my_list)
a = [my_list[i] for i in range(1, len(my_list)) if my_list[i] > my_list[i - 1]]
print(a)
