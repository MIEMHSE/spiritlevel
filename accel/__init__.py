__author__ = 'Sergey Sobko'

import pyb

INIT_DELAY = 20
LOOP_DELAY = 0


class AccelInfo(object):
    x, y, z = None, None, None
    tilt = None

    def __init__(self):
        self.accel = pyb.Accel()
        pyb.delay(INIT_DELAY)

    def loop(self, **kwargs):
        self.x, self.y, self.z = self.accel.filtered_xyz()
        self.tilt = self.accel.tilt()
        if LOOP_DELAY:
            pyb.delay(LOOP_DELAY)

    @property
    def state(self):
        return {
            'x': self.x,
            'y': self.y,
            'z': self.z,
            'tilt': self.tilt
        }
