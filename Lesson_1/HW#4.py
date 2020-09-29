while True:
    num = input('Enter an integer and I\'ll tell you a largest digit in it: ')
    if num.isdigit():
        num = int(num)
        Max = num % 10
        while num // 10 > 0:
            num = num // 10
            if num % 10 > Max:
                Max = num % 10
        break
print('Answer:', Max)