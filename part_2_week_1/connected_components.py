from graph import Graph

class ConnectedComponents:
    def __init__(self,graph):
        self.graph = graph
        self.marked = {k: False for k in self.graph.adjc.keys()}
        self.id = {k: None for k in self.graph.adjc.keys()}
        self.count = 0
        self.cc(self.graph)

    def cc(self, graph):
        for w in self.graph.adjc.keys():
            if self.marked[w] is False:
                self._dfs(self.graph, w)
                self.count += 1

    # explicit stack with recursive call
    def _dfs(self,graph, v):
        # keep track of the browsed vertices
        self.marked[v] = True
        self.id[v] = self.count
        for w in self.graph.adj(v):
            # important!!! only look into if it's not marked already
            if not self.marked[w]:
                # mark the path of this vertex
                self._dfs(self.graph, w)

if __name__ == "__main__":
    g = Graph((5,3), (6,2), (5,2), (4,1), (6, 9), (1, 21))
    cc = ConnectedComponents(g)
    print cc.id
