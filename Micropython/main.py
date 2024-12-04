import Blink as blk
import Sleeping as s
from EyeMovement import eye_movement
import random
import time
from Wakeup import wakeup
from AlarmEyes import alarm_animation
from test import (alarm_sound)

wakeup()

directions = ['left','right','up','down']
random_direction = random.choice(directions)
eye_movement('normal',random_direction)

count = 0
while count < 5:

    alarm_animation()
    alarm_sound()
    alarm_animation()
    count+=1
    

    





