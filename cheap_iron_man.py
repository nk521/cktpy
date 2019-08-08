from adafruit_circuitplayground.express import cpx
from time import sleep
import random

pix = cpx.pixels

def start(x):
    pix[x] = (3,3,3)
    sleep(1)
    pix[x] = (0,0,0)
    sleep(1)
    pix[x] = (50,50,50)
    sleep(0.5)
    pix[x] = (0,0,0)
    sleep(0.5)
    pix[x] = (20,20,20)
    sleep(0.2)
    pix[x] = (1,1,1)
    sleep(0.5)
    pix[x] = (100,100,100)
    sleep(0.1)
    pix[x] = (0,0,0)
    sleep(0.1)
    for _x in range(0,256):
        pix[x] = (_x,_x,_x)
        sleep(0.005)

start(0)
start(4)
start(7)

pix[0],pix[4],pix[7] = (255,255,255),(255,255,255),(255,255,255)

sl = 1.0

for x in range(0,10):
    pix[x] = (255,255,255)
    sleep(sl)
    sl -= 0.1
    pix[x] = (0,0,0)
    
sl = 0.1

for x in range(0,10):
    pix[x] = (255,255,255)
    sleep(sl)
    sl -= 0.01
    pix[x] = (0,0,0)
    
sl = 0.01

for x in range(0,10):
    pix[x] = (255,255,255)
    sleep(sl)
    sl -= 0.0001
    pix[x] = (0,0,0)


for _ in range(5):
    sl = 0.0001
    for x in range(0,10):
        pix[x] = (255,255,255)
        sleep(sl)
        sl -= 0.00001
        pix[x] = (0,0,0)
        

for _ in range(10):
    sl = 0.0001
    for x in range(0,10):
        pix[x] = (255,255,255)
        sleep(sl)
        sl -= 0.00001
        pix[x] = (0,0,0)

for _ in range(5):
    pix.fill((random.randint(0,255),random.randint(0,255),random.randint(0,255)))

pix.fill((255,255,255))
pix.brightness = 0.4
sleep(2)
while True:
    for x in range(1,10):
        pix.brightness = x/10.
        sleep(0.1)
        
    for x in range(0,10):
        x = 10 - x
        pix.brightness = x/10.
        sleep(0.1)
