
# n = int(input())
# company_tree = {i: [] for i in range(2, n+1)}
# try:
#     bosses = list(map(int, input().split()))
# except EOFError:
#     bosses = []
# for employee in range(2, n+1):
#     boss = 1
#     company_tree[boss].append(employee)
# def count_subordinates(employee):
#     subordinates_count[employee] = sum(count_subordinates(child) for child in company_tree[employee]) + len(company_tree[employee])
#     return subordinates_count[employee]
# subordinates_count = [0] * (n+1)
# count_subordinates(1)
# print(' '.join(map(str, subordinates_count[1:])))
n=int(input())
bosses = list(map(int, input().split()))
edges=[[] for i in range(n+1)]
ind=2
for i in bosses:
    edges[int(i)].append(ind)
    ind+=1
sub_size=(n+1)*[0]
def dfs(v:int):
    sub_size[v]=1
    for w in edges[v]:
        dfs(w)
        sub_size[v]+=sub_size[w]
dfs(1)
for i in range(1,n+1):
    sub_size[i]-=1
print(' '.join(map(str,sub_size[1:])))


