class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def prim_mst(self):
        parent = [None] * self.V
        key = [float("inf")] * self.V
        key[0] = 0
        mst_set = [False] * self.V
        for _ in range(self.V):
            u = min((key[v], v) for v in range(self.V) if not mst_set[v])[1]
            mst_set[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and not mst_set[v] and self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        print("Edge \tWeight")
        for i in range(1, self.V):
            print(f"{parent[i]} - {i}\t{self.graph[i][parent[i]]}")
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 6)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 8)
g.add_edge(1, 4, 5)
print("Minimum Spanning Tree using Prim's Algorithm:")
g.prim_mst()
