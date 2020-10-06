''' To calculate "b" to the power of "a" '''


def my_func(base, exponent):
    res = 1
    if exponent >= 0:
        for i in range(exponent):
            res *= base
        return res
    else:
        for i in range(abs(exponent)):
            res *= base
        return '1/{}'.format(res)


''' To initiate data. Use "pos" to get POSITIVE number oe "neg" to get NEGATIVE '''


def get_data(name, sig='all', d_type='int'):
    loc_name = str(name)
    new_data = ''
    while True:
        try:
            if d_type == 'int':
                new_data = int(round(float(input('Enter {} value or 666 to exit: '.format(loc_name)))))
                if new_data == 666:
                    new_data = 'Good Bye!'
                    return new_data
                else:
                    if sig == 'pos':
                        if new_data < 0:
                            return -new_data
                        else:
                            return new_data
                    if sig == 'neg':
                        if new_data > 0:
                            return -new_data
                        else:
                            return new_data
                    return new_data
            elif d_type == 'float':
                new_data = float(input('Enter {} value or 666 to exit: '.format(loc_name)))
                if int(new_data) == 666:
                    new_data = 'Good Bye!'
                    return new_data
                else:
                    if sig == 'pos':
                        if new_data < 0:
                            return -new_data
                        else:
                            return new_data
                    if sig == 'neg':
                        if new_data > 0:
                            return -new_data
                        else:
                            return new_data
                    return new_data
        except ValueError:
            continue
    return new_data


''' "a" is positive float always and "b" is negative int always '''
while True:
    a = get_data('Base', d_type='float', sig='pos')
    if a == 'Good Bye!':
        print(a)
        break
    b = get_data('Exponent', sig='neg')
    if b == 'Good Bye!':
        print(b)
        break
    print('{} to the power of {} is equals: {}\n'.format(a, b, my_func(a, b)))
