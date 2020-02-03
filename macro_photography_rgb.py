import time
import board
import analogio
from adafruit_circuitplayground.express import cpx
 
red = analogio.AnalogIn(board.A6)
blue = analogio.AnalogIn(board.A5)
green = analogio.AnalogIn(board.A4)
 
def valmap(value, istart, istop, ostart, ostop):
    ret = round(ostart + (ostop - ostart) * ((value - istart) / (istop - istart)))
    return 0 if ret < 4 else ret
  
def getVoltage(pin):
    return (pin.value * 3.3) / 65536
 
cpx.pixels.brightness = 0.1
while True:
    red_ = valmap(getVoltage(red), 0.0, 3.3, 0, 255.0)
    blue_ = valmap(getVoltage(blue), 0.0, 3.3, 0, 255.0)
    green_ = valmap(getVoltage(green), 0.0, 3.3, 0, 255.0)
    
    cpx.pixels.fill((red_,green_,blue_))
