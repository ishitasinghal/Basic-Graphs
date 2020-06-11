class BFS:
    def __init__(self, graph_dict = None):
        if(graph_dict is None):
            graph_dict = []
        self.graph_dict = graph_dict

    def edge(self):
        return self.findedge()

    def add(self, e):
        e = set(e)
        (v1, v2)= tuple(e)
        if(v1 in self.graph_dict):
            self.graph_dict[v1].append(v2)
        else:
            self.graph_dict[v1] = [v2]

    def findedge(self):
        ename = []
        for v in self.graph_dict:
            for next in self.graph_dict[v]:
                if({next, v} not in ename):
                    ename.append({v, next})
        return ename

    def breadthfirstsearch(self, s):
        visited = [False] * (len(self.graph_dict))
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            s = queue.pop(0)
            print(s, end = " ")
            for i in self.graph_dict[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True



graph = {
    "a": ['b', 'c'],
     "b":  ['a'],
    "c": ['a', 'd'],
    "d":['d']
}
g1 = BFS(graph)
print(g1.edge())
g1.add({'a', 'e'})
print(g1.edge())

g1.breadthfirstsearch('a')
