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
while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    
    current = 0
    ranges = [[0, 100], [100, 200], [200, 300], [300, 400], [400, 500], [500, 600], [600, 700], [700, 800], [800, 900], [900, 1000]]
    for x in ranges:
        if int(magnitude) in range(x[0],x[1]):
            current = (x[1]/100) - 1 

    for x in range(current):
        cpx.pixels[x] = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
        
    cpx.pixels.fill((0,0,0))
    time.sleep(0.1)
