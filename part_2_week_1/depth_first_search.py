from graph import Graph

class DFS:
    def __init__(self,graph, s):
        self.graph = graph
        self.marked = {}
        self.edgeTo = {}
        self.s = s
        self._dfs(graph, s)

    # explicit stack with recursive call
    def _dfs(self,graph, v):
        # keep track of the browsed vertices
        self.marked[v] = True
        for w in self.graph.adj(v):
            if w not in self.marked:
                # mark the path of this vertex
                self.edgeTo[w] = v
                self._dfs(self.graph, w)

    def path(self, v):
        # if source vertex connects to vertex v it must be marked
        if self.marked[v] != True:
            return

        path = []
        x = v
        # while we trace back our steps on to source vertex
        while x != self.s:
            # append vertex
            path.append(x)
            # go to parent vertex node back to source
            x = self.edgeTo[x]
        # lastly add source
        path.append(self.s)
        return path

if __name__ == "__main__":
    g = Graph((5,3), (6,2), (5,2), (4,1), (6, 9))
    dfs = DFS(g, 5)
    print dfs.marked
    print dfs.edgeTo
    print dfs.path(9)
