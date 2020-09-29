procs, costs = int(input('Enter a proceeds of your company: ')), int(input('Enter a costs of your company: '))
if procs > costs:
    print('\nGood news! Your company is profitable!\n\nYour company\'s profit is: {}\nYour company\'s profitability is {}'
          .format(procs - costs, (procs - costs) / procs))
    employee = int(input('Enter a number of employees: '))
    print('Ypur company\'s profit per employee is {}'.format((procs - costs) / employee))
else:
    print('\nUnfortunately, your company is unprofitable! Find yourself in a different business!')