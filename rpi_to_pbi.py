# Code to stream environment and movement data from Raspberry Pi 3 and Sense HAT to Power BI Service

import time
import requests
from datetime import datetime

# Calling SenseHat board with sensors

from sense_hat import SenseHat

sense = SenseHat()

#REST API endpoint, this will be given/displayed when you create an API streaming dataset in Power BI Service
#Will be of the format "https://api.powerbi.com/beta/<tenant ID>/<datasets>/<dataset ID>/row?key = <key ID>

REST_API_URL = ""

while True:
    #for x in range(0,5):

    # respective sensors on the SenseHat board
    
                t = sense.get_temperature()
                h = sense.get_humidity()
                p = sense.get_pressure()
                accel = sense.get_accelerometer_raw()
                y = accel['y']
                y = round(y,0)

                # Note the print format
                
                print ('{0:0.1f}*C {1:0.1f}% {2:0.1f}mb {3:0.1f}G'.format(t,h,p,y))
    
                now=datetime.strftime(datetime.now(), "%Y-%m-%dT%H:%M:%S%Z")
                print (now)

                # Data should be sent in the exact same format as highlighted in API!

                data = '[{{"timestamp":"{0}","temperature":"{1:0.1f}","humidity":"{2:0.1f}","pressure":"{3:0.1f}","acceleration":"{4:0.1f}"}}]'.format(now,t,h,p,y)
                req = requests.post(REST_API_URL,data)

                time.sleep(0)

