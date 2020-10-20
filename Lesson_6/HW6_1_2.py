from time import sleep
from itertools import cycle


class TrafficLight:
    __colors = ['red', 'yellow', 'green', 'yellow']

    def running(self):

        for i in cycle(self._TrafficLight__colors):
            if i == 'red':
                print('\r', '\x1b[1;30;41m' + f'     {i}     ' + '\x1b[0m', end='')
                sleep(1)
            elif i == 'yellow':
                print('\r', '\x1b[1;30;43m' + f'    {i}   ' + '\x1b[0m', end='')
                sleep(1)
            else:
                print('\r', '\x1b[1;30;42m' + f'    {i}    ' + '\x1b[0m', end='')
                sleep(1)


a = TrafficLight()
TrafficLight.running(a)



