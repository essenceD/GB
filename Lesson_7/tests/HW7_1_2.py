class Matrix:
    def __init__(self, mtrx):
        if type(mtrx) is list:
            self.mtrx = mtrx
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

    def correct_view(self, *args):
        lane = [self.mtrx]
        rows = [len(self.mtrx)]
        for i in args:
            lane.append(i.mtrx)
            rows.append(len(i.mtrx))
        correct = []
        row = []
        max_row = max(rows)
        for i in range(max_row):
            if i == max_row // 2:
                for j in lane:
                    if lane.index(j) == len(lane) - 1:
                        row[-1] = '='
                        row.append(j[i])
                    else:
                        row.append(j[i])
                        row.append('+')
            else:
                for j in lane:
                    row.append(j[i])
                    row.append(' ')
            correct.append(row)
            row = []
        string = ''
        for i in correct:
            for j in range(2 * len(lane) - 1):
                string += str(i[j])
            string += '\n'
        return string.replace('[', ' ').replace(']', ' ').replace(',', ' ')


a = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
b = Matrix([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
c = Matrix([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
d = a + b + c
print(a + b + c)
print(Matrix.correct_view(a, b, c, d))


