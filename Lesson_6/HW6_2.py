class Road:
    def __init__(self, length, width):
        self._length = int(length)
        self._width = int(width)

    def get_weight(self):
        weight = self._length * self._width * 25 * 5
        print('Based on a settlement rule (25 kilos of material per 1 sq.meter with depth 0.01 meter)\n'
              'To complete the road ({}) with depth 0.05 meters you need {} tons of material!'
              .format(self._length, weight/1000))


while True:
    length_1 = input('Enter length of road: ')
    width_1 = input('Enter width of road: ')
    try:
        int(length_1)
        int(width_1)
        break
    except ValueError:
        continue
new_road = Road(length_1, width_1)
Road.get_weight(new_road)

