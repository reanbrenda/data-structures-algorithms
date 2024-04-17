n, t = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0] * n
prefix_sum[0] = array[0]
for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + array[i]
count = 0
sum_map = {0: 1}  
for i in range(n):
    if (prefix_sum[i] - t) in sum_map:
        count += sum_map[prefix_sum[i] - t] 
    sum_map[prefix_sum[i]] = sum_map.get(prefix_sum[i], 0) + 1

print(count)
