lst = [1, 2.2, 'python', [3, ('First', 'Second')], (True, 4), {'a': 'accelerate', 'b': 14}, False]
for i in lst:
    print('Value {} has a type of {}'.format(i, type(i)))