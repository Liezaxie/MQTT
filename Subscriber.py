import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    topic = input("Kies Topic:")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    print(str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
Host = input("Kies Host")
Port = input("Kies poort:")
client.connect(Host,Port, 60)


client.loop_forever()




