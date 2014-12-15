__author__ = 'bug2bug'

import pyb


class LEDIntensity(object):
    def __init__(self):
        self.led = pyb.LED(4)
        self.intensity = 0
        self.step = 4

    def loop(self, **kwargs):
        self.intensity = self.intensity + self.step
        if self.intensity not in range(0, 100):
            self.step = -self.step
            self.intensity = self.intensity + self.step
        self.led.intensity(self.intensity)
        pyb.delay(20)

    @property
    def state(self):
        return {
            'intensity': self.intensity,
            'step': self.step,
            'led': self.led
        }
