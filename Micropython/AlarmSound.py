from machine import Pin, PWM
import time

#import tune array
from Sound import Tunes as t

#alarm sound function
def alarm_sound():
    
    #set pin 15
    buzzer = PWM(Pin(15))
    
    #play tone function
    def play_tone(frequency, duration):
        buzzer.freq(frequency)
        buzzer.duty(100)  
        time.sleep(duration)
        buzzer.duty(0)  
    
    #play alarm sound function
    def play_alarm(song):
        for frequency, duration in song:
            play_tone(frequency, duration)

    #put the alarm sound data from Tunes
    tune = t.alarm_sound

    #call play alarm function
    play_alarm(tune)

# while True:
#     login_sound()
#     time.sleep(1)