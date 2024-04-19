import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18, GPIO.OUT)

GPIO.output(18, GPIO.HIGH)
print("ON")
time.sleep(10)
GPIO.output(18, GPIO.LOW)
print("OFF")
