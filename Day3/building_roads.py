
n, m = map(int, input().split())

graph = {i: [] for i in range(1, n+1)}


for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs_stack(start_node):
    stack = [start_node]
    component = []
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            component.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    stack.append(neighbor)
    return component


visited = set()
components = []
for node in range(1, n+1):
    if node not in visited:
        components.append(dfs_stack(node))


new_roads = []
for i in range(len(components) - 1):
    new_roads.append((components[i][-1], components[i+1][0]))

print(len(new_roads))
for road in new_roads:
    print(road[0], road[1])
