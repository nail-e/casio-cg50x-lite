"""
kruskal.py 
v1.0.1
nail_
"""

def createMatrix():
    matrix_width = int(input("Matrix Width: "))
    matrix_height = int(input("Matrix Height: "))
    matrix = [[0 for x in range(matrix_width)] for y in range(matrix_height)]
    return matrix, matrix_width, matrix_height

def inputMatrix(matrix, matrix_width, matrix_height):
    for i in range(0, matrix_height):
        for j in range(0, matrix_width):
            matrix[i][j] = int(input("Input for row {}, column {}: ".format(i, j)))

    return matrix

def kruskalSearch(matrix, matrix_width, matrix_height):
    edges = []

    for i in range(matrix_height):
        for j in range(matrix_width):
            if matrix[i][j] != 0:
                edges.append((i, j, matrix[i][j]))

    edges.sort(key=lambda edge: edge[2])  # Sort edges by weight
    parent = [i for i in range(max(matrix_height, matrix_width))]

    def find(u):
        if parent[u] == u:
            return u
        return find(parent[u])

    def union(u, v):
        nonlocal mst_weight
        nonlocal mst_edges

        root_u = find(u)
        root_v = find(v)
        if root_u != root_v:
            parent[root_u] = root_v
            mst_weight += w
            mst_edges.append((u, v, w))

    mst_edges = []
    mst_weight = 0

    for edge in edges:
        u, v, w = edge
        if find(u) != find(v):
            union(u, v)

    non_zero_indices_str = ['{}{}'.format(chr(65 + u), chr(65 + v)) for u, v, _ in mst_edges]
    print("Edges in MST:", ' '.join(non_zero_indices_str))
    print("Total MST weight:", mst_weight)

matrix, matrix_width, matrix_height = createMatrix()
matrix = inputMatrix(matrix, matrix_width, matrix_height)
kruskalSearch(matrix, matrix_width, matrix_height)



