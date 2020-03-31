import paho.mqtt.client as mqtt



# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
   # Subscribe = input("Kies Subscriber")
   # client.subscribe(Subscribe)
   # print(Subscribe)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
# client.username_pw_set("paho", "Pa_Ho_Test5%")
client.on_connect = on_connect
client.on_message = on_message

Ip = input("Kies host:")
Topic = input("Kies Topic:")
client.connect(Ip, 1883, 60)


Keuze = int(input("Wil je een bericht sturen? ja 1 of nee 2 "))
if Keuze == 1:
    bericht = input("schrijf bericht:")
    client.publish(Topic, bericht)
    client.loop_forever()

if Keuze == 2:

    print("Oke dan.")
