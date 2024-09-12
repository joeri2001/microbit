from microbit import *

compass.calibrate()

while True:
    degrees = compass.heading()
    if degrees < 45:
        display.show("N")
    elif degrees < 135:
        display.show("E")
    elif degrees < 225:
        display.show("S")
    elif degrees < 315:
        display.show("W")
