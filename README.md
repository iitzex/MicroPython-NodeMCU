# MicroPython-NodeMCU
Command for burn flash
```python
deploy : quick command to modify the serial port and baud rate w/ fast speed
        port = /dev/tty.SLAB_USBtoUART
        baud = 921600
```

Examples for micropython at NodeMCU
```python

led_on.py : light LED 
        GPIO setting, OUT

flash_key : pushing the flash button will light LED
        GPIO setting, IN, Timer w/ polling 

led_breath.py : make LED light and dim
        software PWM, Timer, w/ delay
        may cause reset w/o correct setting

led_breath_timer.py : make LED light and dim
        software PWM, Timer
        set each period w/ timer

```
