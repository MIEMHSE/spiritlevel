# main.py -- put your code here!

import led

global_state = led.initialize()
while True:
    global_state.update(led.loop(**global_state))