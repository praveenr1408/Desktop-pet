from EyeFrame import squareEyeFrame


from machine import Pin, I2C
from ssd1306 import SSD1306_I2C
import time


i2c = I2C(0, scl=Pin(22), sda=Pin(21))  
oled = SSD1306_I2C(128, 64, i2c)
oled.contrast(255)

def alarm_animation():
    oled.fill(0)
    oled.blit(squareEyeFrame,20,15)
    oled.blit(squareEyeFrame,74,15)
    oled.show()

    for i in range(0,15,5):
        oled.fill(0)
        oled.blit(squareEyeFrame,20-i,15)
        oled.blit(squareEyeFrame,74-i,15)
        oled.show()
        
    for j in range(0,15,5):
        oled.fill(0)
        oled.blit(squareEyeFrame,20+j,15)
        oled.blit(squareEyeFrame,74+j,15)
        oled.show()
    
    for i in range(0,15,5):
        oled.fill(0)
        oled.blit(squareEyeFrame,20-i,15)
        oled.blit(squareEyeFrame,74-i,15)
        oled.show()
        
    for j in range(0,15,5):
        oled.fill(0)
        oled.blit(squareEyeFrame,20+j,15)
        oled.blit(squareEyeFrame,74+j,15)
        oled.show()
        
    oled.fill(0)
    oled.blit(squareEyeFrame,20,15)
    oled.blit(squareEyeFrame,74,15)
    oled.show()


# while True:
#     alarm_animation()
    