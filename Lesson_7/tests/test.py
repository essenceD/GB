def __init__(self, x, y, default=0):
    self.__schema = [x, y]
    self.__data = [[default for i in range(y)] for i in range(x)]
    self.default = default

def __add__(self, other):
    maxes = [max(self.__schema[0], other.__schema[0]), max(self.__schema[1], other.__schema[1])]
    self.scale(*maxes)
    other.scale(*maxes)
    out = Matrix(*maxes)
    for i in self.__data:
        for j in i:
            out[i][j] = self[i][j] + other[i][j]
    return out


a = [[1, 1, 1],
     [1, 1, 1],
     [1, 1, 1]]
b = [[2, 2, 2],
     [2, 2, 2],
     [2, 2, 2]]
c = [[3, 3, 3],
     [3, 3, 3],
     [3, 3, 3]]
d = [[4, 4, 4],
     [4, 4, 4],
     [4, 4, 4]]
e = [[10, 10, 10],
     [10, 10, 10],
     [10, 10, 10]]


lane = [a, b, c, d, e]
correct = []
row = []
max_row = max([len(a), len(b), len(c)])
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
for i in correct:
    print(*i)
print(correct)

'''for i in correct:
    for j in range(2 * len(lane) - 1):
        string += str(i[j])
    string += '\n'
    #print(*i[0], *i[1], *i[2], *i[3], *i[4], *i[5], *i[6], *i[7], *i[8])
print(string)'''

'''    else:
        row.append(a[i])
        row.append([' '])
        row.append(b[i])
        row.append([' '])
        row.append(c[i])
        correct.append(row)
        row = []'''