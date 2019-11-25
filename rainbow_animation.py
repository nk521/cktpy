from adafruit_circuitplayground.express import cpx
from time import sleep
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
violet = (255,0,255)
indigo = (147,0,255)
yellow = (255,255,0)
orange = (255,174,66)
colors = [violet,indigo,blue,green,yellow,orange,red]
#cpx.pixels.brightness = 0.1

def breathe(color,start=3,end=255,skip=3,delay=0.01):
    for x in range(start,end,skip):
        cpx.pixels.fill((int(x*(color[0]/255)),int(x*(color[1]/255)),int(x*(color[2]/255))))
        sleep(delay)

    sleep(0.2)
    for x in range(end,start,-1*skip):
        cpx.pixels.fill((int(x*(color[0]/255)),int(x*(color[1]/255)),int(x*(color[2]/255))))
        sleep(delay)

while True:
    for x in colors:
        breathe(x,delay=0.001)
    
    """
    for x in range(15,255,15):
        cpx.pixels.fill((0,x,x))
        sleep(0.04)
    for x in range(255,15,-15):
        cpx.pixels.fill((0,x,x))
        sleep(0.04)
    """
