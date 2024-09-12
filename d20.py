from microbit import *
import random

while True:
    if button_a.was_pressed():
        display.scroll(random.randint(1, 20))
