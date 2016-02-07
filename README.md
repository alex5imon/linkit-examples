# linkit-examples
Examples created for the LinkIt duo 7688  

## Tutorials 

New? Learn how to you LinkIt Smart Duo [here](https://github.com/alex5imon/linkit-examples/wiki/First-steps)  

### Blink WiFi

Make the WiFi LED blink once per second  

1) `scp blink_wifi.py root@mylinkit.local:~`  
2) `python blink_wifi.py`  

### Arduino to MIPS

Demonstrates how to send information from Arduino to MIPS

1) Upload the sketch `Arduino_to_MIPS.ino` to the board  
2) `scp Arduino_to_MIPS.py root@mylinkit.local:~`  
3) `python Arduino_to_MIPS.py`  

### Blink D13

Make LED D13 on the board blink using Python + Arduino sketch  

GPIO: D13 (Optional)  
[TODO] Upload Board design  

1) Upload the sketch `Blink_D13.ino` to the board  
2) `scp blink_LEDs.py root@mylinkit.local:~`  
3) `python blink_LEDs.py` 

NOTE: you can also connect a LED to Pin D13 to see it blinking  

### Blink LEDs

Make LEDs blink using Python + Arduino sketch  

GPIO: D12, D11, D10  
[TODO] Upload Board design  

1) Upload the sketch `Blink_LEDs.ino` to the board  
2) `scp blink_LEDs.py root@mylinkit.local:~`  
3) `python blink_LEDs.py`  

### Pushbutton

Turn LEDs on/off by pushing a button

GPIO: D12, D11, D10, D9  
[TODO] Upload Board design  

1) Upload the sketch `Pushbutton.ino` to the board  
2) `scp pushbutton.py root@mylinkit.local:~`  
3) `python pushbutton.py`  

### Tweet

Tweet a message when pushing a button

GPIO: D9  
[TODO] Upload Board design  

1) Configure Twitter app, follow [this instructions](https://github.com/alex5imon/linkit-examples/wiki/Tweet-from-LinkIt-Smart-Duo)  
2) Upload the sketch `Tweet.ino` to the board  
3) Update the Twitter variables in `tweet.py`  
4) `scp tweet.py root@mylinkit.local:~`  
5) `python tweet.py`  

## Useful links
- Official wiki: [here](http://www.seeedstudio.com/wiki/LinkIt_Smart_7688_Duo)  
- Install LinkIt Smart in your Arduino IDE: [here](https://labs.mediatek.com/site/global/developer_tools/mediatek_linkit_smart_7688/get_started/7688_duo/arduino/)  
- LinkIt with NodeJS: [book](https://iamblue.gitbooks.io/linkit-smart-nodejs/content/en/intro/index.html)  
- LinkIt One projects: [here](http://www.instructables.com/id/Mediatek-LinkIt-ONE/)  
- Grove Multichannel Gas Sensor: [here](http://www.seeedstudio.com/wiki/Grove_-_Multichannel_Gas_Sensor)  
- Portable fire alarm: [recipe](http://www.seeedstudio.com/recipe/451-portable-fire-alarm-with-linkit-smart.html)