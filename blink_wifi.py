#!/usr/bin/env python
'''
blink_wifi.py

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
'''

import mraa
import time

led = mraa.Gpio(44)  # 44 = Wi-Fi LED
led.dir(mraa.DIR_OUT)  # set direction to output

while True:
    led.write(1)  # turn on LED
    time.sleep(0.5)
    led.write(0)  # turn off LED
    time.sleep(0.5)
