import sys


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [
            [0 for column in range(vertices)]
            for row in range(vertices)
        ]

    def min_distance(self, dist, visited_set):
        min = sys.maxsize
        min_index = 0

        for v in range(self.V):
            if dist[v] < min and visited_set[v] == False:
                min = dist[v]
                min_index = v

        return min_index

    def print_sol(self, dist):
        print("Vertex Distance from Source")
        for node in range(self.V):
            print(f"{node} to {dist[node]}")

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        visited_set = [False] * self.V

        for cout in range(self.V):
            u = self.min_distance(dist, visited_set)

            visited_set[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and visited_set[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        self.print_sol(dist)


g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
		[4, 0, 8, 0, 0, 0, 0, 11, 0],
		[0, 8, 0, 7, 0, 4, 0, 0, 2],
		[0, 0, 7, 0, 9, 14, 0, 0, 0],
		[0, 0, 0, 9, 0, 10, 0, 0, 0],
		[0, 0, 4, 14, 10, 0, 2, 0, 0],
		[0, 0, 0, 0, 0, 2, 0, 1, 6],
		[8, 11, 0, 0, 0, 0, 1, 0, 7],
		[0, 0, 2, 0, 0, 0, 6, 7, 0]
		]

g.dijkstra(0)