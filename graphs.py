import networkx as nx

class Graph(nx.Graph):
    
    def __init__(self, start=None, values = None, directed=False):
        super().__init__(start)
        
        self._adjlist = {}
        if values is None:
            values = {}
        self._valuelist = values
        self._isdirected = directed
        
        # plus some code for building a graph from a ’start’ object
        # such as a list of edges
        # here are some of the public methods to implement
        
    def __len__(self):
         return self.number_of_nodes()
     
    def vertices(self):
         return self.nodes()

    def edges(self):
         return self.edges()
    
     
    def neighbors(self, n):
         return self.neighbors(n)

    def add_edge(self,a,b):
         return self.add_edge(a,b)
    
    
    def add_vertex(self,a):
         return self.add_node(a)
    
    
    
    
    def is_directed(self):
         pass
    
    def get_vertex_value(self, v):
         pass
    
    def set_vertex_value(self, v, x):
         pass
    

    def remove_edge(self,u, v):
         return self.remove_edge(u, v)
    
    
    def remove_vertices(self,n):
         return self.remove_node(n)
    


class WeightedGraph(Graph):
    def __init__(self, start=None):
         super().__init__(start)
         self.weights = {}
    
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