from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

from EyeFrame import (
    squareEyeFrame,
    roundEyeFrame,
    eyeLidNormalFrame,
    eyeLidAngryLeftFrame,
    eyeLidAngryRightFrame,
    eyeLidSadLeftFrame,
    eyeLidSadRightFrame,
    eyeLidHappyFrame
)


i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(255)



#normal blink fnction
def normal_blink(x_axis, y_axis, blk_speed, delay):
    
    min_lid_range = 0
    max_lid_range = 40
    
    #close
    for y in range(max_lid_range, min_lid_range, -blk_speed):
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidNormalFrame, x_axis, y_axis - y, 1)
        oled.blit(eyeLidNormalFrame, 54 + x_axis, y_axis - y, 1)
        oled.show()
    
    #open
    for y in range(min_lid_range, max_lid_range, blk_speed):
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidNormalFrame, x_axis, y_axis - y, 1)
        oled.blit(eyeLidNormalFrame, 54 + x_axis, y_axis - y, 1)
        oled.show()
    time.sleep(delay)
    


#angry blink function
def angry_blink(x_axis, y_axis, blk_speed, delay):
    
    min_lid_range = 10
    max_lid_range = 30
    
    #close
    for y in range(max_lid_range, min_lid_range, -blk_speed):
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidAngryLeftFrame, x_axis, y_axis - y, 1)
        oled.blit(eyeLidAngryRightFrame, 54 + x_axis, y_axis - y, 1)
        oled.show()
    time.sleep(delay)
    #open
    for y in range(min_lid_range, max_lid_range, blk_speed):
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidAngryLeftFrame, x_axis, y_axis - y, 1)
        oled.blit(eyeLidAngryRightFrame, 54 + x_axis, y_axis - y, 1)
        oled.show()
    time.sleep(delay)

    
#sad blink function
def sad_blink(x_axis, y_axis, blk_speed, delay):
    
    min_lid_range = 10
    max_lid_range = 30
    
    #close
    for y in range(max_lid_range, min_lid_range, -blk_speed):
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidSadLeftFrame, x_axis, y_axis - y, 1)
        oled.blit(eyeLidSadRightFrame, 54 + x_axis, y_axis - y, 1)
        oled.show()
    time.sleep(delay)
    #open
    for y in range(min_lid_range, max_lid_range, blk_speed):
        oled.fill(0)
        oled.blit(squareEyeFrame, x_axis, y_axis)
        oled.blit(squareEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidSadLeftFrame, x_axis, y_axis - y, 1)
        oled.blit(eyeLidSadRightFrame, 54 + x_axis, y_axis - y, 1)
        oled.show()
    time.sleep(delay)
    


#happy blink funcrion
def happy_blink(x_axis, y_axis, blk_speed, delay):
    
    min_lid_range = 8
    max_lid_range = 20
    
    #open
    for y in range(max_lid_range, min_lid_range, -blk_speed):
        oled.fill(0)
        oled.blit(roundEyeFrame, x_axis, y_axis)
        oled.blit(roundEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidHappyFrame, x_axis, y_axis + y, 1)
        oled.blit(eyeLidHappyFrame, 54 + x_axis, y_axis + y, 1)
        oled.show()
    time.sleep(delay/2)
    
    #close
    for y in range(min_lid_range, max_lid_range, blk_speed):
        oled.fill(0)
        oled.blit(roundEyeFrame, x_axis, y_axis)
        oled.blit(roundEyeFrame, 54 + x_axis, y_axis)
        oled.blit(eyeLidHappyFrame, x_axis, y_axis + y, 1)
        oled.blit(eyeLidHappyFrame, 54 + x_axis, y_axis + y, 1)
        oled.show()
    time.sleep(delay)



# while True:
#     sad_blink(20,15,2,1)
#     angry_blink(20,15,2,1)
#     normal_blink(20,15,2,1)
#     happy_blink(20,15,2,1)


        

     
    
        
    
        
    
