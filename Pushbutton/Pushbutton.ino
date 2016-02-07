/*
Pushbutton.ino

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
*/

const int pinButton = 9;
const int pin1 = 10;
const int pin2 = 11;
const int pin3 = 12;

int prevState = LOW;

void setup() { 
    // open serial connection to USB Serial 
    Serial.begin(115200);  
    // open internal serial connection to MT7688
    Serial1.begin(57600);   
    // Initiate pins in MT7688
    pinMode(pinButton, INPUT);
    pinMode(pin1, OUTPUT);
    pinMode(pin2, OUTPUT);
    pinMode(pin3, OUTPUT);
}

// Turn leds (s1, s2, s3) on(1) or off(0)
void update_leds(int s1, int s2, int s3) {
    digitalWrite(pin1, s1);
    digitalWrite(pin2, s2);
    digitalWrite(pin3, s3);
}

void loop() {
    // check for button press
    int state = digitalRead(pinButton);
    if (state != prevState) {
        prevState = state;
        if (state == LOW) {
            // Send serial signal to MIPS
            Serial1.write("*");
            delay(200);
        }
    }
    // read Serial coming from MIPS
    int c = Serial1.read();
    if (c != -1) {
        switch(c) {
            // turn off all LEDs
            case '0':
                update_leds(0, 0, 0);
                break;
            // turn on level 1 
            case '1':
                update_leds(1, 0, 0); 
                break;
            // turn on level 2 
            case '2':
                update_leds(1, 1, 0);
                break; 
            // turn on level 3 
            case '3':
                update_leds(1, 1, 1);
                break; 
        }
    }
}
