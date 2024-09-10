n = int(input())

array = [0] * 300
for _ in range(n):
    x1, x2 = map(int, input().split())

    for i in range(x1, x2+1):
        array[i] += 1

print(max(array))