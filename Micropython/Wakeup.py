from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time

from EyeFrame import (
    squareEyeFrame,
    eyeLidSleepLeftFrame,
    eyeLidSleepRightFrame,
    eyeLidNormalFrame,
    eyeLidHappyFrame
)
from EyeMovement import eye_movement

i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(255)

#open lids function
def open_lid(lid_range,speed):
    for i in range(0,lid_range,speed):
        oled.fill(0)
        oled.blit(squareEyeFrame,20,15)
        oled.blit(squareEyeFrame,74,15)
        oled.blit(eyeLidSleepLeftFrame,20,15-i,1)
        oled.blit(eyeLidSleepRightFrame,74,15-i,1)
        oled.show()
        
#close lids function      
def close_lid(lid_range,speed):
    for i in range(lid_range,0,-speed):
        oled.fill(0)
        oled.blit(squareEyeFrame,20,15)
        oled.blit(squareEyeFrame,74,15)
        oled.blit(eyeLidSleepLeftFrame,20,15-i,1)
        oled.blit(eyeLidSleepRightFrame,74,15-i,1)
        oled.show()

#sleeping function
def wakeup():
    
    #set close eye state
    oled.fill(0)
    oled.blit(squareEyeFrame,20,15)
    oled.blit(squareEyeFrame,74,15)
    oled.blit(eyeLidSleepLeftFrame,20,15,1)
    oled.blit(eyeLidSleepRightFrame,74,15,1)
    oled.show()  

    time.sleep(1)
    
    #the outer for loop used to step by step opening
    for j in range(0,25,10):
            #open lids function call
            open_lid(j,1)
            #close lids function call
            close_lid(j,1)
    
    #open lids
    open_lid(40,1)
    time.sleep(1)
    
    #normal eye movement function calls
    eye_movement('normal','left')
    eye_movement('normal','right')
    eye_movement('normal','center')

    time.sleep(1)



#wakeup()




    
    
    
