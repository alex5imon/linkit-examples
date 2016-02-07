#!/usr/bin/env python
'''
blink_LEDs.py

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
'''

import serial
import time
s = None
level = 0


def setup():
    global s
    # open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
    # the baudrate is set to 57600 and should be the same as the one
    # specified in the Arduino sketch uploaded to ATMega32U4.
    s = serial.Serial("/dev/ttyS0", 57600)


def turn_level():
    s.write(str(level))
    time.sleep(1)


def loop():
    global level

    turn_level()
    level = (level + 1) if (level < 3) else 0


if __name__ == '__main__':
    # Setup the serial port
    setup()

    # Main loop
    while True:
        loop()
