# main.py -- put your code here!

import pyb

from plot import AccelPlot
from led import LEDIntensity, LEDAccel
from accel import AccelInfo

board_classes = [LEDIntensity, AccelInfo, AccelPlot, LEDAccel]
board_objects = [board_class() for board_class in board_classes]

global_counter = 0
global_state = dict()

while True:
    for board_object in board_objects:

        board_object.loop(**global_state)
        global_state.update({
            board_object.__class__.__name__: board_object.state
        })

        global_counter += 1
        if global_counter > 20:
            print(global_state)
            global_counter = 0
