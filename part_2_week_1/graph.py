import imp
modl = imp.load_source('linked_list', '../week_2/linked_list.py')
LinkedList = modl.LinkedList

class Graph:
    def __init__(self, *args):
        self.V = 0
        self.E = 0
        self.adj = {}
        for v,w in args:
            self.addEdge(v, w)

    def addEdge(self, v, w):
        if v not in self.adj:
            self.adj[v] = LinkedList()
            self.V += 1
        if w not in self.adj:
            self.adj[w] = LinkedList()
            self.V += 1
        self.E += 1
        self.adj[v].add(w)
        self.adj[w].add(v)

    def adj(self, v):
        return self.adj[v]

if __name__ == "__main__":
    g = Graph((5,6), (6,2), (5,2), (4,1))
    for i in g.adj[5]:
        print "edge connected to", i
    print g.V
    print g.E
