__author__ = 'Sergey Sobko'

import pyb
from math import sin, pi, cos

STEP = pi * 2 / 128
LOOP_DELAY_GRAPHICS = 10
LOOP_DELAY_TEXT = 10
MAXX = 127.0
MAXY = 31.0
ACCEL_COEFF_X = MAXX / 90 / 2
ACCEL_COEFF_Y = MAXY / 90 / 2


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


class AccelPlot(Plot):
    def draw_square_for_accel(self, x, y):
        min_x = int(min(MAXX / 2 + x * ACCEL_COEFF_X, MAXX / 2))
        max_x = int(max(MAXX / 2 + x * ACCEL_COEFF_X, MAXX / 2))
        min_y = int(min(MAXY / 2 - y * ACCEL_COEFF_Y, MAXY / 2))
        max_y = int(max(MAXY / 2 - y * ACCEL_COEFF_Y, MAXY / 2))
        for x in range(min_x, max_x):
            self.lcd.pixel(x, min_y, 1)
            self.lcd.pixel(x, max_y, 1)
        for y in range(min_y, max_y):
            self.lcd.pixel(min_x, y, 1)
            self.lcd.pixel(max_x, y, 1)

    def loop(self, **kwargs):
        accel_info = kwargs.get('AccelInfo')
        if accel_info:
            x, y, z = map(accel_info.get, ['x', 'y', 'z'])
            self.lcd.fill(0)
            self.draw_square_for_accel(x, y)
            if LOOP_DELAY_GRAPHICS:
                pyb.delay(LOOP_DELAY_GRAPHICS)
            self.lcd.show()
