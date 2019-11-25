# really dirty code
# Just connect your cktpy board then upload this program
# button A or button B will start the game
# at the end you'll have a led blinking either red or green
# green means truth and red means dare

from adafruit_circuitplayground.express import cpx
from time import sleep
import random

cpx.pixels.brightness = 0.1


def find_decay(delay):
    delay = delay + (0.25 * delay)
    return "x" if delay > 0.20 else delay


def loop(poss, delay):
    color_a = (int(random.randint(4,255)),int(random.randint(4,255)),int(random.randint(4,255)))
    color_b = (int(color_a[0]/2),int(color_a[1]/2),int(color_a[2]/2))
    color_c = (int(color_a[0]/3),int(color_a[1]/3),int(color_a[2]/3))
    # for x in range(times):
    for x, y in enumerate(poss):
        # print(x,y)
        if delay > 0.14:
            cpx.pixels[poss[x - 1]] = (0, 0, 0)
            cpx.pixels[y] = color_a
            sleep(delay)
            cpx.pixels[y] = (0, 0, 0)
        elif delay > 0.08:
            cpx.pixels[poss[x - 2]] = (0, 0, 0)
            cpx.pixels[y] = color_a
            cpx.pixels[poss[x - 1]] = color_b
            sleep(delay)
            cpx.pixels[poss[x - 1]] = (0, 0, 0)
        
        else:
            cpx.pixels[y] = color_a
            cpx.pixels[poss[x - 1]] = color_b
            cpx.pixels[poss[x - 2]] = color_c
            sleep(delay)
            cpx.pixels[poss[x - 2]] = (0, 0, 0)


def start():
    def_poss = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    poss_rand = random.randint(0, 9)
    poss = def_poss[poss_rand:] + def_poss[:poss_rand]
    # print(poss)
    delay = random.random() / 30
    while True:
        loop(poss, delay)
        delay = find_decay(delay)
        if delay == "x":
            # print("PING")
            cpx.pixels.fill((0, 0, 0))
            return poss[-1]
        # print(delay)


def blink(color):
    cpx.pixels.fill(color)
    sleep(0.1)
    cpx.pixels.fill((0, 0, 0))
    sleep(0.1)


cpx.red_led = 1
while True:
    cpx.pixels.fill((255, 0, 255))
    if cpx.button_a or cpx.button_b:
        sleep(0.1)
        curr = start()
        cpx.pixels.fill((0, 0, 0))
        punishment = random.choice([(0, 255, 0), (255, 0, 0)])
        while True:
            if cpx.button_a or cpx.button_b:
                break
            cpx.pixels[curr] = punishment
            sleep(0.1)
            cpx.pixels[curr] = (0, 0, 0)
            sleep(0.1)
