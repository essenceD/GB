''' BE CAREFUL, Sarah! This func could activate T-1000 '''


def my_func(var_1, var_2, var_3):
    to_calc = [var_1, var_2, var_3]
    to_calc.remove(min(to_calc))
    return sum(to_calc)


print(my_func(7, 2, 3))
