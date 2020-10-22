from gpiozero import LED
from time import sleep
blue = LED(3)
red = LED(4)
sTime = .1
while True:
    blue.on()
    red.off()
    sleep(sTime)
    blue.off()
    red.on()
    sleep(sTime)

