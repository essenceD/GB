from sys import argv

name, hours, rate = argv
try:
    salary = int(hours) * int(rate) # ARGV возвращает список.
except ValueError:
    salary = 'Wrong data entered!'
print(salary)
