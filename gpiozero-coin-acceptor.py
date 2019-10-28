#!/usr/bin/env python

import time
from gpiozero import Button

coinslot = Button(17)

while True:
    coinslotState = True
    counter = 0
    while coinslotState:
            if coinslot.is_pressed:
                counter+=1
                time.sleep(.05)
                print(counter)

