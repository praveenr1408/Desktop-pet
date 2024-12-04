from machine import Timer
import time
from ImageData import Number as num

from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import framebuf

i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
oled = SSD1306_I2C(128, 64, i2c)

minutes = 10
seconds = 0
timer_done = False

def countdown(timer):
    global minutes, seconds, timer_done
    if seconds == 0:
        if minutes > 0:
            minutes -= 1
            seconds = 59
        else:
            oled.fill(0)
            oled.text("Time Up!",10,10)
            oled.show()
            print("Timer done!")	
            timer_done = True
            timer.deinit()
            return
    else:
        seconds -= 1
    
    print(f"Time left: {minutes}m {seconds}s")

    mins = f"{minutes:02}"
    secs = f"{seconds:02}"

    m1 = int(mins[0])
    m2 = int(mins[1])
    
    s1 = int(secs[0])
    s2 = int(secs[1])

    frame1 = framebuf.FrameBuffer(bytearray(num.minImgData[m1]), 21, 32, framebuf.MONO_HLSB)
    frame2 = framebuf.FrameBuffer(bytearray(num.minImgData[m2]), 21, 32, framebuf.MONO_HLSB)
    
    frame3 = framebuf.FrameBuffer(bytearray(num.minImgData[s1]), 21, 32, framebuf.MONO_HLSB)
    frame4 = framebuf.FrameBuffer(bytearray(num.minImgData[s2]), 21, 32, framebuf.MONO_HLSB)
    
    frame5 = framebuf.FrameBuffer(bytearray(num.m), 10, 9, framebuf.MONO_HLSB)
    frame6 = framebuf.FrameBuffer(bytearray(num.s), 10, 9, framebuf.MONO_HLSB)

    oled.fill(0)
    oled.blit(frame1, 5, 15)
    oled.blit(frame2, 30, 15)
    oled.blit(frame5, 54, 38)
    oled.blit(frame3, 65, 15)
    oled.blit(frame4, 90, 15)
    oled.blit(frame6, 113, 38)
    oled.show()

timer = Timer(-1)
timer.init(period=1000, mode=Timer.PERIODIC, callback=countdown)

try:
    while not timer_done:
        time.sleep(1)
except KeyboardInterrupt:
    print("Timer interrupted!")
    timer.deinit()
