#!/usr/bin/env python
'''
blink_D13.py

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
'''

import serial
import time
s = None


def setup():
    global s
    # open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
    # the baudrate is set to 57600 and should be the same as the one
    # specified in the Arduino sketch uploaded to ATMega32U4.
    s = serial.Serial("/dev/ttyS0", 57600)


def turn_led(on):
    x = "1" if on else "0"
    s.write(x)
    time.sleep(1)


def loop():
    # turn on LED
    turn_led(True)
    # turn off LED
    turn_led(False)

if __name__ == '__main__':
    # Setup the serial port
    setup()

    # Main loop
    while True:
        loop()
