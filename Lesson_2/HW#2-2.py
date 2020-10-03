while True:
    size = input('Enter a size of list: ')
    if size.isdigit() and int(size) > 0:
        size = int(size)
        break
lst = input('Enter elements separated by space bar: ').split()
print('The list you\'ve input:  ', *lst)
for i in range(0, size, 2):
    lst.insert(i + 1, lst.pop(i))
print('Modified list is: \t\t', *lst)