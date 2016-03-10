from time import sleep_us, sleep_ms
from machine import Timer
from pyb import Pin

D0 = Pin(0, Pin.IN)

LED_BUILDIN = 16
led = Pin(LED_BUILDIN, Pin.OUT)

def get_value():
    print("flash_key : %d" % D0.value())
    if(D0.value()):
        led.high()
    else:
        led.low()

tim = Timer(0)
tim.init(period=100, mode=Timer.PERIODIC, callback=lambda t:get_value())
#