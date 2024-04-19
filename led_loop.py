import RPi.GPIO as GPIO
import time

PIN = 18
PIN2 = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN, GPIO.OUT)
GPIO.setup(PIN2, GPIO.OUT)

def led_on_off(time_asleep, pin):
    print("LED ON: ")
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(time_asleep)
    print("LED OFF")
    GPIO.output(pin, GPIO.LOW)
    time.sleep(time_asleep)

def led_alternating(time_asleep, pin1, pin2):
    GPIO.output(pin1, GPIO.HIGH)
    GPIO.output(pin2, GPIO.LOW)
    time.sleep(time_asleep)
    GPIO.output(pin1, GPIO.LOW)
    GPIO.output(pin2, GPIO.HIGH)
    time.sleep(time_asleep)
    

for i in range(20):
    print(i + 1)
    led_alternating(2, PIN, PIN2)

GPIO.output(PIN, GPIO.LOW)
GPIO.output(PIN2, GPIO.LOW)
