to_write, res = '', 0
with open('samples\\inputs\\text_5.txt', 'w', encoding='utf-8') as file_w:
    while True:
        string = input('Enter numbers separated with the space bar or "quit" to exit: \n')
        if 'quit' in string:
            break
        to_write += string + '\n'
        res += sum([int(_) for _ in string.split() if _.isdigit()])
    file_w.writelines(to_write)
print('Sum: {}'.format(res))



