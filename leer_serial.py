import serial
ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=2) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
cadena = ""
vals =[]
while True:
	cadena = ser.readline()
	if cadena:
		print(cadena)
		vals.append(ser.readline())
