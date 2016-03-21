from pyb import Pin
from time import sleep_ms, sleep_us, ticks_us
from machine import Timer

RS = Pin(5, Pin.OUT)
E = Pin(4, Pin.OUT)
D4 = Pin(14, Pin.OUT)
D5 = Pin(12, Pin.OUT)
D6 = Pin(13, Pin.OUT)
D7 = Pin(15, Pin.OUT)

# Define some device constants
WIDTH = 16 # Maximum characters per line
CHR = True
CMD = False
LINE1 = 0x80 # LCD RAM address for the 1st line
LINE2 = 0xC0 # LCD RAM address for the 2nd line
DELAY = 15 #ms

def lcd_enable():
    E.value(1)
    sleep_ms(DELAY)
    E.value(0)
    sleep_ms(DELAY)

def lcd_byte(bits, Mode=True): #CMD:False, CHR=True
    E.value(0)
    RS.value(1 if Mode else 0)
    D7.value(1 if (0x80 & bits) else 0)
    D6.value(1 if (0x40 & bits) else 0)
    D5.value(1 if (0x20 & bits) else 0)
    D4.value(1 if (0x10 & bits) else 0)
    # print("%s %02x %d %d %d %d" % (str(chr), bits,D4.value(), D5.value(), D6.value(), D7.value()))
    lcd_enable()
    #
    E.value(0)
    RS.value(1 if Mode else 0)
    D7.value(1 if (0x08 & bits) else 0)
    D6.value(1 if (0x04 & bits) else 0)
    D5.value(1 if (0x02 & bits) else 0)
    D4.value(1 if (0x01 & bits) else 0)
    # print("%d %d %d %d" % (D4.value(), D5.value(), D6.value(), D7.value()))
    lcd_enable()

def lcd_init():
    sleep_ms(DELAY)
    lcd_byte(0x33, CMD)
    lcd_byte(0x32, CMD)
    lcd_byte(0x06, CMD)
    lcd_byte(0x0C, CMD)
    lcd_byte(0x28, CMD)
    lcd_clear()

def lcd_clear():
    lcd_byte(0x01, CMD)
    lcd_byte(LINE1, CMD)

def lcd_str(msg, line=LINE1):
    lcd_byte(line, CMD)
    if len(msg) > WIDTH:
        print("over length")
        return
    for i in range(len(msg)):
        lcd_byte(ord(msg[i]), CHR)

if __name__ == '__main__':
    lcd_init()
    lcd_str("Hello World!", LINE1)
    lcd_str("2nd line.", LINE2)

#