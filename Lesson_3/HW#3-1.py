''' To divide "a" by "b" '''


def foo(var_1, var_2):
    try:
        res = round(var_1 / var_2, 3)
    except ZeroDivisionError:
        res = 'I can\'t divide by zero((('
    return res


while True:
    try:
        a = float(input('Enter the dividend: '))
        b = float(input('Enter the divider: '))
        break
    except ValueError:
        print('Dividend and divider supposed to be numeric!')
print(foo(a, b))


