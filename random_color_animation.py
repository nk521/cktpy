from adafruit_circuitplayground.express import cpx
from time import sleep
import random
#cpx.pixels.brightness = 0.1

def breathe(color,start=20,end=255,skip=3,delay=0.01):
    for x in range(start,end,skip):
        cpx.pixels.fill((int(x*(color[0]/255)),int(x*(color[1]/255)),int(x*(color[2]/255))))
        sleep(delay)

    sleep(0.2)
    for x in range(end,start,-1*skip):
        cpx.pixels.fill((int(x*(color[0]/255)),int(x*(color[1]/255)),int(x*(color[2]/255))))
        sleep(delay)

while True:
    color = (int(random.randint(0,255)),int(random.randint(0,255)),int(random.randint(0,255)))
    breathe(color,delay=0.001)
