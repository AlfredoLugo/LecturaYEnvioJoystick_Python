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
valorFiltradoSeleccion = 0
# valorAceleracionEntero = 0
# valorDireccionEntero = 0
# valorSeleccionEntero = 0

while True:
	valorAceleracion = arduinoJoystick.readline() #Lectura del serial aceleracion
	valorDireccion = arduinoJoystick.readline() #Lectura del serial direccion
	# valorSeleccion = arduinoJoystick.readline() #Lectura del serial seleccion de estado
	if constanteControl <= 19:
		# Estabilización de los datos leidos
		constanteControl = constanteControl + 1
		valorFiltradoAceleracion = valorFiltradoAceleracion + int(valorAceleracion)
		valorFiltradoDireccion = valorFiltradoDireccion + int(valorDireccion)
		# valorFiltradoSeleccion = valorFiltradoSeleccion + int(valorSeleccion)
	else:
		# Revisión de información Recivida
		print('Aceleracion: ', valorFiltradoAceleracion / 20, '  Direccion: ', valorFiltradoDireccion / 20,)# '  Seleccion: ', valorSeleccion / 20)
		# Reset variable utilizadas
		constanteControl = 0
		valorFiltradoAceleracion = 0
		valorFiltradoDireccion = 0
		ValorFiltradoSeleccion = 0
		# Limpiamos el buffer
		arduinoJoystick.flush()
		arduinoJoystick.setDTR()
	