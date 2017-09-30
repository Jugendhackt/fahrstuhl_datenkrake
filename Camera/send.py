#!/usr/bin/python
import os
import subprocess
from Preproc import predict


verpasst = ["Online"]
hostname = "google.com"
bot_key = "XXX"
chat_id = "XXX"



while True:
	takePicture()
	result = predict("weights.hd5", "picture.jpg")	
	send("Du bist im Stockwerk " + result + ".")

	if len(verpasst) > 0:
		for verpassten in verpasst:
			send(verpassten)


def send(text):
	if online():
		os.system("curl -i -X GET https://api.telegram.org/bot" + bot_key + "/sendMessage?chat_id=" + chat_id + "&text=" + str(text))
	else:
		verpasst.append(text)


def online():
	if "verschwoerhaus" in subprocess.check_output("netsh wlan show interfaces"):
                print("W-Lan Verfügbar")
                response = os.system("ping -c 1 " + hostname)
                if response == 1:
                        return True
		else:
			return False
	else:
		return False

def takePicture():
	os.system("raspistill -vf -hf -w 96 -h 96 -o picture.jpg")
