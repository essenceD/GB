# I hope, it's done))
from Lesson_3.HW3_5 import get_num
with open('samples\\inputs\\text_6.txt', 'r', encoding='utf-8') as file_r:
    print({i.split()[0]: get_num(i) for i in file_r})

# get_num from lesson_3 is:
'''def get_num(sample):
    det = [j for j in sample]
    c, d, sign = '', [], 0
    for x in det:
        if x.isdigit():
            c += x
        else:
            if c.isdigit():
                if sample[sample.index(c) - 1] == '-':
                    d.append(-(int(c)))
                else:
                    d.append(int(c))
                c = ''
            else:
                continue
    if c.isdigit():
        if sample[sample.index(c) - 1] == '-':
            d.append(-(int(c)))
        else:
            d.append(int(c))
    return sum(d)'''