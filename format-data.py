# Read from file and format

import json

def format(filename):
    filehandler = open(filename)
    players = json.load(filehandler)

    formatted_players = []

    for player in players:

        formatted_player = {}
        formatted_player['Player'] = str(player['Player'])
        formatted_player['Team'] = str(player['Team'])
        formatted_player['Pos'] = str(player['Pos'])
        formatted_player['Att'] = int(player['Att'])
        formatted_player['Att/G'] = float(player['Att/G'])
        formatted_player['Yds'] = float(str(player['Yds']).replace(',', ''))
        formatted_player['Avg'] = float(player['Avg'])
        formatted_player['Yds/G'] = float(player['Yds/G'])
        formatted_player['TD'] = int(player['TD'])
        formatted_player['Lng'] = int(str(player['Lng']).replace('T', ''))
        formatted_player['1st'] = int(player['1st'])
        formatted_player['1st%'] = float(player['1st%'])
        formatted_player['20+'] = int(player['20+'])
        formatted_player['40+'] = int(player['40+'])
        formatted_player['FUM'] = int(player['FUM'])

        formatted_players.append(formatted_player)

    with open('formatted-rushing.json', 'w') as outfile:
        json.dump(formatted_players, outfile)

    filehandler.close()

if __name__== "__main__":
    format("rushing.json");
