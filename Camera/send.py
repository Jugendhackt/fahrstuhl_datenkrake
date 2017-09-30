#!/usr/bin/python
import os
import subprocess


verpasst = ["Online"]
hostname = "google.com"
bot_key = "XXX"
chat_id = "XXX"



while True:
	if len(verpasst) > 0:
		for verpassten in verpasst:
			send(verpassten)


def send(text):
	if "verschwoerhaus" in subprocess.check_output("netsh wlan show interfaces"):	
		print("W-Lan Verfügbar")
		response = os.system("ping -c 1 " + hostname)
		if response == 0:
			print("WWW Verfügbar")
			os.system("curl -i -X GET https://api.telegram.org/bot" + bot_key + "/sendMessage?chat_id=" + chat_id + "&text=" + str(text))
		else:
			verpasst.append(text)
