# MicroPython-NodeMCU
Command for burn flash
```python
boot.py : auto loading code after boot

deploy : quick command to modify the serial port and baud rate w/ fast speed
        port = /dev/tty.SLAB_USBtoUART
        baud = 921600
```

Examples for micropython at NodeMCU
```python

led_on.py : light LED 
        GPIO setting, OUT
        Pin:D0

flash_key : pushing the flash button will light LED
        GPIO setting, IN, Timer w/ polling 
        Pin:D3

led_breath.py : make LED light and dim
        software PWM, Timer, w/ delay
        may cause reset w/o correct setting
        Pin:D0

led_breath_timer.py : make LED light and dim
        software PWM, Timer
        set each period w/ timer
        Pin:D0

stepper.py : use 28BYJ-48 5V DC stepper
        Pin:D1, D2, D3, D4

sonic.py : use HC-SR04 to measure distance
        Pin:D5, D6


```
