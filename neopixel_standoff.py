"""
Press button A to start!
Yellow means 0
Cyan means 1
score is in binary :D
"""
from adafruit_circuitplayground.express import cpx
from time import sleep
import random

score_a = 0
score_b = 0
cpx.pixels.brightness = 0.1
winner = 0

while True:
    while True:
        if cpx.button_a:
            #print(0)
            cpx.pixels.fill((255,0,0))
            sleep(random.randint(2,7))
            cpx.pixels.fill((0,255,0))
            while True:
                if cpx.button_a:
                    winner = 1
                    break
                
                if cpx.button_b:
                    winner = 2
                    break
            break
        
    cpx.pixels.fill((0,0,0))

    if winner == 2:
        score_b += 1
        for _ in range(30):
            for x in range(5,10):
                cpx.pixels[x] = (0,0,255)
    if winner == 1:
        score_a += 1
        for _ in range(30):
            for x in range(0,5):
                cpx.pixels[x] = (0,0,255)
                
    cpx.pixels.fill((0,0,0))
    for x,y in enumerate(bin(score_a)[2:]):
        if y == "1":
            cpx.pixels[x] = (255,255,0)
        if y == "0":
            cpx.pixels[x] = (0,255,255)
        
    for x,y in enumerate(bin(score_b)[2:]):
        if y == "1":
            cpx.pixels[x+5] = (255,255,0)
        if y == "0":
            cpx.pixels[x+5] = (0,255,255)

