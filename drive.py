import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  # Switching to BCM mode

print("0")


MOTOR1_IN1 = 17 # 29 # Motor 1 (Driver A) PURPLR
MOTOR1_IN2 = 22 # 31 # BLUE

MOTOR2_IN1 = 23 # 32 # Motor 2 (Driver A) ORANGE
MOTOR2_IN2 = 23 # 33 # GRAY

# MOTOR3_IN1 = 5   # Motor 3 (Driver B)
# MOTOR3_IN2 = 6
# MOTOR4_IN1 = 13  # Motor 4 (Driver B)
# MOTOR4_IN2 = 19

# GPIO.setup(27, GPIO.OUT) # BROWN
# GPIO.setup(22, GPIO.OUT) # PURPLE
# GPIO.setup(24, GPIO.OUT) # BLUE
# GPIO.setup(25, GPIO.OUT) # LIGHT BROWN

GPIO.setup(MOTOR1_IN1, GPIO.OUT) # BROWN
GPIO.setup(MOTOR1_IN2, GPIO.OUT) # BLUE

GPIO.setup(MOTOR2_IN1, GPIO.OUT) # ORANGE
GPIO.setup(MOTOR2_IN2, GPIO.OUT) # GRAY

print("1")
GPIO.output(MOTOR1_IN1, GPIO.HIGH) # BROWN
time.sleep(3)
GPIO.output(MOTOR1_IN2, GPIO.LOW) # PURPLE

print("2")

GPIO.output(MOTOR2_IN1, GPIO.HIGH) # BROWN
time.sleep(3)
GPIO.output(MOTOR2_IN2, GPIO.LOW) # PURPLE

print("DONE")

GPIO.cleanup()  # Cleanup GPIO settings to prevent pin lock

