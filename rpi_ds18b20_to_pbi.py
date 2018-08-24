# Program to stream environment and movement data from Raspberry Pi 3 and ds18b20 to Power BI Service

import time
import os
import glob
import requests
from datetime import datetime

# Calling SenseHat board with sensors

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

# Initialize
I = 0
# Final count
F = 10000 
# Inout to time.sleep function
C = 0

while I <= F:

    file = open('/sys/bus/w1/devices/"your device number: typically starts with 28-...Note, dont need quotes"/w1_slave')
    filecontent = file.read()
    file.close()


    stringvalue = filecontent.split("\n")[1].split(" ")[9]
    t = float(stringvalue[2:]) / 1000


    #REST API endpoint, this will be given/displayed when you create an API streaming dataset in Power BI Service
    #Will be of the format "https://api.powerbi.com/beta/<tenant ID>/<datasets>/<dataset ID>/row?key = <key ID>

    REST_API_URL = "Input here & keep the quotes"


    print (t)                
    #print ('{0:0.1f}*C'.format(t)
    
    now=datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
    print (now)

    # Data should be sent in the exact same format as highlighted in API!

    data = '[{{"timestamp":"{0}","temperature":"{1:0.1f}"}}]'.format(now,t)
    req = requests.post(REST_API_URL,data)

    time.sleep(C)
    I = I + 1

