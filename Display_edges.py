class Edges:
    def __init__(self, graph_dict =None):
        if(graph is None):
            graph_dict = []
        self.graph_dict = graph_dict

    def findedge(self):
        ename = []
        for v in self.graph_dict:
            for next in self.graph_dict[v]:
                if({next, v} not in ename):
                    ename.append({v, next})
        return ename
    def edge(self):
        return self.findedge()

graph = {
    "a": ['b', 'c'],
     "b":  ['a'],
    "c": ['a', 'd'],
    "d":['d']
}
g1 = Edges(graph)
print(g1.edge())