/*
blink_D13.ino

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
*/

const int pin = 13;

void setup() { 
    // open serial connection to USB Serial 
    Serial.begin(115200);  
    // open internal serial connection to MT7688
    Serial1.begin(57600);   
    // in MT7688, this maps to device 
    pinMode(pin, OUTPUT);
}

void loop() {
    // read from MT7688
    int c = Serial1.read();
    if (c != -1) {
        switch(c) {
            // turn off D13 when receiving "0"
            case '0':                
                digitalWrite(pin, 0); 
                break;
            // turn on D13 when receiving "1" 
            case '1':
                digitalWrite(pin, 1); 
                break; 
        }
    }
}
