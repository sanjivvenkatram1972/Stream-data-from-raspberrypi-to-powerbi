# Program to stream environment and movement data from Raspberry Pi 3 and ds18b20 to Power BI Service

import time
import os
import glob
import requests
from datetime import datetime

# Calling SenseHat board with sensors

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

I = 0
F = 10000 
C = 0

while I <= F:

    file = open('/sys/bus/w1/devices/28-0416c4e2ecff/w1_slave')
    filecontent = file.read()
    file.close()


    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    t = float(stringvalue[2:]) / 1000


    #REST API endpoint, this will be given/displayed when you create an API streaming dataset in Power BI Service
    #Will be of the format "https://api.powerbi.com/beta/<tenant ID>/<datasets>/<dataset ID>/row?key = <key ID>

    REST_API_URL = "https://api.powerbi.com/beta/4d690ea3-a04b-43bc-bffe-0423efe49b0e/datasets/3f672732-0056-4395-90fa-195551fa3277/rows?key=Loa9zSGoCE5HfjPvuwMKWR4c6VHFLIf8CceQUxnlrQVQZobHU2IcLxVOXsc3haEdkaSC0JCZIR%2F1Ftc0i8qKvQ%3D%3D"


    print (t)                
    #print ('{0:0.1f}*C'.format(t)
    
    now=datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
    print (now)

    # Data should be sent in the exact same format as highlighted in API!

    data = '[{{"timestamp":"{0}","temperature":"{1:0.1f}"}}]'.format(now,t)
    req = requests.post(REST_API_URL,data)

    time.sleep(C)
    I = I + 1

