import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pin labels
pinr_forw = 14
pinr_backw = 18
pinl_forw = 23
pinl_backw = 24

#first wheel setup
GPIO.setup(pinr_forw, GPIO.OUT)
GPIO.setup(pinr_backw, GPIO.OUT)

#Second wheel setup
GPIO.setup(pinl_forw, GPIO.OUT)
GPIO.setup(pinl_backw, GPIO.OUT)

# moves the vehicle forward, input length in seconds
def forward(length):
    print("going forward")
    GPIO.output(pinr_forw, GPIO.HIGH)
    GPIO.output(pinl_forw, GPIO.HIGH)
    time.sleep(length)
    GPIO.output(pinr_forw, GPIO.LOW)
    GPIO.output(pinl_forw, GPIO.LOW)
    
# moves the vehicle backward, input length in seconds
def backward(length):
    print("going backward")
    GPIO.output(pinr_backw, GPIO.HIGH)
    GPIO.output(pinl_backw, GPIO.HIGH)
    time.sleep(length)
    GPIO.output(pinr_backw, GPIO.LOW)
    GPIO.output(pinl_backw, GPIO.LOW)

# Turns the vehicle right, input turn length in seconds
def turn_right(length):
    print("turning right")
    GPIO.output(pinr_forw, GPIO.HIGH)
    GPIO.output(pinr_backw, GPIO.LOW)
    time.sleep(length)
    GPIO.output(pinr_forw, GPIO.LOW)

# Turns the vehicle left, input turn length in seconds
def turn_left(length):
    print("turning left")
    GPIO.output(pinl_forw, GPIO.HIGH)
    GPIO.output(pinl_backw, GPIO.LOW)
    time.sleep(length)
    GPIO.output(pinl_forw, GPIO.LOW)
    
# Turns off all power to the wheels
def turn_off():
    GPIO.output(pinr_forw, GPIO.LOW)
    GPIO.output(pinr_backw, GPIO.LOW)
    GPIO.output(pinl_forw, GPIO.LOW)
    GPIO.output(pinl_backw, GPIO.LOW)
  
forward(3)
backward(3)  
turn_right(3)
turn_left(3)
turn_off()

    