import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#pins planta
pinRegado = 3 #led azul

#pins sensor de luz
pinLDR = 23 #sensor de luz

#pins sensor de movimiento
pinPIR = 4 #sensor de movimiento

#pins alarma
pinVerde = 8 
pinRojo = 7
pinBuzzer = 10
pinBoton = 9

#entradas y salidas
GPIO.setup(pinRegado, GPIO.OUT)
GPIO.setup(pinPIR, GPIO.IN)

GPIO.setup(pinVerde, GPIO.OUT)
GPIO.setup(pinRojo, GPIO.OUT)
GPIO.setup(pinBuzzer, GPIO.OUT)
GPIO.setup(pinBoton, GPIO.IN)

#metodos sensor de luz
def RCtime(RCpin):
    leer = 0
    GPIO.setup(RCpin, GPIO.OUT)
    GPIO.output(RCpin, False)
    time.sleep(0.1)

    GPIO.setup(RCpin, GPIO.IN)
    while (GPIO.input(RCpin) == False):
        leer += 1
    return leer

#metodos alarma
def sonarAlarma():
	for i in range(10):
		GPIO.output(pinBuzzer, True)
		time.sleep(0.1)
		GPIO.output(pinBuzzer, False)
		time.sleep(0.1)

def activarAlarma():
	for i in range(50):
		print(i)
		
		if GPIO.input(pinBoton) == True:
			GPIO.output(pinVerde, True)
			print("Alarma desactivada")
			time.sleep(0.1)
			break
		elif i >= 49:
			GPIO.output(pinRojo, True)
			print("Alarma activada")
			sonarAlarma()
		
		time.sleep(0.1)
	
	GPIO.output(pinVerde, False)
	GPIO.output(pinRojo, False)

while True:
	#detectar humedad
	humedad = random.randint(0, 1000)
	print("Humedad: ", humedad)
	
	if humedad < 10: #si la humedad es baja se riega la planta
		print("Regando planta")
		GPIO.output(pinRegado, True)
		time.sleep(5)
		GPIO.output(pinRegado, False)
	
	#detectar estado del dia
	estado = RCtime(pinLDR)
	
	if estado < 1000: #identificar si es de dia o de noche
		print("Es de dia ", estado)
		
	else:
		print("Es de noche", estado)
		
		#si es de noche se activa el sensor de movimiento
		if GPIO.input(pinPIR) == True: #identificar si existe movimiento
			print("Se detecto movimiento")
			
			#si se detecta movimiento se activa la alarma
			activarAlarma()
			
		else:
			print("No hay movimiento")
	
	time.sleep(0.5)
		

GPIO.cleanup() #limpiar GPIO
