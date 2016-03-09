from time import sleep_us, sleep_ms
from machine import Timer
from pyb import Pin

LED_BUILDIN = 16
p = Pin(LED_BUILDIN, Pin.OUT)

def count():
    for i in range(5):
        print(i)
        sleep_ms(100)

def breath():
    Brightness = 90
    Inhale = 800
    Pulse = Inhale*1000/Brightness
    for i in range(Brightness):
        p.low()
        sleep_us(i*10)
        p.high()
        sleep_us(int(Pulse) - i*10)
    for i in range(Brightness, 0, -1):
        p.low()
        sleep_us(i*10)
        p.high()
        sleep_us(int(Pulse) - i*10)

tim = Timer(0)
# tim.init(period=500, mode=Timer.PERIODIC, callback=lambda t:count())
tim.init(period=3000, mode=Timer.PERIODIC, callback=lambda t:breath())
#