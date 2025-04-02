import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BCM)
pins = [17, 22, 23, 24]
for pin in pins:
    gpio.setup(pin, gpio.OUT)

try:
    for pin in pins:
        print(f"Activating GPIO {pin}")
        gpio.output(pin, True)  # Turn on
        time.sleep(2)
        gpio.output(pin, False)  # Turn off
finally:
    gpio.cleanup()
