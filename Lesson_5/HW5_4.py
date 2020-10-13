rus, translate = {'1': 'Один', '2': 'Два', '3': 'Три', '4': 'Четыре', '5': 'Пять',
                  '6': 'Шесть', '7': 'Семь', '8': 'Восемь', '9': 'Девять', '0': 'Ноль'}, []
with open('samples\\inputs\\text_4.txt', 'r', encoding='utf-8') as file_r:
    for i in file_r:
        translate.append(rus[i.split()[len(i.split()) - 1]] + ' ' + i[i.index(i.split()[len(i.split()) - 1]) - 2:])
        print(i, end='')
with open('samples\\outputs\\file-4.txt', 'w', encoding='utf-8') as file_w:
    file_w.writelines(translate)


