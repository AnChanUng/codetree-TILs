n, m = map(int, input().split())

array1 = []
result1 = 0
for _ in range(n):
    v, t = map(int, input().split())
    result1 = result1 + v * t
    array1.append(result1)

array2 = []
result2 = 0
for _ in range(m):
    v, t = map(int, input().split())
    result2 = result2 + v * t
    array2.append(result2)