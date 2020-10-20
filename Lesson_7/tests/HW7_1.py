class Matrix:
    def __init__(self, mtrx):
        if type(mtrx) is list :
            print(f'Matrix has been defined!')
            for i in mtrx:
                print(*i)
            self.mtrx = mtrx
            print()
        else:
            print('You have entered wrong data!')
            del(self, mtrx)

    def __str__(self):
        try:
            return '\n'.join(['\t'.join([str(i) for i in j]) for j in self.mtrx])
        except AttributeError:
            return 'Not a matrix'

    def __add__(self, other):
        res = []
        string = []
        for i in range(len(self.mtrx)):
            res.append(string)
            for j in range(i):
                string.append(self.mtrx[i][j] + other.mtrx[i][j])
        return Matrix(res)

    def correct_view(self):
        pass


a = Matrix([[1, 1, 1],
            [1, 1, 1],
            [1, 1, 1]])
b = Matrix([[4, 4, 4],
            [4, 4, 4],
            [4, 4, 4]])
c = Matrix([[5, 5, 5],
            [5, 5, 5],
            [5, 5, 5]])
d = a + b + c
rest = f'{a} \n\t+ \n{b} \n\t+ \n{c} \n\t=\n{d}'
print(rest)





