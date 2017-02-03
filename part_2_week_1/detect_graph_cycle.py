from graph import Graph

class CycleDetector:
    def __init__(self, graph):
        self.graph = graph
        self.marked = {k: False for k in self.graph.adjc.keys()}
        ## a list is mutable
        self.found = [False]

    def detect(self):
        # for every key in graph
        for v in self.graph.adjc.keys():
            if not self.marked[v]:
                self._dfs(self.graph, v, self.found, v, self.marked)
            if self.found[0]:
                break
        return self.found[0]

    # pass down previous vertex as to not confused that one with the marked one
    def _dfs(self, G, u, found, prev, marked):
        if found[0]:     # - Stop dfs if cycle is found.
            return
        self.marked[u] = True     # - Mark node.
        for v in G.adj(u):    # - Check neighbors
            if self.marked[v] and v != prev: # - If neighbor is marked and not predecessor,
                found[0] = True   # then a cycle exists.
                return
            if not self.marked[v]:   # - Call dfs_visit recursively.
                self._dfs(G, v, found, u, marked)

if __name__ == "__main__":
    g = Graph((5,3), (6,2), (5,2), (4,1), (9,5), (6, 9), (1, 21))
    cd = CycleDetector(g)
    print cd.detect()
