import time

from RPi import GPIO

from lib.mqtt import MQTTClient


def any_message_received(client, userdata, message):
    m = message
    print(f'received {message.payload.decode("utf-8")}')
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18, GPIO.OUT)
    print("LED on")
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    print("LED off")
    GPIO.output(18, GPIO.LOW)


if __name__ == '__main__':
    mqtt_client = MQTTClient()
    # mqtt_client.pub('speed', 663)
    mqtt_client.sub(any_message_received, "base/relay/led1")
