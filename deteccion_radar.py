#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 13:13:40 2017

@author: fran
"""
from __future__ import print_function
import mysql.connector


class deteccion_radar:
    
    def conectar_mysql(self, usuario, basedatos, contrasena):
        cnx = mysql.connector.connect(user = usuario, database = basedatos, password = contrasena)
        return cnx
    
    def guardar_datos(self,cnx,frame_number,target_number, number_of_targets,direcction, speed, speed_unit, target_range):
        cursor = cnx.cursor()

        datos = (str(frame_number), str(target_number), str(number_of_targets),str(direcction), str(speed), str(speed_unit), str(target_range))
        add_datos =("insert into datos_radar ""(frame_number, target_number, number_of_target, direction, speed, speed_unit, target_range) ""VALUES (%s, %s, %s, %s, %s, %s, %s)")
        cursor.execute(add_datos,datos)
        emp_no = cursor.lastrowid
        cnx.commit()
        
    def readline(self,a_serial, eol=b'\n\n'):
        leneol = len(eol)
        line = bytearray()
        while True:
            c = a_serial.read(1)
            if c:
                line += c
                if line[-leneol:] == eol:
                    break
            else:
                break
        return bytes(line)