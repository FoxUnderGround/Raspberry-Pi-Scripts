import os

import time



def measure_temp():

        temp = os.popen("vcgencmd measure_temp").readline()
        #os.popen("vcgencmd measure_temp  > /dev/ttyAMA0").readline()
        return (temp.replace("temp=",""))



while True:

        print(measure_temp())

        time.sleep(0.5)
