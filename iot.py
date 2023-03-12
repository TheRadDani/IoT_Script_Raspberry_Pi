#basadso en https://thingsboard.io/docs/user-guide/attributes/
from smbus2 import SMBus
import time
import sys
import paho.mqtt.client as paho  		    #mqtt library
import os
import json
import time
from datetime import datetime
import paho.mqtt.client as mqtt
bus = SMBus(1)
def main():  
    ACCESS_TOKEN='xx'                 #Token of your device
    broker="xx"   			    #host name
    port=0 					    #data listening port
    # Open i2c bus 1 and read one byte from address 80, offset 0
    def on_publish(client,userdata,result):             #create function for callback
        print("data published to thingsboard \n")
        pass
    client1= paho.Client("control1")                    #create client object
    client1.on_publish = on_publish                     #assign function to callback
    client1.username_pw_set(ACCESS_TOKEN)               #access token from thingsboard device
    client1.connect(broker,port,keepalive=60)           #establish connection

    while True:
       b = bus.read_byte_data(8, 0)
       if(b<20):
         payload="{"
         payload+="\"Fire\": YES"; 
         payload+="}"  
       else:
         payload="{"
         payload+="\"Fire\": NO"; 
         payload+="}"
       ret= client1.publish("v1/devices/me/telemetry",payload) #topic-v1/devices/me/telemetry
       print("Please check LATEST TELEMETRY field of your device")
       print(payload)
       time.sleep(1)
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Exiting')
        bus.close()
        sys.exit()
    except SystemExit:
        pass