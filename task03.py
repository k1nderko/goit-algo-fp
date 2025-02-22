import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        """ Додає орієнтоване ребро у граф (u -> v) з вагою """
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []  
        self.graph[u].append((v, weight))

    def dijkstra(self, start):
        """ Алгоритм Дейкстри для знаходження найкоротших шляхів """
        min_heap = []
        heapq.heappush(min_heap, (0, start))  
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0

        while min_heap:
            current_distance, current_vertex = heapq.heappop(min_heap)

            if current_distance > distances[current_vertex]:
                continue  

            for neighbor, weight in self.graph[current_vertex]:
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Приклад
g = Graph()
g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 3)

start_vertex = 'A'
shortest_paths = g.dijkstra(start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in shortest_paths.items():
    print(f"{vertex}: {distance}")