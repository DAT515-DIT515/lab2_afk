import json
import sys
import networkx as nx
import graphviz as gv
TRAM_FILE = 'tramnetwork.json'

def readTramNetwork(tramfile=TRAM_FILE):
    
    with open(tramfile, 'r') as file:
        TramNetwork = json.load(file)
        return TramNetwork
    
Network = (readTramNetwork())
#print(len(Network["stops"]))
G = nx.Graph(Network["times"])
dot = gv.Graph( engine='dot')
for v in G.nodes():
        print(v)
        dot.node(str(v))
for (a,b) in G.edges():
        dot.edge(str(a),str(b))
        print(a,b)
dot.render('mygraph.gv', view=True)
#dot.view()
#print(G.edges)
