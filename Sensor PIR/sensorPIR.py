import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins
pinPIR = 18
pinLed = 23

#entradas y salidas
GPIO.setup(pinLed, GPIO.OUT)
GPIO.setup(pinPIR, GPIO.IN)

while True:
    leer = GPIO.input(pinPIR)

    if leer == False:
        print("Intrusos")
        GPIO.output(pinLed, True)
        time.sleep(0.1)
    else:
        print("No hay instrusos")
        GPIO.output(pinLed, False)
        time.sleep(0.1)

    time.sleep(0.1)

GPIO.cleanup() #limpiar GPIO
