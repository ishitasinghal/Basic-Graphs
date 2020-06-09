class Vertices:
    def __init__(self, graph_dict =None):
        if(graph is None):
            graph_dict = []
        self.graph_dict = graph_dict

    def vertice(self):
        return list(self.graph_dict.keys())

graph = {
    "a": ['b', 'c'],
     "b":  ['a'],
    "c": ['a', 'd'],
    "d":['d']

}
g1 = Vertices(graph)
print(g1.vertice())