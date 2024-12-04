from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

from EyeFrame import (
    squareEyeFrame,
    eyeLidSleepLeftFrame,
    eyeLidSleepRightFrame,
    SleepZ1Frame,
    SleepZ2Frame,
    SleepZ3Frame
)





i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(255)


def sleeping():
    #set eye position
    x_axis=20
    y_axis=15

    #set sound 'z' position
    SleepZ1_X = 60
    SleepZ1_Y = 30

    #the outer for loop used to step by step closing
    for j in range(25,0,-5):
        #close
        for i in range(j,0,-1):
            oled.fill(0)
            oled.blit(squareEyeFrame, x_axis, y_axis)
            oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
            oled.blit(eyeLidSleepLeftFrame, x_axis, y_axis - i, 1)
            oled.blit(eyeLidSleepRightFrame, 54 + x_axis, y_axis - i, 1)
            oled.show()
        time.sleep(0.9)
        
        #open
        for i in range(0,j,1):
            oled.fill(0)
            oled.blit(squareEyeFrame, x_axis, y_axis)
            oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
            oled.blit(eyeLidSleepLeftFrame, x_axis, y_axis-i, 1)
            oled.blit(eyeLidSleepRightFrame, 54 + x_axis, y_axis-i, 1)
            oled.show()
        time.sleep(0.5)
        
        


    while True:
        #set close eye state and remove all 'z' 
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidSleepLeftFrame, x_axis, y_axis, 1)
        oled.blit(eyeLidSleepRightFrame, 54 + x_axis, y_axis, 1)
        oled.show()
        time.sleep(0.5)
        
        #z1 show
        oled.blit(SleepZ1Frame, SleepZ1_X, SleepZ1_Y)
        oled.show()
        time.sleep(0.5)
        
        #z2 show
        oled.blit(SleepZ2Frame, SleepZ1_X+10, SleepZ1_Y-10)
        oled.show()
        time.sleep(0.5)
        
        #z3 show
        oled.blit(SleepZ3Frame, SleepZ1_X+20, SleepZ1_Y-20)
        oled.show()
        time.sleep(0.5)



# while True:
#     sleeping()
    



