class Matrix:
    def __init__(self, mtrx):
        #if type(mtrx) is list:
        self.mtrx = mtrx
        #else:
        #    print('You have entered wrong data!')
        #    del(self, mtrx)

    def __str__(self):
        '''lane = [self.mtrx]
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
        return Matrix(correct)'''
        return '\n'.join(['\t'.join([str(i) for i in j]) for j in self.mtrx])

    def __add__(self, other):
        res = []
        string = []
        size.append(len(self.mtrx))
        size.append(len(other.mtrx))
        try:
            order.pop(-1)
            order.pop(-1)
            order.pop(-1)
        except IndexError:
            pass
        if len(order) > 0:
            for i in other.mtrx:
                order.append(i)
        else:
            for i in self.mtrx:
                order.append(i)
            for i in other.mtrx:
                order.append(i)
        for i in range(len(self.mtrx)):
            res.append(string)
            for j in range(i):
                string.append(self.mtrx[i][j] + other.mtrx[i][j])
        for i in res:
            order.append(i)
        print(f'result to convert: {order}')
        return Matrix(order[-(max(size)):])

    def correct_view(self, *args):
        pass


order, size = [], []
a = Matrix([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
b = Matrix([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
c = Matrix([[5, 5, 5], [5, 5, 5], [5, 5, 5]])
d = a + b + c
print(d)




