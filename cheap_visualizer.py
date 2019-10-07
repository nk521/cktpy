import array
import math
import time
from adafruit_circuitplayground.express import cpx
import audiobusio
import board
import random

def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    sum_of_samples = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(sum_of_samples / len(values))


mic = audiobusio.PDMIn(
    board.MICROPHONE_CLOCK,
    board.MICROPHONE_DATA,
    sample_rate=32000,
    bit_depth=16
)
samples = array.array('H', [0] * 160)
mic.record(samples, len(samples))
cpx.pixels.brightness = 0.1
old = 0
current = 0
while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)


    ranges = [[0, 100/2], [100/2, 200/2], [200/2, 300/2], [300/2, 400/2], [400/2, 500/2], [500/2, 600/2], [600/2, 700/2], [700/2, 800/2], [800/2, 900/2], [900/2, 2000/2]]
    for x in ranges:
        if int(magnitude) in range(int(x[0]),int(x[1])):
            current = (x[1]/100)
    if current < old:
        for x in range(current, old+1):
            x = int(x)
            try:
                cpx.pixels[x] = (0,0,0)
            except:
                pass

    for x in range(current):
            #cpx.pixels[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            cpx.pixels[x] = (x*28,0,255 - (x*28))

    old = current

    #time.sleep(0.05)
