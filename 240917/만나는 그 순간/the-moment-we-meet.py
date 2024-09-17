n, m = map(int, input().split())

distance1 = 0
array1 = []
for _ in range(n):
    d, t = input().split()
    t = int(t)

    if d == 'L':
        distance1 -= t
    elif d == 'R':
        distance1 += t
    
    array1.append(distance1)

distance2 = 0
array2 = []
for _ in range(m):
    d, t = input().split()
    t = int(t)
    print(d, t)

    if d == 'L':
        distance2 -= t
    elif d == 'R':
        distance2 += t

    array2.append(distance2)

print(array1[-1] - array[-2])