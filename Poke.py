import json

# Open and load the JSON file
with open('./PokeTCG.json', 'r',  encoding='utf-8-sig') as file:
    data = json.load(file)

# Print the loaded data (optional)
#print the name of all fighting type pokemon
""" found = False
for i in data['data']:
    if i['type']['fighting'] in ['data']:
        print(i['name'])
        found = True

    if not found:
        print('not found')
 """

#print all cards from the set "HeartGold & SoulSilver"

#print all cards where the averageSellPrice is greater than 1.5
found = False
for i in data['data']:
    if i['cardmarket']['prices']['averageSellPrice'] > 1.5:
        print(i['name'])
        found = True

    if not found:
        print('not found')

#i['averageSellPrice'] = int(i['averageSellPrice'])