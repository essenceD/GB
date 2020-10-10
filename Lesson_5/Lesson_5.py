from random import randint
print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1])
