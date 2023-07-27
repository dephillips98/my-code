#!/usr/bin/env python3
import requests

url = "http://api.open-notify.org/iss-now.json"
url_responce = requests.get(url)
api = url_responce.json()
print(api["iss_position"]["latitude"]," : ",api["iss_position"]["longitude"])
