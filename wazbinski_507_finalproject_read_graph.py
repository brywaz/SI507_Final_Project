import os
import networkx as nx
from networkx.readwrite import json_graph
import json

'''
The purpose of this file is to take in the graph .json file from wazbinski_507_finalproject_create_graph.py, prompt the user to input
players, and returns their "Bacon Score"

'''

abs_path = os.path.dirname(os.path.abspath(__file__))

##########################################################
### LOADING IN GRAPH .gml FILE ###########################
#########################################################

print(f"\nLoading graph file...")

G = json_graph.node_link_graph(json.load(open('graph_main_2015_2020.json'))) ### <--- Loading in json file



### GET SHORTEST PATH FUNCTION ######

def get_shortest_path(graph, source, target):
    '''
    takes in a graph, source (string), and target(string)
    returns the shortest path from the source to the target (Bacon score)
    
    '''

    path = nx.shortest_path(graph,source=source,target=target)
    print('{0} has a Bacon score of: {1}'.format(source, int(len(path)/2)))
    print(path)


#########################################################
#########################################################

if __name__ == "__main__":

#########################################################
######### User Input #####################################
#########################################################
    count = 0
    if count == 0:
        source_player = input(f"\n**--**--**-- The 6 Degrees of Kevin Bacon: MLB Edition! --**--**--**\n\n"
                            f"How many degrees of separation (Bacon Score) are there between any MLB Players?\n"
                            f"Please enter the name of an MLB player (FirstName LastName) or type 'EXIT' to quit: ")
        if source_player == 'exit'.upper():
            print(f'\nCIAO!')
            exit()
        else:
            target_player = input(f"\nPlease enter the name of another player (FirstName LastName): ")
            get_shortest_path(G, source_player, target_player)
            print("Example: MIN201505160 = Game Played on 05/16/2015 in Minnesota")
            count +=1
    while count >=1:
        check_proceed = input(f"\nSearch Again?: ")
        if check_proceed.lower() == 'no':
            print(f'\nCIAO!')
            exit()
        else:
            source_player = input(f"Please enter the name of an MLB player (FirstName LastName) or type 'EXIT' to quit: ")
            if source_player == 'exit'.upper():
                print(f'\nCIAO!')
                exit()
            else:
                target_player = input(f"\nPlease enter the name of another player (FirstName LastName): ")
                get_shortest_path(G, source_player, target_player)




