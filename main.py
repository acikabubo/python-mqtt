import os
import paho.mqtt.client as mqtt


# Define event callbacks

def on_connect(client, userdata, rc):
    if rc == 0:
        print("Connected successfully.")
    else:
        print("Connection failed. rc= " + str(rc))


def on_publish(client, userdata, mid):
    print("Message " + str(mid) + " published.")


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribe with mid " + str(mid) + " received.")


def on_message(client, userdata, msg):
    print("Message received on topic " + msg.topic + " with QoS " + str(msg.qos) + " and payload " + msg.payload)

mqttclient = mqtt.Client()

# Assign event callbacks
mqttclient.on_connect = on_connect
mqttclient.on_publish = on_publish
mqttclient.on_subscribe = on_subscribe
mqttclient.on_message = on_message

# Connect
mqttclient.username_pw_set('acikabubo@gmail.com', os.environ['PS'])
mqttclient.connect('mqtt.dioty.co', 1883)

# Start subscription
mqttclient.subscribe("/acikabubo@gmail.com/proba")
mqttclient.subscribe("/acikabubo@gmail.com/slider")

# Publish a message
mqttclient.publish("/acikabubo@gmail.com/", "Hello World Message!")

# Loop; exit on error
rc = 0
while rc == 0:
    mqttclient.loop()
    # print("rc: " + str(rc))
