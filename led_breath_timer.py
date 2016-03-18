from time import sleep_us, sleep_ms
from machine import Timer
from pyb import Pin

LED_BUILDIN = 16
p = Pin(LED_BUILDIN, Pin.OUT)

Pulse = 24000
Flash = 50
Brightness = 0.8

MAX = int(Pulse * Brightness)
MIN = -int(MAX/25)
ix = 0
step = int(MAX / Flash)

def breath():
    global ix
    global step
    if ix > 0:
        p.low()
        # print(ix)
        sleep_us(ix)
        p.high()
        sleep_us(Pulse - ix)
    else:
        sleep_us(Pulse)
    ix += step
    if ix >= MAX and step > 0:
        step = -step
    if ix <= MIN and step < 0:
        step = -step

tim = Timer(0)
tim.deinit()
tim.init(period=25, mode=Timer.PERIODIC, callback=lambda t:breath())
#
