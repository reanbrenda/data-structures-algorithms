n=int(input())
array = list(map(int, input().split()))
count = 0
for i in range(n):
    for j in range(i+1, n):
        sum = array[i] + array[j]
        if (sum & (sum - 1)) == 0:
            count += 1
print(count)
