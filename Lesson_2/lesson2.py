string = '123456789abcdefghijklmnopqrstuvwxyz'
print(string[0:5:1])
print(string[:13:2])
print(string[::-1])
print(string[::2])
print(string[:6][:2])

lst = string.split()
print(lst)

a = ['name', 'surname']
print(a)
print(' '.join(a))

a = 'gEorgE'
print(a.title())
print(a.upper())
print(a.lower())
print(a.count('g'))

a = 'hypopothampo'
print(a)
print(a.replace('po', 'PO'))
print(a.index('po', 5))

a = list(a)
print(a)
a = [12, 44.55, 'str', False, [1, 2]]
print(a)
a[0] = 121212
print(a)
print(len(a))
print(a[4][0])
a.append('new')
print(a)
a.insert(1, True)
print(a)
b = ['q', 'w', 'e']
print(a + b)
print(a.pop())
print(b + a.pop())
print(a)
a.remove(True)
print(a)
a.append(22)
a.append(22)
a.append(22)
a.append(22)

a = tuple(a)
print(a)
a = (12, 44.55, 'str', False, 33, 33, 33, 33)
print(a)


a = set(a)
print(a)

a = {1: 11, 2: 22}

for i in 'abcdef':
    print(i)

for i in range(len('abcdefg')):
    print(i)
a = ['a', 'e', 'f']
for i, j in enumerate(a):
    print(i, j)

