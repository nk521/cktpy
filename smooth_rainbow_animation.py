from adafruit_circuitplayground.express import cpx
from time import sleep
import random
#cpx.pixels.brightness = 0.1

violet = (255,0,255)
indigo = (147,0,255)
blue = (0,0,255)
green = (0,255,0)
yellow = (255,255,0)
orange = (255,174,66)
red = (255,0,0)

colors = [indigo,blue,green,yellow,orange,red,violet]
def change(color_1,color_2,speed=1):
    color_1 = list(color_1)
    if color_1[0] > color_2[0]:
        color_1[0] -= speed

    if color_1[0] < color_2[0]:
        color_1[0] += speed

    if color_1[1] > color_2[1]:
        color_1[1] -= speed

    if color_1[1] < color_2[1]:
        color_1[1] += speed

    if color_1[2] > color_2[2]:
        color_1[2] -= speed

    if color_1[2] < color_2[2]:
        color_1[2] += speed

    if color_1[0] > 255:
        color_1[0] = 255

    if color_1[0] < 0:
        color_1[0] = 0

    if color_1[1] > 255:
        color_1[1] = 255

    if color_1[1] < 0:
        color_1[1] = 0

    if color_1[2] > 255:
        color_1[2] = 255

    if color_1[2] < 0:
        color_1[2] = 0

    return tuple(color_1)

while True:
    color_1 = violet
    for x in colors:
        color_2 = x
        #print(color_1, "->", color_2)
        while color_1 != color_2:
            cpx.pixels.fill(color_1)
            color_1 = change(color_1,color_2)
