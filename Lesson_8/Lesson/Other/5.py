# make exclusion
class MyOwnErr(Exception):
    def __init__(self, txt):
        self.txt = txt


in_data = input("enter value")
try:
    in_data = int(in_data)
    if in_data < 0:
        raise MyOwnErr('Only positive!')
except (ValueError, MyOwnErr) as err:
    print(err)
else:
    print(in_data)
finally:
    print('The End!')


