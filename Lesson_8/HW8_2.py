class MyOwnErr(Exception):

    def __init__(self, txt):
        self.txt = txt


a, b = input("enter A and B to divide itself: ").split()
try:
    if int(b) == 0:
        raise MyOwnErr('NOOOOOOOOO!')
    print(int(a) / int(b))

except (ValueError, MyOwnErr, TypeError) as err:
    print(err)
else:
    print(int(b) / int(a))
finally:
    print('Thank you!')


