import Blink as blk
import Sleeping as s
import random
import time


#eye movement function
def eye_movement(react,direction):
    #left
    if direction == 'left':
        for i in range(0,10,5):
            if react == 'normal':
                blk.normal_blink(20-i,15,5,0.5)
            if react == 'sad':
                blk.sad_blink(20-i,15,5,0.5)
            if react == 'happy':
                blk.happy_blink(20-i,15,5,0.5)
            if react == 'angry':
                blk.angry_blink(20-i,15,5,0.5)
                
    #right           
    if direction == 'right':
        for i in range(0,10,5):
            if react == 'normal':
                blk.normal_blink(20+i,15,5,0.5)
            if react == 'sad':
                blk.sad_blink(20+i,15,5,0.5)
            if react == 'happy':
                blk.happy_blink(20+i,15,5,0.5)
            if react == 'angry':
                blk.angry_blink(20+i,15,5,0.5)
            
            
    #up
    if direction == 'up':
        for i in range(0,10,5):
            if react == 'normal':
                blk.normal_blink(20,15-i,5,0.5)
            if react == 'sad':
                blk.sad_blink(20,15-i,5,0.5)
            if react == 'happy':
                blk.happy_blink(20,15-i,5,0.5)
            if react == 'angry':
                blk.angry_blink(20,15-i,5,0.5)

            
    #down
    if direction == 'down':
        for i in range(0,10,5):
            if react == 'normal':
                blk.normal_blink(20,15+i,5,0.5)
            if react == 'sad':
                blk.sad_blink(20,15+i,5,0.5)
            if react == 'happy':
                blk.happy_blink(20,15+i,5,0.5)
            if react == 'angry':
                blk.angry_blink(20,15+i,5,0.5)
                
    #center
    if direction == 'center':
        for i in range(0,10,5):
            if react == 'normal':
                blk.normal_blink(20,15,5,0.5)
            if react == 'sad':
                blk.sad_blink(20,15,5,0.5)
            if react == 'happy':
                blk.happy_blink(20,15,5,0.5)
            if react == 'angry':
                blk.angry_blink(20,15,5,0.5)


    
# while True:
#     eye_movement('angry','center')
