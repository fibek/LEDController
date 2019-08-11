# LED Controller

### About app

Application with GUI written in python to control WS2811 LED strip connected to 
arduino with two (as yet) simple options: Rainbow and static color.

### Requirements

* [Python 3.x.x](https://www.python.org/downloads/)
* [Arduino IDE](https://www.arduino.cc/en/main/software)
* Arduino

### Installation

1. Clone repository

```
git clone https://github.com/Fibek/LEDController
```
2. Open Arduino IDE
3. Open ArduinoPart.ino
4. Choose your board and port

![screen1](https://github.com/Fibek/LEDController/tree/master/src/scr3_board_processor_port.png)

5. Set your macros

![screen2](https://github.com/Fibek/LEDController/tree/master/src/scr4_define.png)

7. Go to directory where you've cloned repository
8. Run controller.py (if your device port != /dev/ttyUSB0, first change it in controller.py using text editor

```
./controller.py
```
or
```
python3 controller.py
```
