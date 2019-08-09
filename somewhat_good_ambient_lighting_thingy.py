from adafruit_circuitplayground.express import cpx
from time import sleep
r,g,b = 0,0,0
mode = ['r','g','b']
curr = 'r'
counter=0
bright = 1.0
while True:
    cpx.pixels.fill((r,g,b))
    if cpx.button_a and cpx.button_b:
        counter += 1
        curr = mode[counter % 3]
        sleep(0.2)

    if curr == 'r':
        if cpx.button_a:
            r += 5

        if cpx.button_b:
            r -= 5

        if r > 255:
            r = 255

        if r < 0:
            r = 0

        cpx.red_led = 1
        sleep(0.05)

    if curr == 'g':
        if cpx.button_a:
            g += 5

        if cpx.button_b:
            g -= 5

        if g > 255:
            g = 255

        if g < 0:
            g = 0

        cpx.red_led = 1
        sleep(0.05)
        cpx.red_led = 0

    if curr == 'b':
        if cpx.button_a:
            b += 5

        if cpx.button_b:
            b -= 5

        if b > 255:
            b = 255

        if b < 0:
            b = 0

        sleep(0.05)

    if cpx.switch == True:
        while cpx.switch == True:
            if cpx.button_a:
                bright += 0.1
                if bright > 1.0:
                    bright = 1.0

            if cpx.button_b:
                bright -= 0.1
                if bright < 0.0:
                    bright = 0.0

            cpx.pixels.brightness = bright
            sleep(0.1)

    sleep(0.05)
