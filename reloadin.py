#!/isan/bin/python

import datetime
from cli import cli
import sys

numArg = len(sys.argv)

if sys.argv[1] == "Cancelar":

        schedCLIjob = 'conf t ; no scheduler job name reloadinCommand5657373'
        schedCLItime = 'conf t ; no scheduler schedule name reloadinCommand5657373'
        print ("Cancelando reinicio")


elif numArg &lt;= 3:
        try:

                requestTime = int(sys.argv[1])
        except:
                print ("Introduzca un número entero para el tiempo")
                sys.exit() 

        now = datetime.datetime.now()
        actionTime = now + datetime.timedelta(minutes = requestTime)
        reloadTime = str(actionTime)
        reloadTime=reloadTime[11:-10]
        schedCLIjob = 'conf t ; scheduler job name reloadinCommand5657373 ; reload ; exit'
        schedCLItime = 'conf t ; scheduler schedule name reloadinCommand5657373 ; time start ' + reloadTime + ' repeat 48:00 ; end '
"""
        if numArg == 3 and sys.argv[2] == "save".lower():
                cli('copy r s')
                print ("Guardar configuración antes de recargar")

"""
        if numArg == 3 and sys.argv[2] == "save".lower():
                cli('copy running-config startup-config')
                print ("Guardar configuración antes de recargar")

        print ("La hora actual del switch es: " + str(now))
        print ("Reinicio programado en: " + reloadTime)


cli('conf t ; feature scheduler')

try:
        cli(schedCLIjob)
except:
        print ("la operación falló... ¿canceló un trabajo que no estaba allí?")
        sys.exit()

cli(schedCLItime)
print ("Operación exitosa")
