n, x = map(int, input().split())
a = list(map(int, input().split()))

positions = {}
for i, v in enumerate(a):
    if v in positions:
        print(positions[v], i+1)
        break
    positions[x-v] = i+1
else:
    print("IMPOSSIBLE")
