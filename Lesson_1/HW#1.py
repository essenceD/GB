a, b, c, d, e = 123, 1.23, 'one-twenty three', True, input('What is your name?\t')
while True:
    f = input(f'How old are you, {e}? \t')
    if f.isdigit():
        int(f)
        print('\nTake a look:\n')
        break
    else:
        print('NOTICE: Your age should be INTEGER')
print(f'This is INT: {a};\nThis is FLOAT: {b};\nThis is STRING: {c};\nThis is BOOL: {d};\nThat\'s your name: {e};'
      f'\nThat\'s your age: {f}')
