from flask import Flask, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

PIN_R = 18
PIN_Y = 24

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_Y, GPIO.OUT)

@app.route("/led_on_r", methods=["POST"])
def led_on_r():
    print("Red LED on")
    GPIO.output(PIN_R, GPIO.HIGH)
    return "ok"

@app.route("/led_off_r", methods=["POST"])
def led_off_r():
    print("Red LED off")
    GPIO.output(PIN_R, GPIO.LOW)
    return "ok"

@app.route("/led_on_y", methods=["POST"])
def led_on_y():
    print("Yellow LED on")
    GPIO.output(PIN_Y, GPIO.HIGH)
    return "ok"

@app.route("/led_off_y", methods=["POST"])
def led_off_y():
    print("Yellow LED off")
    GPIO.output(PIN_Y, GPIO.LOW)
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("button.html", title="Button", name="Austin Windley")


