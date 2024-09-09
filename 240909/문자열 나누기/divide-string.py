n = int(input())
words = input().split()

result = ''
for i in range(n):
    result += words[i]

result = list(result)

for i in range(0, len(result), 5):
    res = ''.join(result[i:i+5])
    print(res)