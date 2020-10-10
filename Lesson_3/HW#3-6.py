# To set correct size of first letter in each word of phrase
def set_words(sample):
    new_words = [t for t in sample.split()]
    for j in range(len(new_words)):
        if stop in new_words[j]:
            new_words[j] = new_words[j][:new_words[j].index(stop)].title()
            return new_words[:j + 1]
        new_words[j] = new_words[j].title()
    return new_words


# To check the entered text for compliance with the task
def check_phrase(sample):
    if len(sample) == 0:
        return True
    elif len(sample) == sample.count(' '):
        return True
    for x in sample:
        if x not in base:
            return True
    return False


stop, words = input('Enter a stop-symbol: '), ''
repeat, base = True, ' ' + stop
for i in range(97, 123):
    base += chr(i)
while True:
    while repeat:
        words = input('Enter only latin in lower case: ')
        repeat = check_phrase(words)
    if stop in words:
        print('\tStop-symbol "{}" has been entered'.format(stop))
        print('Correct phrase is: ', *set_words(words[:words.index(stop)]))
        print('**********GOOD BYE!**********')
        break
    else:
        print('Correct Phrase is: ', *set_words(words))
        repeat = True
