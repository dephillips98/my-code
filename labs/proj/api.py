#!/usr/bin/env python3
import requests

url = "https://pokeapi.co/api/v2/pokemon"

http_url = requests.get(url)
results = http_url.json()
#num = 0
pokemon = results['results']
#print(results["results"][0]["name"])
#print(pokemon)
def choice():
    for num in range(2,20,3):
        type_dict = {pokemon[num]["name"]}
        print(type_dict)

    

    # TO DO
    # prompt the user to choose three different pokemon
    # send a .get() to all three of those pokemon
    # process the response
    # display what their type is

choice()
