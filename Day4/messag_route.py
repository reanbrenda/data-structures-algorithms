from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
visited = [False] * (n+1)
prev = [None] * (n+1)
visited[1] = True

while queue:
    node = queue.popleft()
    if node == n:
        break
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            prev[neighbor] = node
            queue.append(neighbor)

if visited[n]:
    path = []
    at = n
    while at is not None:
        path.append(at)
        at = prev[at]
    path.reverse()
    print(len(path))
    print(' '.join(map(str, path)))
else:
    print("IMPOSSIBLE")
