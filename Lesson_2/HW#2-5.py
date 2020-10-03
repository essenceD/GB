# initialization of first data set
while True:
    rate_data = input('Enter a start rating-data set!\nThis set must be positive integer values!\n').split()
    check = len(rate_data)
    for i in range(len(rate_data)):
        if rate_data[i].isdigit():
            rate_data[i] = int(rate_data[i])
            check -= 1
    if check == 0 and len(rate_data) > 0:
        break
print('\nStart rating-data set is: ', *rate_data)
sorted_rate = []
counter = len(rate_data)
# just to make an order like in a sample
while counter > 0:
    _max_rate = rate_data[0]
    for i in rate_data:
        if i > _max_rate:
            _max_rate = i
    sorted_rate.append(_max_rate)
    rate_data.remove(_max_rate)
    counter -= 1
print('Sorted data: ', *sorted_rate)
# add new data value and place it by order in list
while True:
    new_data = input('Type "exit" to leave this program or \nEnter a new rating value: ')
    if new_data == 'exit':
        print('Good Bye!\nLast data is: ', *sorted_rate)
        break
    if new_data.isdigit():
        new_data = int(new_data)
        if new_data in sorted_rate:
            sorted_rate.insert(sorted_rate.index(new_data), new_data)
            print('Modified data set is: ', *sorted_rate)
        elif new_data > sorted_rate[0]:
            sorted_rate.insert(0, new_data)
            print('Modified data set is: ', *sorted_rate)
        elif new_data < sorted_rate[-1]:
            sorted_rate.append(new_data)
            print('Modified data set is: ', *sorted_rate)
        else:
            for i in range(len(sorted_rate)):
                if new_data > sorted_rate[i]:
                    sorted_rate.insert(i, new_data)
                    break
            print('Modified data set is: ', *sorted_rate)
    else:
        print('This data should be an integer!')





