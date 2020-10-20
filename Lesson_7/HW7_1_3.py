class Matrix:
    def __init__(self, mtrx):
        self.mtrx = mtrx

    def __str__(self):
        return '\n'.join(['\t'.join([str(i) for i in j]) for j in self.mtrx])

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
                        for k in j[i]:
                            row.append(k)
                    else:
                        for k in j[i]:
                            row.append(k)
                        row.append('+')
            else:
                for j in lane:
                    if lane.index(j) == len(lane) - 1:
                        row[-1] = ' '
                        for k in j[i]:
                            row.append(k)
                    else:
                        for k in j[i]:
                            row.append(k)
                        row.append(' ')
            correct.append(row)
            row = []
        return Matrix(correct)


order = []
a = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
b = Matrix([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
c = Matrix([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
d = a + b + c
print(Matrix.correct_view(a, b, c, d))

