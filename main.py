import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
#first wheel
GPIO.setup(18, GPIO.OUT)
GPIO.setup(14, GPIO.OUT)

#Second wheel
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)

#First wheel
GPIO.output(18, GPIO.HIGH)
GPIO.output(14, GPIO.LOW)
GPIO.output(23, GPIO.HIGH)
GPIO.output(24, GPIO.LOW)

print("ON")
time.sleep(5)
#first wheel
GPIO.output(18, GPIO.LOW)
GPIO.output(14, GPIO.HIGH)
#second wheel
GPIO.output(23, GPIO.LOW)
GPIO.output(24, GPIO.HIGH)
time.sleep(5)
#make sure everything is off
GPIO.output(24, GPIO.LOW)
GPIO.output(14, GPIO.LOW)
print("OFF")
