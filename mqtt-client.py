import paho.mqtt.client as mqtt



def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

Ip = input("Kies host:")
Topic = input("Kies Topic:")
Port = input("Kies poort:")
client.connect(Ip, Port, 60)


Keuze = int(input("Wil je een bericht sturen? ja 1 of nee 2 "))
if Keuze == 1:
    bericht = input("schrijf bericht:")
    client.publish(Topic, bericht)


if Keuze == 2:
 exit()
