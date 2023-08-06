import paho.mqtt.client as mqtt
import subprocess

# MQTT broker configuration
broker_address = "localhost"  # Replace with your MQTT broker's address
broker_port = 1883  # Replace with the broker's port number

# Callback function when the client connects to the broker
def on_connect(client, userdata, flags, rc):
	if(rc == 0):
		print('\n[ Client connected successfully ]\n')
		
		#topic creation
		client.subscribe("#")
		print('[ Pubblication of # ]\n')
		print('[ Waiting for message ... ]\n')
		return
	elif(rc == 1):
		print('\n[ ERROR: Unacceptable protocol version ]')
	elif(rc == 2):
		print('\n[ ERROR: client identifier rejected ]')
	elif(rc == 3):
		print('\n[ ERROR: server unavailable ]')
	elif(rc == 4):
		print('\n[ ERROR: bad username or password ]')
	elif(rc == 5):
		print('\n[ ERROR: not authorized ]')
	
	exit() #error case

# Callback function when a message is received from the broker
def on_message(client, userdata, msg):
    print("Topic: " + msg.topic + ", Message: " + str(msg.payload.decode()))

try:
	print('\nSubscriber creating new topic and subscribe to it.\n')

	client = mqtt.Client(client_id="client_sub_attacker")
	client.on_connect = on_connect
	client.on_message = on_message

	client.connect(broker_address, broker_port)

	client.loop_forever()

except KeyboardInterrupt:
	client.disconnect()
	subprocess.call('clear', shell=True)
	print('[ Client disconnected successfully ]')

except ConnectionRefusedError:
	print('[ ERROR: connection refused ]')
