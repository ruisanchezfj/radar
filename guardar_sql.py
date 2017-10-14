#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:13:40 2017

@author: fran
"""
import deteccion_radar
import serial

ser = serial.Serial('/dev/ttyUSB0', 460800, timeout=2) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
cadena = ""

detec = deteccion_radar.deteccion_radar()
conex = detec.conectar_mysql('root','fran_prueba','asecnaus')

vals =[]
while True:
    
    #ser.flushOutput()
    cadena = detec.readline(ser,eol=b'\r')
    print cadena
    vals = cadena.split(",")
    print vals
    
    
    if len(vals) > 7:
        
        
        print("message type... " +vals[0])
        print("frame number in hexadecimal... " + vals[1])
        print("target number... " + vals[2])
        print("total number of targets in the current frame... " + vals[3])
        print("direcction the target is traveling... " + vals[4])
        print("target speed... " + vals[5])
        print("speed units... " + vals[6])
        print("target range... " + vals[7])
        print("target amplitude... " + vals[8])
        
        #detec.guardar_datos(conex,vals[1],vals[2],vals[3],vals[4],vals[5],vals[6],vals[7])
