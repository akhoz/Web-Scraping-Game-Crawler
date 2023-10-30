import json
import os
current_directory = os.path.dirname(os.path.realpath(__file__))

with open(f'{current_directory}/spiders/data/g2a.json', 'r') as file:
    g2a = json.load(file)

with open(f'{current_directory}/spiders/data/ig.json', 'r') as file:
    ig = json.load(file)

with open(f'{current_directory}/spiders/data/ps.json', 'r') as file:
    ps = json.load(file)

with open(f'{current_directory}/spiders/data/hltb.json', 'r') as file:
    hltb = json.load(file)

data_dict = {}
merged_data = g2a + ig + ps
for game in merged_data:
    game_name = game['Name']
    game_price = float(game['Price'])

    if game_name in data_dict:
        if game_price < float(data_dict[game_name]['Price']):
            data_dict[game_name] = game
    else:
        data_dict[game_name] = game

with open(f'{current_directory}/spiders/data/metacritic.json', 'r') as file:
    mc = json.load(file)
#print(mc)
for game in mc:
    if game['Name'] in data_dict:
        data_dict[game['Name']]['Metacritic'] = game['Metascore']

for game in hltb:
    if game['Game Name'] in data_dict:
        print(game['Game Name'])
        #print(game['Completionist Hours'])
        data_dict[game['Game Name']]['Completionist hours'] = game['Completionist Hours']
print(data_dict)