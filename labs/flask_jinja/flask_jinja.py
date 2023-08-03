#!/usr/bin/env python3
from flask import Flask
from flask import render_template
import requests

def api():
    num = 1
    for num in range(1,151): 
        url = f"https://pokeapi.co/api/v2/pokemon-form/{num}"
        response = requests.get(url)
        data = response.json()
        poke_name = data["name"]
        poke_type = data["types"][0]["type"]["name"]
        poke_pic = data["sprites"]["front_default"]
        choose = input("search a pokemon by name:\n")
        if poke_name == choose.lower():
            return poke_name
            return poke_type
            return poke_pic
        else:
            print("try again")        



app = Flask(__name__)
@app.route("/<poke_name>")
def homepage(poke_name):
    api()
    return render_template("poke.html", poke_name = poke_name)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
