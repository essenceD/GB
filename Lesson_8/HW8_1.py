class Date:

    def __str__(self):
        return str(self.date)

    def __init__(self, date):
        self.date = date

    @classmethod
    def deg_num(cls, date):
        return list(map(lambda i: int(i), date.split('-')))

    @staticmethod
    def valid_num(date):
        dd, mm, yyyy = date
        limits = {'31': [1, 3, 5, 7, 8, 10, 12], '30': [4, 6, 9, 11], '28': [2], '29': [2]}
        for i in limits.keys():
            if mm in limits[i]:
                if 0 < dd <= int(i):
                    return 'Correct date'
        return 'Invalid date'


date_1 = '27-05-1703'
date_2 = '31-02-2032'
date_3 = '12-16-2000'
a = Date(date_1)
print(a, type(a.date))
b = Date(date_2)
print(b, type(b.date))
c = Date(date_3)
print(c, type(c.date))
d = Date.deg_num(a.date)
print(*d, type(d))
e = Date.deg_num(b.date)
print(*e, type(e))
f = Date.deg_num(c.date)
print(*f, type(f))
g = Date.valid_num(d)
print(g, type(g))
h = Date.valid_num(e)
print(h, type(h))
j = Date.valid_num(f)
print(j, type(j))







