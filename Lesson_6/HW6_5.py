class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing...')


class Pen(Stationery):
    def draw(self):
        print('Start drawing with PEN....')


class Pencil(Stationery):
    def draw(self):
        print('Start drawing with PENCIL....')


class Handle(Stationery):
    def draw(self):
        print('Start drawing with HANDLE....')


a = Stationery('ABC')
b = Pen('DEF')
c = Pencil('GHI')
d = Handle('JKL')
a.draw()
b.draw()
c.draw()
d.draw()