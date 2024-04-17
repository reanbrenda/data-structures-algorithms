n = int(input())
array = list(map(int, input().split()))
indx_arr = [0] * (n + 1) 

for i in range(n):
    indx_arr[array[i]] = i 

count = 1  

for i in range(2, n + 1):
    if indx_arr[i] < indx_arr[i - 1]:
        count += 1  
print(count)



