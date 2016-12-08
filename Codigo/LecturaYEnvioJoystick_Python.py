# Se agrega la libreria PySerial
import serial 
# Se agrega la libreria time para poder dar un tiempo para que se abra el puerto serial
import time

# Instancia del puerto de lectura y tiempo maximo de espera
arduinoJoystick = serial.Serial('COM4', 250000, timeout = 2) 
time.sleep(1) #Tiempo para la la apertura del puerto serial
arduinoJoystick.flush()
arduinoJoystick.setDTR()

constanteControl = 0
valorFiltrado = 0

while True:
	valorAceleracion = arduinoJoystick.readline() #Lectura del serial 
	valorAceleracionEntero = int(valorAceleracion) #Converción a valor enetero
	if constanteControl <= 19:
		# Estabilización de los datos leidos
		constanteControl = constanteControl + 1
		valorFiltrado = valorFiltrado + valorAceleracionEntero
	else:
		# Revisión de información Recivida
		print(int(valorFiltrado / 20))
		# Reset variable utilizadas
		constanteControl = 0
		valorFiltrado = 0
		# Limpiamos el buffer
		arduinoJoystick.flush()
		arduinoJoystick.setDTR()
	