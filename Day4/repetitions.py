s = input()
n = len(s)

i, j = 0, 0
ans = 0
while i < n:
    j = i
    while j + 1 < n and s[j + 1] == s[j]:
        j += 1
    ans = max(ans, j - i + 1)
    i = j + 1
print(ans)