#!/usr/bin/env python
'''
Arduino_to_MIPS.py

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
'''

import serial
s = None
value = ''


def setup():
    global s
    # open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
    # the baudrate is set to 57600 and should be the same as the one
    # specified in the Arduino sketch uploaded to ATMega32U4.
    s = serial.Serial("/dev/ttyS0", 57600)


def loop():
    global value

    # Read from serial and print
    c = s.read()
    # Check for end of value
    if c == '*':
        print value
        value = ''
    else:
        value = value + c


if __name__ == '__main__':
    # Setup the serial port
    setup()

    # Main loop
    while True:
        loop()
