"""
There are 2 modes which depends on switch position
Mode A will paste the copied text and hit enter (to spam TG/WA/etc)
Mode B will not press enter but will paste continously!

Swtich A will start the spamming
Switch B will stop the spamming
"""
from adafruit_circuitplayground.express import cpx
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from time import sleep

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)
trigger = 0
mode = 0
while True:
    mode = cpx.switch

    if cpx.button_a:
        trigger = 1

    if cpx.button_b:
        trigger = 0

    if trigger == 1:
        if mode == False:
            kbd.press(Keycode.CONTROL, Keycode.V)
            kbd.release(Keycode.CONTROL, Keycode.V)
            kbd.press(Keycode.RETURN)
            kbd.release(Keycode.RETURN)
        if mode == True:
            kbd.press(Keycode.CONTROL, Keycode.V)
            kbd.release(Keycode.CONTROL, Keycode.V)
    sleep(0.01)
