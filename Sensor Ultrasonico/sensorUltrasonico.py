import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins
trig = 23
echo = 24

#entradas y salidas
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

#leer distancia del sensor
def detectar():
    GPIO.output(trig, False)
    time.sleep(2*10**-6) #2 microsegundos
    GPIO.output(trig, True)
    time.sleep(10*10**-6) #10 microsegundos
    GPIO.output(trig, False)

    #contar tiempo
    while GPIO.input(echo) == 0:
        start = time.time()
    while GPIO.input(echo) == 1:
        end = time.time()

    #duracion del pulso
    duracion = end-start

    #convertir a microsegundos
    #duracion = duracion*10**6

    #distacia en cm
    #medida = duracion/58

    distancia = (duracion * 34300)/2
    return str(distancia)


while True:
    distancia = detectar()
    print(distancia)
    time.sleep(0.5)

GPIO.cleanup() #limpiar GPIO
