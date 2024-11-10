a = input()
b = input()
c = input()

max_length = max(len(a), len(b), len(c))
min_length = min(len(a), len(b), len(c))

result = max_length - min_length
print(result)