#!/isan/bin/python

import datetime
from cli import cli
import sys

numArg = len(sys.argv)

if sys.argv[1] == "cancel":

        schedCLIjob = 'conf t ; no scheduler job name reloadinCommand5657373'
        schedCLItime = 'conf t ; no scheduler schedule name reloadinCommand5657373'
        print ("Canceling reload")


elif numArg &lt;= 3:
        try:

                requestTime = int(sys.argv[1])
        except:
                print ("Enter a integer for time")
                sys.exit() 

        now = datetime.datetime.now()
        actionTime = now + datetime.timedelta(minutes = requestTime)
        reloadTime = str(actionTime)
        reloadTime=reloadTime[11:-10]
        schedCLIjob = 'conf t ; scheduler job name reloadinCommand5657373 ; reload ; exit'
        schedCLItime = 'conf t ; scheduler schedule name reloadinCommand5657373 ; time start ' + reloadTime + ' repeat 48:00 ; end '

        if numArg == 3 and sys.argv[2] == "save".lower():
                cli('copy running-config startup-config')
                print ("Saving config before reload")

        print ("current time on the switch is " + str(now))
        print ("reload scheduled at " + reloadTime)


cli('conf t ; feature scheduler')

try:
        cli(schedCLIjob)
except:
        print ("operation failed..did you cancel a job that was not there?")
        sys.exit()

cli(schedCLItime)
print ("Operation success")