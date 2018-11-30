import requests
import json
import time
from random import randint

import socket
import struct

# def get_ip_address(ifname):
#    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#    return socket.inet_ntoa(fcntl.ioctl(
#        s.fileno(),
#        0x8915,  # SIOCGIFADDR
#        struct.pack('256s', ifname[:15])
#    )[20:24])

#print(get_ip_address('en0'))
#print(get_ip_address('wlan0'))

####################################################################################################
# ''' please enter your alternate device ID and your alternate sensor ID and other values in the variables below

deviceId = 'd5c69c4ae0d1e168'  # the deviceAlternateId
sensorId = '6af6247b84ca4d3b'  # the sensorAlternateId
capabilityAlternateId = 'dht11'
ipCapabilityAlternateId = 'a2cff1720092814d'
tenant = 'https://b7c43a66-5b99-4e0d-921b-7d8c142a2ebf.eu10.cp.iot.sap/iot/gateway/rest/measures/'
####################################################################################################

postAddress = (tenant + deviceId)

print('Device ID: ', deviceId)
print('Sensor ID: ', sensorId)
print('Posting to:', postAddress)

# Initial values for temperature, humidity, light
temp = 50
hum = 82
light = 1000


bodyJson = {
    "capabilityAlternateId": ipCapabilityAlternateId,
    "sensorAlternateId": sensorId,
    "measures": [
        ["10.1.1.20"]
    ]
}

data = json.dumps(bodyJson)
headers = {'content-type': 'application/json'}
#r = requests.post(postAddress, data=data, headers=headers, cert=(
    #'dshop.pem', 'dshop_private_key.pem'), timeout=5)
#responseCode = r.status_code
#print(str(bodyJson))
#print("==> HTTP Response: %d" % responseCode)

for x in range (0,120000):

    bodyJson = {
        "capabilityAlternateId": capabilityAlternateId,
        "sensorAlternateId": sensorId,
        "measures": [
            [int(temp),int(hum)]
        ]
    }

    data = json.dumps(bodyJson)
    headers = {'content-type': 'application/json'}
    try:
      r = requests.post(postAddress, data=data, headers=headers, cert=(
          'dansensor-device_certificate.pem', 'dankey.pem'), timeout=5)
      responseCode = r.status_code
      print(str(bodyJson))
      print("==> HTTP Response: %d" % responseCode)
    except:
      print("Unable to reach server")
  
    if(x % 2 == 0):
        #temp = 60
        hum = 92
        light = 950
    else:
        #temp = 50
        hum = 82
        light = 1000


    temp += randint(1,7)-4

    if (temp <= 43):
      temp +=2
    if (temp >= 88):
      temp -=2
    print(temp)
    time.sleep(60)
