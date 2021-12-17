import os
import json
import pandas as pd
from tqdm import tqdm


'''
The purpose of this file is to take in the raw .csv files and create a .json file
that will be used to create the graph in a separate program.

'''

abs_path = os.path.dirname(os.path.abspath(__file__))

events_path_2015 = os.path.join(abs_path, 'project_data/2015_events.csv')
events_path_2016 = os.path.join(abs_path, 'project_data/2016_events.csv')
events_path_2017 = os.path.join(abs_path, 'project_data/2017_events.csv')
events_path_2018 = os.path.join(abs_path, 'project_data/2018_events.csv')
events_path_2019 = os.path.join(abs_path, 'project_data/2019_events.csv')
events_path_2020 = os.path.join(abs_path, 'project_data/2020_events.csv')

players_path = os.path.join(abs_path, 'project_data/BIOFILE.txt')

#####################################################################
############### PART 1 - LOAD IN DATA ################################
######################################################################

### !!! First section below is initial loading of data, creating dicitonaries
### and saving to json. It is commented out once json's created, since I then
### load in the json files to create necessary dictionaries. 

### Create dataframes to eventually merge
players_raw = pd.read_csv(players_path) 
events_2015 = pd.read_csv(events_path_2015)
events_2016 = pd.read_csv(events_path_2016)
events_2017 = pd.read_csv(events_path_2017)
events_2018 = pd.read_csv(events_path_2018)
events_2019 = pd.read_csv(events_path_2019)
events_2020 = pd.read_csv(events_path_2020)


## Create dataframe of only necessary player info
players = players_raw[['PLAYERID', 'LAST', 'NICKNAME']].copy()
events_all = pd.concat([events_2015, events_2016, events_2017, events_2018, events_2019, events_2020])

# ## Convert to dictionaries
players_dict = players.to_dict(orient='records')
events_dict_all = events_all.to_dict(orient='records')

### Create Functions to get workable dictionaries
def make_dict_players(player_data):
    '''
    Takes in list of dictionaries of {playerID, LastName, FirstName}
    Returns dictionary of {playerID: FirstName LastName}
    
    '''
    player_names = {}
    for player in player_data:
        key = player['PLAYERID']
        name = f"{player['NICKNAME']} {player['LAST']}"
        player_names[key]= name
    return player_names


def make_dict_games(game_data):
    '''
    Takes in list of dictionaries of {game_id, batterID, pitcherID, catcherID}
    Returns dictionary of {game_id: [playerIDs]}

    '''
    games_all = {}
    for game in tqdm(game_data):
        key = game['game_id']
        players = [game['batter'], game['pitcher'], game['catcher']]
        if key in games_all.keys():
            for player in players:
                games_all[key].append(player)
        else:
            games_all[key]= players

    for key, value in games_all.items():
        value_set = set(value)
        back_to_list = list(value_set)
        games_all[key]= back_to_list

    return games_all


## Create Main Dictionary ###

def get_main_dict(player_dict, game_dict):
    '''
    Takes in player and game dictionaries
    Converts player ID's to player names
    Returns dictionary in the form {gameID: [Player Names]}

    '''
    main_dict = {}
    for gameID, playerIDs in game_dict.items():
        playersByName = []
        for playerID in playerIDs:
            playerName = player_dict[playerID]
            playersByName.append(playerName)
        main_dict[gameID]=playersByName

    return main_dict

A = make_dict_players(players_dict)
B = make_dict_games(events_dict_all)
main_2015_2020 = get_main_dict(A, B)

### Store as Json ####
f = open("main_2015_2020.json", "w")
json.dump(main_2015_2020, f)
f.close()






