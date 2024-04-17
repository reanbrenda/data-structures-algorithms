n = int(input())

if n == 1:
    print(1)
elif n == 2 or n == 3:
    print("NO SOLUTION")
else:
    permutation = []
    for i in range(n, 0, -2):
        permutation.append(i)
    
    if n % 2 == 0:
        for i in range(n - 1, 0, -2):
            permutation.append(i)
    else:
        for i in range(2, n, 2):
            permutation.append(i)

    print(*permutation)
