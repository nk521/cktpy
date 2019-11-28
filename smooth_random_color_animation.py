from adafruit_circuitplayground.express import cpx
from time import sleep
import random
#cpx.pixels.brightness = 0.1

def change(color_1,color_2):
    color_1 = list(color_1)
    if color_1[0] > color_2[0]:
        color_1[0] -= 1
    
    if color_1[0] < color_2[0]:
        color_1[0] += 1
        
    if color_1[1] > color_2[1]:
        color_1[1] -= 1
        
    if color_1[1] < color_2[1]:
        color_1[1] += 1
        
    if color_1[2] > color_2[2]:
        color_1[2] -= 1
        
    if color_1[2] < color_2[2]:
        color_1[2] += 1
        
    return tuple(color_1)

color_1 = (int(random.randint(0,255)),int(random.randint(0,255)),int(random.randint(0,255)))
color_2 = (int(random.randint(0,255)),int(random.randint(0,255)),int(random.randint(0,255)))

while True:
    while color_1 != color_2:
        sleep(0.001)
        cpx.pixels.fill(color_1)
        color_1 = change(color_1,color_2)
    
    color_1 = color_2
    color_2 = (int(random.randint(0,255)),int(random.randint(0,255)),int(random.randint(0,255)))
