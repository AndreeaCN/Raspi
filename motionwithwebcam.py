import RPi.GPIO as GPIO
import time
import os

#from picamera import PiCamera
GPIO.setmode(GPIO.BCM)
#camera = PiCamera()

PIR_PIN = 12
GPIO.setup(PIR_PIN, GPIO.IN)

try:
    print "PIR Module Test (CTRL+C to exit)"
    time.sleep(1)
    print "Ready"

    while True:
        if GPIO.input(PIR_PIN):
            print "Motion Detected"
            os.system("sudo fswebcam test.jpg")
        time.sleep(1)

except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()
