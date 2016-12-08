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
valorFiltradoAceleracion = 0
valorFiltradoDireccion = 0

while True:
	valorAceleracion = arduinoJoystick.readline() #Lectura del serial aceleracion
	valorDireccion = arduinoJoystick.readline() #Lectura del serial direccion
	if constanteControl <= 19:
		# Estabilización de los datos leidos
		constanteControl = constanteControl + 1
		valorFiltradoAceleracion = valorFiltradoAceleracion + int(valorAceleracion)
		valorFiltradoDireccion = valorFiltradoDireccion + int(valorDireccion)
	else:
		# Revisión de información Recivida
		print('Aceleracion: ', int(valorFiltradoAceleracion / 20), '  Direccion: ', int(valorFiltradoDireccion / 20,)) 
		# Reset variable utilizadas
		constanteControl = 0
		valorFiltradoAceleracion = 0
		valorFiltradoDireccion = 0
		# Limpiamos el buffer
		arduinoJoystick.flush()
		arduinoJoystick.setDTR()
	