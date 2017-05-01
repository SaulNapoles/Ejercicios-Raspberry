import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pin leds
pinArray = [14,15,18,23,24,25]

#salidas
for pin in pinArray:
    GPIO.setup(pin, GPIO.OUT)

while True:

    for iteracion in range(2):
        for contador in range(5):
            GPIO.output(pinArray[contador], True)
            time.sleep(0.01)
            GPIO.output(pinArray[contador+1], True)
            time.sleep(0.01)
            GPIO.output(pinArray[contador], False)
            time.sleep(0.02)
        
        pinArray.reverse()


GPIO.cleanup() #limpiar GPIO
