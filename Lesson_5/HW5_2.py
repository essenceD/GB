# 'Cause '/', '#', '*' etc are not words))
excl = ''
for i in range(33, 65):
    excl += chr(i)
with open('samples\\inputs\\text_2.txt', 'r', encoding='utf-8') as file:
    f = file.readlines()
    for i in f:
        if len(i) > 2:
            print(*i.split(), ' ->  "{} words"'.format(len([_ for _ in i.split() if _ not in excl])))
        else:
            print()
    print('\nFilled lines: {}\nTotal lines: {}'
          .format(len(f) - f.count('\n'), len(f)))


