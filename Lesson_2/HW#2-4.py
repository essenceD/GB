num, string = 0, input('\tEnter a few words separated with space bar: ').strip()
while string.count(' ') == 0 and len(string) == 0:
    string = input('Your phrase has to content at least one space bar and one symbol!\n\tTry again: ').strip()
print('Success!\nThe sentence "{}"\nIncludes the following words:'.format(string))
for i in string:
    if i == ' ':
        num += 1
        print('{:0=2}. {:.10}'.format(num, string[:string.index(i)]))
        string = string[string.index(i):].strip()
        if string.count(' ') == 0:
            break
print('{:0=2}. {:.10}'.format(num + 1, string))
