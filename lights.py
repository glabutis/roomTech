import RPi.GPIO as gpio
import time
import pygame

gpio.setmode(gpio.BCM)

ldr_pin = 13

def rc_time (ldr_pin):
    count = 0
  
    #Output on the pin for 
    gpio.setup(ldr_pin, gpio.OUT)
    gpio.output(ldr_pin, gpio.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    gpio.setup(ldr_pin, gpio.IN)
  
    #Count until the pin goes high
    while (gpio.input(ldr_pin) == gpio.LOW):
        count += 1

    return count

light_sen = rc_time(ldr_pin)

def loop():
    #Catch when script is interrupted, cleanup correctly
    try:
        # Main loop
        while True:
            light_sen = rc_time(ldr_pin)
            print(light_sen)
            if light_sen < 1000:
                standDown()
            


        
    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()


def standDown():
    pygame.mixer.init()
    pygame.mixer.music.load("file.mp3")
    pygame.mixer.music.set_volume(1.0)
    pygame.mixer.music.play()

while pygame.mixer.music.get_busy() == True:
	pass
while light_sen < 1000:
    if light_sen > 1000:
        loop()

loop()