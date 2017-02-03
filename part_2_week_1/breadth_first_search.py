from graph import Graph
import imp
modl = imp.load_source('queue', '../week_2/queue_with_array.py')
Queue = modl.Queue

class BFS:
    def __init__(self,graph, s):
        self.graph = graph
        self.marked = {}
        self.edgeTo = {}
        self.distances = {}
        self.s = s
        self._bfs(graph, s)

    def _bfs(self, graph, s):
        q = Queue()
        self.marked[s] = True
        q.enqueue(s)

        while q.size() != 0:
            # process vertex
            v = q.dequeue()
            # for all of its neigbhors
            for w in self.graph.adj(v):
                # unvisited vertices
                if w not in self.marked:
                    self.marked[w] = True
                    self.distances[w] = self.distances.get(v, 0) + 1
                    self.edgeTo[w] = v
                    q.enqueue(w)

    #shortest path from s to v
    def path(self, v):
        # if source vertex connects to vertex v it must be marked
        if self.marked[v] != True:
            return

        path = []
        x = v
        # while we trace back our steps on to source vertex
        while self.distances[x] != 1:
            # append vertex
            path.append(x)
            # go to parent vertex node back to source
            x = self.edgeTo[x]
        # lastly add source
        path.append(self.s)
        return path


if __name__ == "__main__":
    g = Graph((5,3), (6,2), (5,2), (4,1), (6, 9), (5,9))
    bfs = BFS(g, 5)
    print bfs.marked
    print bfs.edgeTo
    print bfs.distances
    print bfs.path(9)
