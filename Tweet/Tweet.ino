/*
Tweet.ino

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
*/

const int pinButton = 9;
int prevState = LOW;

void setup() { 
    // open serial connection to USB Serial 
    Serial.begin(115200);  
    // open internal serial connection to MT7688
    Serial1.begin(57600);   
    // Initiate pins in MT7688
    pinMode(pinButton, INPUT);
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
}
