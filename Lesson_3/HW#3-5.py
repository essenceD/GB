''' To get nums from each word '''


def get_num(sample):
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
    return sum(d)


stop, full_sum, check = input('Enter stop-symbol: ').strip(), 0, 0
while True:
    a, sub_sum = input('Enter numbers separated with space bar: ').split(), 0
    for i in a:
        if stop in i:
            sub_sum += get_num(i[:-1])
            check += 1
            break
        sub_sum += get_num(i)
    full_sum += sub_sum
    if check > 0:
        print('Partial Sum is:{}\tFull Sum is:{}\n'.format(sub_sum, full_sum))
        print('**********GOOD BYE!**********')
        break
    print('Partial Sum is:{}\tFull Sum is:{}\n'.format(sub_sum, full_sum))
