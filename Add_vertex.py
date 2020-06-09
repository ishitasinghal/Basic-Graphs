class Avertex:
    def __init__(self, graph_dict = None):
        if(graph_dict is None):
            graph_dict = []
        self.graph_dict = graph_dict

    def getv(self):
        return list(self.graph_dict.keys()) #to display the final added vertex

    def add(self, v):
        if(v not in self.graph_dict):
            self.graph_dict[v] = []

graph = {
    "a": ['b', 'c'],
     "b":  ['a'],
    "c": ['a', 'd'],
    "d":['d']
}
g1 = Avertex(graph)
g1.add("e")
g1.add("i")
print(g1.getv())