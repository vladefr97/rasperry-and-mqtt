from time import sleep
import os
from lib.mqtt import MQTTClient

mqtt = MQTTClient()
def sensor():
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            ds18b20 = i
    return ds18b20


def read(ds18b20):
    location = '/sys/bus/w1/devices/' + ds18b20 + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    tempdata = secondline.split(" ")[9]
    temp = float(tempdata[2:])
    celsuis = temp / 1000
    farenheit = (celsuis * 1.8) + 32

    return celsuis, farenheit


def loop(ds18b20):
    while True:
        if read(ds18b20) is not None:
            print("Current temperature: %0.3f C" % read(ds18b20)[0])


def kill():
    quit()


if __name__ == '__main__':
    try:
        serialNum = sensor()
        loop(serialNum)
    except KeyboardInterrupt:
        kill()
