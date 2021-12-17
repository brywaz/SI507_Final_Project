import os
from networkx.readwrite import json_graph
from tqdm import tqdm
import json
import networkx as nx

'''
The purpose of this file is to take in the .json file created by wazbinski_507_finalproject_create_main_data.py, create a graph,
and save it for later use (in this case as a .json file)

'''


abs_path = os.path.dirname(os.path.abspath(__file__))

######################################################

##### LOADING IN SAVED JSON FILE CREATED in wazbinski_507_finalproject_create_main_data.py ######

######################################################
with open('main_2015_2020.json') as fjson:
    main_data = json.load(fjson)
fjson.close()

#########################################################################
###################### CREATE THE GRAPH  (2 Ways )##############
#########################################################################

class Vertex:

    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=1):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


##############################
## Making Graph like in class
##############################


## taking in dictionary in form game_id: [players]

# G = Graph()
# for game in main_data.keys():
#     G.addVertex(game)

# for game, players in main_data.items():
#     for player in players:
#         G.addEdge(game, player)

# for v in G:
#     for w in v.getConnections():
#         print("(%s, %s)" % (v.getId(), w.getId()))

'''
The above code shows that I am able to create a graph.
I was not able to implement a method from scratch to get the shortest graph
So I used networkx instead.

'''

#############################################
## Making Graph Networkx and Saving .gml file
#############################################

G = nx.Graph()
added_players = []

def add_games_and_players_to_graph(dict):
    for game, players in tqdm(dict.items()):
        G.add_node(game)
        for player in players:
            if player not in added_players:
                G.add_node(player)
                added_players.append(player)
            G.add_edge(game, player)


add_games_and_players_to_graph(main_data) ###<---- creating graph

out_graph = json_graph.node_link_data(G) ###<---- generating data for json format

###saving graph as .json 
f = open("graph_main_2015_2020.json", "w")
json.dump(out_graph, f)
f.close()

