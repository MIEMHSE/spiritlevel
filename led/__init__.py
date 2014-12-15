__author__ = 'Sergey Sobko'

import pyb

MAX_INTENSITY = 20
INTENSITY_STEP = 1
LOOP_DELAY = 20


class LEDIntensity(object):
    def __init__(self):
        self.led = pyb.LED(4)
        self.intensity = 0
        self.step = INTENSITY_STEP

    def loop(self, **kwargs):
        self.intensity = self.intensity + self.step
        if self.intensity not in range(0, MAX_INTENSITY):
            self.step = -self.step
            self.intensity = self.intensity + self.step
        self.led.intensity(self.intensity)
        if LOOP_DELAY:
            pyb.delay(LOOP_DELAY)

    @property
    def state(self):
        return {
            'intensity': self.intensity,
            'step': self.step,
            'led': self.led
        }
