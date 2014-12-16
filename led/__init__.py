__author__ = 'Sergey Sobko'

import pyb

MAX_INTENSITY = 20
INTENSITY_STEP = 1
LOOP_DELAY = 20

ACCEL_EPS_X = 30
ACCEL_EPS_Y = 30
ACCEL_EPS_TILT = 50


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


class LEDAccel(object):
    def __init__(self):
        self.led = pyb.LED(3)
        self.led_tilt = pyb.LED(2)
        self.on = False
        self.on_tilt_counter = 0

    def loop(self, **kwargs):
        accel_info = kwargs.get('AccelInfo')
        self.on = False
        if accel_info:
            x, y, z, tilt = map(accel_info.get, ['x', 'y', 'z', 'tilt'])
            if abs(x) > ACCEL_EPS_X or abs(y) > ACCEL_EPS_Y:
                self.on = True
            if tilt > ACCEL_EPS_TILT:
                self.on_tilt_counter = 10
                self.led_tilt.on()

        # Tilt register
        if self.on_tilt_counter > 0:
            self.on_tilt_counter -= 1
        else:
            self.led_tilt.off()
            self.on_tilt_counter = 0

        # X, Y, Z epsilon
        if self.on:
            self.led.on()
        else:
            self.led.off()

    @property
    def state(self):
        return {
            'on': self.on,
            'led': self.led
        }
