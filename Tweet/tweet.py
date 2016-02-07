#!/usr/bin/env python
'''
tweet.py

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688

Packages needed:
pip install python-twitter
'''

import serial
import twitter
s = None


# Twitter variables
# Visit: https://apps.twitter.com/
twitterCK = ''  # Consumer Key
twitterCS = ''  # Consumer Secret
twitterATK = ''  # Access Token Key
twitterATS = ''  # Access Token Secret


def setup():
    global s
    # open serial COM port to /dev/ttyS0, which maps to UART0(D0/D1)
    # the baudrate is set to 57600 and should be the same as the one
    # specified in the Arduino sketch uploaded to ATMega32U4.
    s = serial.Serial("/dev/ttyS0", 57600)


def tweet():
    api = twitter.Api(consumer_key=twitterCK,
                      consumer_secret=twitterCS,
                      access_token_key=twitterATK,
                      access_token_secret=twitterATS)

    try:
        message = 'My tweet'
        status = api.PostUpdate(message)
    except twitter.TwitterError:
        print "Error in posting twitter Update"
    else:
        print status


def loop():
    # Read Serial sent from Arduino
    c = s.read()
    # Check for signal
    if c == '*':
        print 'Button detected'
        tweet()


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
