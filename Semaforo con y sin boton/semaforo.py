import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins
ledVerde = 14
ledAmarillo = 15
ledRojo = 18
boton = 11

ledPeaton = 23
activado = False

#entradas y salidas
GPIO.setup(ledVerde, GPIO.OUT)
GPIO.setup(ledAmarillo, GPIO.OUT)
GPIO.setup(ledRojo, GPIO.OUT)
GPIO.setup(boton, GPIO.IN)
GPIO.setup(ledPeaton, GPIO.OUT)

#metodos
def pasandoPeatones():
    parpadear(ledVerde)
    encender(ledAmarillo)
    GPIO.output(ledRojo, True)
    time.sleep(0.1)
    print("PASANDO PEATONES")
    parpadear(ledPeaton)
    GPIO.output(ledRojo, False)


def encender(led):
    GPIO.output(led, True)
    time.sleep(2)
    GPIO.output(led, False)


def parpadear(led):
    for i in range(5):
        GPIO.output(led, True)
        time.sleep(0.4)
        GPIO.output(led, False)
        time.sleep(0.4)


#loop
while True:

    GPIO.output(ledVerde, True)

    for i in range(40):  #esperar 4 segundos a ler un boton
        if GPIO.input(boton) == True:
            pasandoPeatones()
            activado = True
            break
        time.sleep(0.1)

    if activado == False:
        pasandoPeatones()

    activado = False

GPIO.cleanup() #limpiar GPIO
