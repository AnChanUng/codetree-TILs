import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())

arr = [0] * (n+1)
array = []
for _ in range(m):
    array.append(int(input()))

found = False
for i in range(len(array)):
    
    arr[array[i]] += 1
    
    if arr[array[i]] == k:
        print(array[i])
        break

if not found:
    print(-1)