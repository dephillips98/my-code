#!/usr/bin/env python3
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
user = input("Please pick NE, SE, or W\n")
option = input("do you want all, animals, or plants")

if user.lower() == "ne":
    if option.lower() == "all"
        for animals in farms[0]["agriculture"]:
            print(animals)
    if option.lower() == "animals"

if user.lower() == "w":
    for animals in farms[1]["agriculture"]:
        print(animals)
if user.lower() == "se":
    for animals in farms[2]["agriculture"]:
        print(animals)
