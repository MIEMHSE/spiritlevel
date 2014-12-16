# main.py -- put your code here!

import pyb

from plot import Plot, AccelPlot
from led import LEDIntensity
from accel import AccelInfo

board_classes = [LEDIntensity, AccelInfo, AccelPlot]
board_objects = [board_class() for board_class in board_classes]

global_state = dict()
while True:
    for board_object in board_objects:
        if global_state:
            board_object.loop(**global_state)
        else:
            board_object.loop()
        global_state.update({
            board_object.__class__.__name__: board_object.state
        })
        print(global_state)
        pyb.delay(200)
