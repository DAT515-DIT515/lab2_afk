class Graph:
    def __init__(self, start=None, values = None, directed=False):
        self._adjlist = {}
        if values is None:
            values = {}
        self._valuelist = values
        self._isdirected = directed
        # plus some code for building a graph from a ’start’ object
        # such as a list of edges
        # here are some of the public methods to implement
    def vertices(self):
        pass
    def edges(self):
         pass
    def neighbours(self,v):
         pass
    def add_edge(self,a,b):
         pass
    def add_vertex(self,a):
         pass
    def is_directed(self):
         pass
    def get_vertex_value(self, v):
         pass
    def set_vertex_value(self, v, x):
         pass


class WeightedGraph(Graph):

    def set_weight(self, a, b, w):
         pass
    def get_weight(self, a, b):
        pass
    	# etc etc
    	# check the lab assignment for details


def  dijkstra(graph, source, cost=lambda u,v: 1):
    pass

def visualize(graph, view='dot', name='mygraph', nodecolors={}, engine='dot'):
    pass