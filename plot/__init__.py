__author__ = 'bug2bug'

import pyb
from math import sin, pi, cos

STEP = pi * 2 / 128


class Plot(object):
    def __init__(self):
        self.lcd = pyb.LCD('X')
        self.lcd.light(True)
        self.counter = 0

    def plot(self, initial_x=0, f=sin):
        x = initial_x
        for i in range(0, 127):
            y = f(x) * 16 + 16
            x += STEP
            self.lcd.pixel(int(x / STEP) - int(initial_x / STEP), int(y), 1)

    def loop(self, **kwargs):
        if self.counter > 127:
            self.counter = 0
        i = self.counter
        self.lcd.fill(0)
        self.plot(i * STEP)
        self.plot(i * STEP, cos)
        pyb.delay(10)
        self.lcd.text('Profitware Group', 0, 13, 1)
        pyb.delay(10)
        self.lcd.show()
        self.counter += 1

    @property
    def state(self):
        return {
            'lcd': self.lcd,
        }
