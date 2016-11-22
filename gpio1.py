import RPi.GPIO as GPIO
import time
import sys


GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

GPIO.setup(24, GPIO.OUT)

try:
    while 1:
        key = sys.stdin.read(1)
        if key == 'a':
            GPIO.output(25, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(25, GPIO.LOW)
            time.sleep(1)
        if key == 's':
            GPIO.output(24, GPIO.HIGH)
            time.sleep(1)
            GPIO.output(24, GPIO.LOW)
            time.sleep(1)
except KeyboardInterrupt:
    GPIO.output(24, GPIO.LOW)
    GPIO.output(25, GPIO.LOW)
    GPIO.cleanup()
