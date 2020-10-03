# solution over the dictionary

while True:
    month_number = input('Enter the month number (from 1 to 12): ')
    if month_number.isdigit() and 13 > int(month_number) > 0:
        month_number = int(month_number)
        break
seasons = {'Winter': [1, 2, 12], 'Spring': [3, 4, 5], 'Summer': [6, 7, 8], 'Autumn': [9, 10, 11]}
months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}
for i, j in seasons.items():
    if int(month_number) in j:
        print('The month number {} is {} and it is a {}!'.format(int(month_number), months[month_number], i))
