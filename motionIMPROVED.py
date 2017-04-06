import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

PIR_PIN = 12
GPIO.setup(PIR_PIN, GPIO.IN)

def MOTION(PIR_PIN):
    print "Motion Detected"

print "PIR Module Test (CTRL+C to exit)"
time.sleep(2)
print "Ready"

try:
   # use a GPIO interrupt function with call back to separate function
   # more efficient as program waits for GPIO event and not continually
   # listens to the pin
   # it works as edge detection, detecting changes in state low to high, high to low
   GPIO.add_event_detect(PIR_PIN, GPIO.RISING, callback=MOTION)
   # check for 1 instead of True
   # using 1 saves resources as it skips the variable check on True
   while 1:
        time.sleep(100)

except KeyboardInterrupt:
    print " Quit"
    GPIO.cleanup()
