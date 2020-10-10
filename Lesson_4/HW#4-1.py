from sys import argv

name, hours, rate = argv
try:
    salary = int(hours) * int(rate)
except ValueError:
    salary = 'Wrong data entered!'
print(salary)
