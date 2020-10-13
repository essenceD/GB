file = open('test01.txt', 'r', encoding='utf-8')
print('1')
content = file.read()
print(content)
file.close()
file = open('test01.txt', 'r', encoding='utf-8')
print('2')
content_2 = file.readline()
print(content_2)
file.close()
file = open('test01.txt', 'r', encoding='utf-8')
print('3')
content_3 = file.readlines()
print(content_3)
file.close()
file = open('test01.txt', 'r', encoding='utf-8')
print('4')
content_4 = file.read(15)
print(content_4)
file.close()
file = open('test01.txt', 'r', encoding='utf-8')
print('5')
content_5 = file.readline(2)
print(content_5)
file.close()
file = open('test01.txt', 'r', encoding='utf-8')
print('6')
content_6 = file.readlines(2)
print(content_6)
file.close()

file = open('test02.txt', 'w', encoding='utf-8') # 'w' полностью очищает файл перед записью
print('7')
content_7 = file.write(f'FUCK YOU!\n{[1, 2, 3, 4]}\n{1, 2, 3, 4, 5, 6}')
file.close()

with open('test03.txt', 'w', encoding='utf-8') as file:
    file.writelines(['{1, 2, 3, 4, 5}'])

with open('test02.txt', 'x+', encoding='utf-8') as file:
    file.writelines('{1, 2, 3, 4, 5}')

with open('test02.txt', 'w+', encoding='utf-8') as file:
    file.seek(0)
    print(file.read())


with open('test04.txt', 'r', encoding='utf-8') as file:
    file.seek(2)
    print(file.read())

with open('test04.txt', 'r', encoding='utf-8') as file:
    file.seek(4)
    print(file.tell())

with open('test04.txt', 'a', encoding='utf-8') as file:
    print('allright...', file=file)

import os
#os.remove('test05.txt')
#os.rename('test03.txt', 'test06.txt')
#print(os.listdir())

import json
data = {
    'income': {
        'salary': 50000,
        'bonus': 20000
    }
}
with open('my_json', 'w', encoding='utf-8') as file:
    json.dump(data, file)
js = json.dumps(data)
print(js)
print(type(js))









