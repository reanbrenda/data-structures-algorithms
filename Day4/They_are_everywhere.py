
n = int(input())
s = input()

unique_types = set(s)
type_count = len(unique_types)
min_length = n
type_freq = {}

left = 0
for right in range(n):
    type_freq[s[right]] = type_freq.get(s[right], 0) + 1
    
    while len(type_freq) == type_count:
        min_length = min(min_length, right - left + 1)
        type_freq[s[left]] -= 1
        if type_freq[s[left]] == 0:
            del type_freq[s[left]]
        left += 1
            
print(min_length)

