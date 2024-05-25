import heapq

def dijkstra(graph, start):
    # Ініціалізація відстаней до всіх вершин як нескінченність, окрім початкової
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0  # Відстань до початкової вершини

    # Створення бінарної купи для швидкого вибору вершини з найменшою відстанню
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань до цієї вершини більша, пропускаємо
        if current_distance > distances[current_vertex]:
            continue

        # Оновлення відстаней до сусідніх вершин
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад графу
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

start_vertex = 'A'
shortest_distances = dijkstra(graph, start_vertex)
print("Найкоротші відстані від вершини", start_vertex)
for vertex, distance in shortest_distances.items():
    print(f"До вершини {vertex}: {distance}")
