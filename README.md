# SI507_Final_Project
Final Project for SI507 Course

This project uses the networkx package for python (https://networkx.org/),
the tqdm package (https://tqdm.github.io/) and pandas (https://pandas.pydata.org/)


This project creates a network (graph) of MLB games played from 2015-2020 and any player that batted, pitched, or played catcher in that game.

The raw data is in the project_data directory.

The json files graph_main_2015_2020.json and main_2015_2020.json are generated from the .py files and included as samples. If you run ...create_main_data.py, it will create main_2015_2020.json. If you run ...create_graph.py, it will create graph_main_2015_2020.json

With graph_main_2015_2020.json already created, you can simply run ...read_graph.py and follow the prompts. 

If you want to create everything again, the workflow is as follows:

Run ...create_main_data.py
Run ...create_graph.py
Run ...read_graph.py

...create_main_data.py takes in the .csv and .txt files of the raw data, creates a dictionary in the form:

game_id: [players]

and generates a main .json file to be used by ...create_graph.py 

...create_graph.py reads in the .json file, creates a graph, and saves the graph in .json format.

...read_graph.py reads in the .json graph file and then prompts the user to input the names of two MLB players that have played in a game between 2015 and 2020. It then shows the "Bacon Score," indicating how closely linked the players are. A Bacon Score of 1 means they've played in a game together. A Bacon Score of 2 means they did not play directly in a game together, but rather played with another player that has played in games with both of them. The results are in the format:

Player1, gameID, Player2

The gameID format is:

First 3 letters: Abbreviation of home team
Next 4 digits: Year game was played
Next 2 digits: Month game was played
Next 2 digits: Day game was played
Last digit: If game was part of double-header (0 indicates not a double-header)

Example:

MIN201505160

Game Played on 05/16/2015 in Minnesota
