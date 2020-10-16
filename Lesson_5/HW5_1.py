# To my mind, it is bad idea to reopen file for multiple times
# But if you have at least couple files, this func would be useful
'''def update_file(_name, _text):
    with open(_name, 'a', encoding='utf-8') as _file:
        _file.writelines(_text)'''


# To make testing easier, in these case user has to enter an existing file address only.
# If you don't like it - tell me about and I'll make changes.
while True:
    name = input('Enter a file address. Default is: samples\\outputs\\file-1.txt\nAddress: ')
    try:
        file = open(name, 'r', encoding='utf-8')
        file.close()
        break
    except FileNotFoundError as error:
        print(error)
with open(name, 'a', encoding='utf-8') as file:
    while True:
        text = input('Enter a message to next line in "{}"!\nLeave it blank to quit.\nText: '.format(name))
        text += '\n'
        if len(text.strip()) == 0:
            break
        else:
            file.writelines(text)
with open(name, 'r', encoding='utf-8') as file:
    print('Final update is: \n{}\n**********GOOD BYE!**********'.format(file.read()))



