import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v, weight):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append((v, weight))
        self.graph[v].append((u, weight))  # Karena graph undirected

    def dijkstra(self, start, end):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, node)
        previous_nodes = {node: None for node in self.graph}

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_node
                    heapq.heappush(priority_queue, (distance, neighbor))

        # Rekonstruksi jalur
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous_nodes[current]
        path.reverse()

        return path, distances[end]

    def reachable_cities(self, start):
        distances = {node: float('inf') for node in self.graph}
        distances[start] = 0
        priority_queue = [(0, start)]  # (distance, node)

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            for neighbor, weight in self.graph[current_node]:
                distance = current_distance + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
        
        # Sort berdasarkan jarak
        reachable = sorted(distances.items(), key=lambda x: x[1])
        return reachable

    def display(self):
        for city, neighbors in self.graph.items():
            connections = ', '.join([f"{neighbor}({weight})" for neighbor, weight in neighbors])
            print(f"{city} -> {connections}")

g = Graph()
edges = [
    ("A", "B", 4), ("A", "C", 2), ("B", "C", 1),
    ("B", "D", 5), ("C", "D", 8), ("C", "E", 10),
    ("D", "E", 2), ("D", "F", 6), ("E", "F", 3)
]

for u, v, weight in edges:
    g.add_edge(u, v, weight)

print("Graph kota dan jarak:")
g.display()
print("-" * 30)

# 1. Menemukan rute terpendek dari A ke F
start, end = "A", "F"
path, total_distance = g.dijkstra(start, end)

print(f"Rute terpendek dari {start} ke {end}:")
print(f"Jalur: {' -> '.join(path)}")
print(f"Total Jarak: {total_distance}")

# 2. Menampilkan jangkauan kota dari titik A
print("\nJarak dari kota A ke kota lainnya:")
reachable = g.reachable_cities("A")
for city, dist in reachable:
    print(f"Ke {city}: {dist}")