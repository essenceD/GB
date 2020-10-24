class WinDoor:
    def __init__(self, wd_len, wd_hi):
        self.square = wd_len * wd_hi


class Room:
    def __init__(self, l_1, l_2, h):
        self.square = 2 * (l_1 + l_2) * h
        self.wd = []

    def add_wd(self, wd_len, wd_hi):
        self.wd.append(WinDoor(wd_len, wd_hi))

    def common_sq(self,):
        main_sq = self.square
        for i in self.wd:
            main_sq -= i.square
        return main_sq


r = Room(7, 4, 3.7)
print(r.square)
r.add_wd(2, 2)
r.add_wd(2, 2)
print(r.common_sq())




