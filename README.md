# LED Controller

## About app

Application with GUI written in python to control WS2811 LED strip connected to 
arduino with two (as yet) simple options: Rainbow and static color.

### Requirements

* [Python 3.x.x](https://www.python.org/downloads/)
* [Arduino IDE](https://www.arduino.cc/en/main/software)
* Arduino

#### Installation

1. Clone repository

```
git clone https://github.com/Fibek/LEDController
```
2. Open Arduino IDE
3. Open ArduinoPart.ino
4. Choose your board and port
![alt text](https://github.com/Fibek/LEDController/src/scr3_board_processor_port.png "Choose port, board, and processor")
5. Set your macros
![alt text](https://github.com/Fibek/LEDController/src/scr4_define.png "Set your macros")
7. Go to directory where you've cloned repository
8. Run conrtoller.py

```
./controller.py
```
or
```
python3 controller.py
```
