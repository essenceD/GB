from random import randint


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('{} go!'.format(self.name))

    def stop(self):
        print('{} stop!'.format(self.name))

    def turn(self):
        num = randint(0, 2)
        direction = ['left - turn', 'right-turn', 'u-turn']
        print('{} makes {}'.format(self.name, direction[num]))

    def show_speed(self):
        # sp = randint(5, 75)
        print('Car "{}" is moving with speed: {}'.format(self.name, self.speed))


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) > 60:
            print('Car "{}" is moving with speed: {}. Violation is $200'.format(self.name, self.speed))
        else:
            print('Car "{}" is moving with speed: {}. It\'s normal speed'.format(self.name, self.speed))


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) > 40:
            print('Car "{}" is moving with speed: {}. Violation is $400'.format(self.name, self.speed))
        else:
            print('Car "{}" is moving with speed: {}. It\'s normal speed'.format(self.name, self.speed))


class PoliceCar(Car):
    pass


a = PoliceCar(100, 'Black\'n\'white', 'Ford Taurus', True)
b = TownCar(65, 'Deep-Red', 'Mercedes-Benz CLS', False)
c = WorkCar(50, 'Light-Green', 'Garbage Truck', False)
d = SportCar(180, 'Yellow', 'Lamborghini Aventador', False)
e = TownCar(60, 'Gray', 'Volkswagen Passat - VIII', False)
f = WorkCar(15, 'Pink', 'Ice-Cream Truck', False)
g = PoliceCar(59, 'Brown', 'Sheriff\'s Wagon', True)
park = [a, b, c, d, e, f, g]
for i in park:
    print(f'Car: {i.name} | color: {i.color} | speed: {i.speed} | Police car: {i.is_police}')
    i.go()
    i.show_speed()
    i.turn()
    i.stop()
    print()


