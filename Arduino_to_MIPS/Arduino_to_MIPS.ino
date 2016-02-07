/*
Arduino_to_MIPS.ino

Copyright (C) 2016 Alejandro Simon
License: MIT License http://opensource.org/licenses/MIT

LinkIt Smart Duo 7688
*/

void setup() { 
    // open serial connection to USB Serial 
    Serial.begin(115200);
    // open internal serial connection to MT7688
    Serial1.begin(57600);
}

void loop() {
    // indicate end of value with a *
    Serial1.write("12345*");
}
