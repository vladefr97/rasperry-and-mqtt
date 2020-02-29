import sys

import paho.mqtt.subscribe as subscribe
import paho.mqtt.publish as publish

mqtt_cred = {
    "hostname": "sandbox.rightech.io",
    "port": 1883,
    "client_id": "model_1"

}


class MQTTClient:

    def __init__(self, host=mqtt_cred['hostname'], port=mqtt_cred['port'], client_id=mqtt_cred['client_id']) -> None:
        self.host = host
        self.port = port
        self.client_id = client_id
        # self.auth = auth

    def pub(self, topic, msg, retained=False):
        print("Connecting {}".format(mqtt_cred["hostname"]))
        publish.single(topic, msg, hostname=self.host,
                       port=self.port, client_id=self.client_id, retain=retained)

    def sub(self, callback_function, topic, wait=False):
        subscribe.callback(callback_function, topic, hostname=self.host, port=self.port, client_id=self.client_id, )
