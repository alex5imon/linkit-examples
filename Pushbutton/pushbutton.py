#!/usr/bin/env python
'''
pushbutton.py

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


def show_level():
    s.write(str(level))
    # wait 3 secs
    time.sleep(3)
    # turn LED off again
    s.write('0')


def loop():
    global level

    # Read Serial sent from Arduino
    c = s.read()
    # Check for signal
    if c == '*':
        print 'Button detected'
        # calculate level
        level = (level + 1) if (level < 3) else 0
        show_level()

if __name__ == '__main__':
    # Setup the serial port
    setup()

    # Main loop
    while True:
        try:
            loop()
        except (KeyboardInterrupt, SystemExit):
            # turn off everything
            s.write('0')
            print 'Thanks for using me!'
            raise
