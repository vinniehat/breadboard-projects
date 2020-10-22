from gpiozero import LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

host = "192.168.1.23"
factory = PiGPIOFactory(host)
red = LED(2, pin_factory=factory)
blue = LED(3, pin_factory=factory)
sTime = .05


while True:
    blue.on()
    red.off()
    sleep(sTime)
    blue.off()
    red.on()
    sleep(sTime)

