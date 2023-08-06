import time
import json
import paho.mqtt.client as mqtt
import time
class IoTCoreMQTTClient(object):
    mqtt_bridge_hostname = 'localhost'
    mqtt_bridge_port = 1883

    def __init__(self, payload_size):
        self.payload_size = payload_size
        self.client = mqtt.Client(client_id="client_attacker")

    def connect_to_server(self):
        try:
            self.client.connect(self.mqtt_bridge_hostname, self.mqtt_bridge_port)
        except NameError as e:
            print("Failed to connect to server:", e)

    def disconnect_from_server(self):
        try:
            self.client.disconnect()
        except NameError as e:
            print("Failed to disconnect from server:", e)

    def generate_payload(self):
        payload = {}
        for i in range(1, self.payload_size+1):
            iStr = "%03d" % (i,)
            payload['field'+iStr] = 'payload_value_'+iStr
        return json.dumps(payload)

    def send_event(self, numberOfMsg):
        mqtt_topic = 'TestTopic'
        payload = self.generate_payload()
        try:
            self.client.reconnect()
            self.client.loop_start()
            for i in range(1, numberOfMsg+1):
                msgInfo = self.client.publish(mqtt_topic, payload, qos=1)
                msgInfo.wait_for_publish()
                time.sleep(1)
            self.client.disconnect()
        except ValueError as e:
            print("Failed to send event:", e)


client = IoTCoreMQTTClient(1024)

client.connect_to_server()
client.disconnect_from_server()

# client.send_event(1)
client.send_event(40)
# client.send_event(100)
# client.send_event(1000)