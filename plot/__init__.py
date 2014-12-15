__author__ = 'bug2bug'

from math import sin, pi, cos

STEP = pi * 2 / 128


def initialize():
    lcd = pyb.LCD('X')
    lcd.light(True)
    return locals()


def plot(lcd, initial_x=0, f=sin):
    x = initial_x
    for i in range(0, 127):
        y = f(x) * 16 + 16
        x += STEP
        lcd.pixel(int(x / STEP) - int(initial_x / STEP), int(y), 1)


def loop(**kwargs):
    lcd = kwargs.get('lcd')
    for i in range(0, 127):
        lcd.fill(0)
        plot(lcd, i * STEP)
        plot(lcd, i * STEP, cos)
        pyb.delay(10)
        lcd.text('Profitware Group!', 0, 13, 1)
        pyb.delay(10)
        lcd.show()
    return locals()