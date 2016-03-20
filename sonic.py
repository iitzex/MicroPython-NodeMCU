from pyb import Pin
from time import sleep_ms, sleep_us, ticks_us
from machine import Timer

D5 = Pin(14, Pin.OUT)
D6 = Pin(12, Pin.IN)
Trig = D5
Echo = D6

def measure():
    Trig.low()
    sleep_us(15)
    Trig.high()
    sleep_us(15)
    Trig.low()
    while(Echo.value() == 0):
        start = ticks_us()
    while(Echo.value() == 1):
        end = ticks_us()
    duration = end - start
    dist = 0.03435 * 0.5 * duration
    print("duration: " + str(duration) + ", " + \
          "distance: " + str(dist))
    return dist

tim = Timer(0)
tim.deinit()
tim.init(period=200, mode=Timer.PERIODIC, callback=lambda t:measure())
#