import json
import yaml
with open("favs.json", "r") as my_file:
    my = json.load(my_file)
#    print(my)
diction = {'name': 'Deshawn', 'movie': 'Kill Bill vol 2', 'ice cream': 'Vinilla', 'color': 'Beige'}
my.append(diction)
#print(my_fave)

with open("favs.yaml", "w") as our_file:    
    yaml.dump(my, our_file, sort_keys=False)
    #finnish = jason.dump(my_fav)
