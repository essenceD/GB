# Для дочки чтобы учить табличку умножения

from random import randint as rd
import os

lives = 3
cnt = 0
level = 4
hist = []
os.system('CLS')
points = 0

while True:
    os.system('CLS')
    _max = input('\n' * 10 + '\t' * 2 + 'До какого числа проверяем таблицу умножения?\n\n' + '\t' * 4 + 'Максимум: ')
    try:
        _max = int(_max)
    except ValueError:
        os.system('CLS')
        print('\n' * 10 + '\t' * 3 + 'Такого числа не существует!')
    else:
        os.system('CLS')
        print('\n' * 10 + '\t' * 4 + 'Хорошо. Начинаем!\n')
        _max = int(_max)
        break
tasks = int(_max) * level
print(f'  У тебя есть 3 жизни и {tasks} примеров, чтобы проверить знания по умножению до {_max}!\n')
cont = input('\t' * 3 + 'Нажми ENTER для продолжения!')
os.system('CLS')
ans = ''
mark = 5.0
ans_cost = 0.4
while tasks > 0:
    if ans == 'quit':
        break
    a = rd(2, _max)
    b = rd(2, 10)
    hist.append(f'{a}x{b}')
    if cnt > 0:
        if hist.count(f'{a}x{b}') > 1:
            continue
    cnt += 1
    while True:
        ans = input('\n' * 8 + '\t' * 3 + f'Жизни: {lives} || Примеры: {tasks} || Очки: {points}\n\n' + '\t' * 3 +
                    f'Пример {cnt}:\n\n' + '\t' * 3 + f'{a} x {b} = ')
        if ans == 'quit':
            os.system('CLS')
            print('GOOD BYE!')
            points = 0
            break
        elif ans == 'restart':
            os.system('CLS')
            print('\n' * 10 + '\t\t\tНачнем сначала...\n\n')
            cont = input('\t' * 3 + 'Нажми ENTER для продолжения...')
            points = 0
            os.system('CLS')
            tasks = int(_max) * level
            lives = 3
            cnt = 0
            hist = []
            mark = 5.0
            ans_cost = 0.4
            break
        try:
            ans = int(ans)
        except ValueError:
            os.system('CLS')
            print('\n' * 10 + '\t' * 3 + 'Нужно напечатать число!\n')
            cont = input('\t' * 3 + 'Нажми ENTER для продолжения!')
            os.system('CLS')
        else:
            if int(ans) == a * b:
                tasks -= 1
                print('\n' + '\t' * 3 + f'Правильно! Осталось примеров: {tasks}\n')
                cont = input('\t' * 3 + 'Нажми ENTER для продолжения!')
                points += 5
                os.system('CLS')
                break
            elif int(ans) != a * b and lives > 0:
                lives -= 1
                print('\n' + '\t' * 2 + f'Это неправильный ответ! Правильный ответ: {a * b}\n')
                hist.pop()
                cont = input('\t' * 3 + 'Нажми ENTER для продолжения!')
                points -= 6
                os.system('CLS')
                mark -= ans_cost
                break
            elif int(ans) != a * b and lives == 0:
                tasks += 3
                print('\n' + '\t' * 2 + f'Это неправильный ответ! Правильный ответ: '
                                  f'{a * b}\n\n\t\tПолучаешь 3 дополнительных примера! >:-)=\n')
                hist.pop()
                cont = input('\t' * 3 + 'Нажми ENTER для продолжения!')
                points -= 16
                os.system('CLS')
                mark -= ans_cost
                break
    if tasks == 0:
        os.system('CLS')
        if mark > 3.5:
            print('\n' * 10 +
                  '\t\tМолодец! Позови папу или маму, \n\n\t\t'
                  'чтобы они увидели выполненное задание и вернули планшет >:>\n\n\t\t'
                  f'Твоя оценка: {int(mark)}')
            cont = input('\n' * 2 + '\t' * 2 + 'Нажми ENTER для выхода из программы!')
            os.system('CLS')
        else:
            print('\n' * 10 +
                  '\t\tМолодец! Ты решила все примеры, \n\n\t\tно сделала очень много ошибок!'
                  '\n\n\t\tНачни сначала и будь внимательнее!'
                  f'Твоя оценка {int(mark)}')
            cont = input('\n' * 2 + '\t' * 2 + 'Нажми ENTER для пересдачи!')
            os.system('CLS')
            tasks = int(_max) * level
            cnt = 0
            points = 0
            lives = 3
            hist = []
            mark = 5.0
            ans_cost = 0.4
