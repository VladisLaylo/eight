import RPi.GPIO as gpio
import time

IN1 = 17
IN2 = 22
IN3 = 23
IN4 = 24

def init():
 gpio.setmode(gpio.BCM)
 gpio.setup(IN1, gpio.OUT)
 gpio.setup(IN2, gpio.OUT)
 gpio.setup(IN3, gpio.OUT)
 gpio.setup(IN4, gpio.OUT)

def forward(sec):
 init()
 gpio.output(IN1, True)
 gpio.output(IN2, False)
 gpio.output(IN3, True) 
 gpio.output(IN4, False)
 time.sleep(sec)

def reverse(sec):
 init()
 gpio.output(IN1, False)
 gpio.output(IN2, True)
 gpio.output(IN3, False) 
 gpio.output(IN4, True)
 time.sleep(sec)

try:
    print("forward")
    forward(4)
    print("reverse")
    reverse(2)
finally:
    gpio.cleanup()
