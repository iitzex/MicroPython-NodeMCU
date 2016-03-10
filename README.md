# micropython-nodemcu
Command for MAC
```python
deploy : quick command to modify the serial port and baud rate
        port = /dev/tty.SLAB_USBtoUART
        baud = 921600
```

Examples for micropython at NodeMCU
```python

ledon.py : light LED 
        GPIO setting, OUT

flash_key : push the flash button will light LED
        GPIO setting, IN 

led_breath.py : make LED 
        software PWM, Timer

```
