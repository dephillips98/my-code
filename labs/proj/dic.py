#!/usr/bin/env python3
iroh= {
        "Nation": "Fire",
        "Relatives": ["Zuko - Nephew", "Ozai - Brother", "Lu Ten - Son (Deceased)", "Azulon - Father", "Ilah - Mother"],
        "Bending element" : "Fire",
        "Voiced by" : ["Mako - books 1 & 2", "Greg Baldwin - book 3"],
        "Created by" : ["Michael Dante DiMartino", "Bryan Konietzko"]
        }
iroh["Trained by"] = "Twin dragons"
'''
Ask your user for input. Have them choose one of those keys you just printed. Save their selection as the variable choice.

Use the variable choice to access your dictionary and return the appropriate value.
'''
choice = input(f"Please choice a catigory: {iroh.keys()}")
print(f"the infomation on {choice} is {iroh[choice]}")
