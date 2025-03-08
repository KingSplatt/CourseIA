import heapq

class Graph:
    def __init__(self):
        self.graph = {}
        self.parent = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2, weight):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append((node2, weight))
        self.graph[node2].append((node1, weight))

    def dijkstra(self, start, target):
        INF = float('inf')
        distances = {node: INF for node in self.graph}
        distances[start] = 0
        pq = [(0, start)]
        self.parent = {}

        while pq:
            dist, node = heapq.heappop(pq)

            if dist > distances[node]:
                continue

            for neighbor, weight in self.graph[node]:
                new_dist = dist + weight
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    self.parent[neighbor] = node
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return distances[target] if distances[target] != INF else None
    
    def get_path(self, start, target):
        if target not in self.parent:
            return None
        path = []
        node = target
        while node != start:
            path.append(node)
            node = self.parent[node]
        path.append(start)
        path.reverse()
        return path

# Cargar datos desde archivo
file_path = "C:/Users/mari_/OneDrive/Escritorio/Main/Proyectos2/IA/CourseIA/Unidad2/Tarea1/Caminos.cvs.txt"
try:
    graph = Graph()
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    start_node = int(input("Ingrese el Pueblo desde donde iniciará el recorrido: "))
    graph.add_node(start_node)
    
    for line in lines[1:]:
        node1, node2, weight = map(int, line.strip().split(','))
        graph.add_edge(node1, node2, weight)
    
    print(f"Recorrido desde el pueblo: {start_node}")
    print("Cdad Prev | Cdad Act | Km")
    
    for node in graph.graph:
        if node != start_node:
            distance = graph.dijkstra(start_node, node)
            if distance is not None:
                path = graph.get_path(start_node, node)
                print(f"{start_node:9} | {node:8} | {distance:3} - Ruta: {path}")
            else:
                print(f"No se encontró camino a {node}")
except FileNotFoundError:
    print("No se encontró el archivo.")
