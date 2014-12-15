__author__ = 'Sergey Sobko'

import pyb
from math import sin, pi, cos

STEP = pi * 2 / 128
LOOP_DELAY_GRAPHICS = 10
LOOP_DELAY_TEXT = 10


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
        if LOOP_DELAY_GRAPHICS:
            pyb.delay(LOOP_DELAY_GRAPHICS)
        self.lcd.text('Profitware Group', 0, 13, 1)
        if LOOP_DELAY_TEXT:
            pyb.delay(LOOP_DELAY_TEXT)
        self.lcd.show()
        self.counter += 1

    @property
    def state(self):
        return {
            'lcd': self.lcd,
        }
