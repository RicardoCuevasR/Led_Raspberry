#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

Led = 11 #pin 11

def setup():
    GPIO.setmode(GPIO.BOARD)    #Numbering according to the physical location
    GPIO.setup(Led, GPIO.OUT)   #Set pin mode as output
    GPIO.output(Led, GPIO.HIGH) #Output high level(+3,3 V) to off the led

def loop():
    while True:
        print ('...led on')
        GPIO.output(Led, GPIO.LOW)  #led on
        time.sleep(0.5)
        print ('...led off')
        GPIO.output(Led, GPIO.HIGH) #led off
        time.sleep(0.5)

def destroy():
    GPIO.output(Led, GPIO.HIGH) #led off
    GPIO.cleanup()              #Release resource

if __name__ == '__main__':  #Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt: #Press ctrl + C to end program
        destroy()
