import heapq

class Edge:
    def __init__(self, u, v, weight):
        self.u = u
        self.v = v
        self.weight = weight


def prim(vertices, edges):
    start_vertex = int(input("Enter the starting vertex: "))

    if start_vertex not in vertices:
        print(f"Vertex {start_vertex} not found among {vertices}.")
        return []

    graph = {v: [] for v in vertices}
    for edge in edges:
        graph[edge.u].append((edge.weight, edge.v))
        graph[edge.v].append((edge.weight, edge.u))

    visited = set()
    mst = []
    priority_queue = []

    visited.add(start_vertex)
    for weight, neighbor in graph[start_vertex]:
        heapq.heappush(priority_queue, (weight, start_vertex, neighbor))

    while len(mst) < len(vertices) - 1 and priority_queue:
        weight, u, v = heapq.heappop(priority_queue)

        if v not in visited:
            visited.add(v)
            mst.append(Edge(u, v, weight))
            print(f"Edge added: ({u}, {v}) with weight {weight}")

            for edge_weight, neighbor in graph[v]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_weight, v, neighbor))

    if len(mst) != len(vertices) - 1:
        print("The graph is not connected, MST found only for one component.")
    return mst


vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
edges = [
    Edge(1, 2, 1),
    Edge(1, 3, 6),
    Edge(1, 4, 3),
    Edge(2, 5, 3),
    Edge(2, 7, 2),
    Edge(5, 8, 4),
    Edge(5, 9, 2),
    Edge(8, 11, 7),
    Edge(3, 5, 7),
    Edge(3, 6, 5),
    Edge(6, 8, 7),
    Edge(6, 10, 3),
    Edge(9, 11, 5),
    Edge(4, 7, 4),
    Edge(7, 10, 4),
    Edge(7, 9, 1),
    Edge(4, 6, 2),
    Edge(10, 11, 4)
]

mst = prim(vertices, edges)

print("\nMinimum Spanning Tree:")
for edge in mst:
    print(f"({edge.u}, {edge.v}) with weight {edge.weight}")
