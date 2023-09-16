class Kruskal():
    def __init__(self):
        self.matrix_width = 0
        self.matrix_height = 0
        self.matrix = None

        self.mst_edges = []
        self.mst_weight = 0

    def createMatrix(self):
        self.matrix_width = int(input("Matrix Width: "))
        self.matrix_height = int(input("Matrix Height: "))
        self.matrix = [[0 for x in range(self.matrix_width)] for y in range(self.matrix_height)]

    def inputMatrix(self):
        for i in range(0, self.matrix_width):
            for j in range(0, self.matrix_height):
                self.matrix[j][i] = int(input(f"Input for row {j}, column {i}: " ))
        
        return self.matrix

    def kruskalSearch(self):
        edges = []

        for i in range(self.matrix_height):
            for j in range(self.matrix_width):
                if self.matrix[i][j] != 0:
                    edges.append((i, j, self.matrix[i][j]))

        edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
        parent = [i for i in range(self.matrix_height)]

        def find(u):
            if parent[u] == u:
                return u
            return find(parent[u])

        def union(u, v):
            root_u = find(u)
            root_v = find(v)
            if root_u != root_v:
                parent[root_u] = root_v
                self.mst_weight += w
                self.mst_edges.append((u, v, w))

        for edge in edges:
            u, v, w = edge
            if find(u) != find(v):
                union(u, v)

        non_zero_indices_str = [f"{chr(65 + u)}{chr(65 + v)}" for u, v, _ in self.mst_edges]
        print(f"Edges in MST: {' '.join(non_zero_indices_str)}")
        print(f"Total MST weight: {self.mst_weight}")


kruskal = Kruskal()
kruskal.createMatrix()
kruskal.inputMatrix()
kruskal.kruskalSearch()
