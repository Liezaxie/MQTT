# MQTT
My first MQTT project

## Getting Started
Deze handleiding laat je zien hoe je mijn MQTT project kan laten werken op jouw PC.

## Wat heb je nodig?
Je hebt een MQTT broker nodig om mijn subscriber of publisher te gebruiken.

## Installeren
Je hebt de paho-mqtt package nodig verder hoef je alleen de code te runnen.

## Testen en Gebruiken
Voor een makkelijke test kan je een eigen broker draaien op je PC bijv. mosquitto. 
Je kan dan bij host je eigen loopback adress invullen(127.0.0.1).
Subscriber.py is de subscriber.
mqtt-client.py is de publisher.

Er zijn een paar opties:
Kies Host: dit is het adress waar de broker aan verbonden is.
Kies Poort: dit is de poort waarover hij communiceerd standaard is dit 1883.
Kies Topic: Dit bepaald waaron je published of subscribed. Als je deze gaat testen moeten ze in beide codes gelijk zijn.

