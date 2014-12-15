# main.py -- put your code here!

from plot import Plot
from led import LEDIntensity

board_classes = [LEDIntensity, Plot]
board_objects = [board_class() for board_class in board_classes]

while True:
    for board_object in board_objects:
        board_object.loop()
        print(board_object.state)
