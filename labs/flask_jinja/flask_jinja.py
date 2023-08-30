#!/usr/bin/env python3
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_pokemon_info(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    data = response.json()
    poke_name = data["name"]
    poke_type = data["types"][0]["type"]["name"]
    return poke_name, poke_type

@app.route("/", methods=["GET", "POST"])
def index():
    poke_name = ""
    poke_type = ""

    if request.method == "POST":
        search_name = request.form.get("search_name")
        if search_name:
            poke_name, poke_type = get_pokemon_info(search_name)
    
    return render_template("poke.html", poke_name=poke_name, poke_type=poke_type)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

