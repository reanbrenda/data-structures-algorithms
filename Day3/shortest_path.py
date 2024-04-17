import heapq


n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


distances = [float('inf')] * (n+1)
distances[1] = 0
queue = [(0, 1)]  

while queue:
    distance, node = heapq.heappop(queue)
    if distance > distances[node]:
        continue
    for neighbor, weight in graph[node]:
        new_distance = distance + weight
        if new_distance < distances[neighbor]:
            distances[neighbor] = new_distance
            heapq.heappush(queue, (new_distance, neighbor))


for i in range(1, n+1):
    print(distances[i])
