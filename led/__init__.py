__author__ = 'bug2bug'

import pyb


def initialize():
    led = pyb.LED(4)
    intensity = 0
    step = 1
    return locals()


def loop(**kwargs):
    led, intensity, step = map(kwargs.get, ['led', 'intensity', 'step'])
    intensity = (intensity + step)
    if not intensity in range(0, 100):
        step = -step
        intensity = (intensity + step)
    led.intensity(intensity)
    pyb.delay(20)
    return locals()