from pyb import Pin
from time import sleep_ms, sleep_us

D1 = Pin(5, Pin.OUT)
D2 = Pin(4, Pin.OUT)
D3 = Pin(0, Pin.OUT)
D4 = Pin(2, Pin.OUT)

#steps of revolution = 4096, 8*512
seq = [[0,0,0,1],
       [0,0,1,1],
       [0,0,1,0],
       [0,1,1,0],
       [0,1,0,0],
       [1,1,0,0],
       [1,0,0,0],
       [1,0,0,1]]

def rotate(RPM, angle):
    if(RPM > 20):
        print("RPM should less than 20")
        return
    delay = int(60*1000*1000/4096/RPM)
    steps = int(512*abs(angle)/360)
    if angle < 0:
        direction = -1
    else:
        direction = 1
    for i in range(steps):
        for step in seq[::direction]:
            set_step(step)
            sleep_us(delay)

def set_step(step):
    D1.value(int(step[0]))
    D2.value(int(step[1]))
    D3.value(int(step[2]))
    D4.value(int(step[3]))

for i in range(1):
    rotate(20, 360)

#