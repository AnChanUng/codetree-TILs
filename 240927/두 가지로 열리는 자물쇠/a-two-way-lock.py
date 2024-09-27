n = int(input())
a1, b1, c1 = list(map(int, input().split()))
a2, b2, c2 = map(int, input().split())

array1 = []
for i in range(a1-2, a1+2+1):
    for j in range(b1-2, b1+2+1):
        for k in range(c1-2, c1+2+1):
            if i < 1:
                i = n+i 
            elif j < 1: 
                j = n+j
            elif k < 1:
                k = n+k
            array1.append((i, j, k))

array2 = []
for i in range(a2-2, a2+2+1):
    for j in range(b2-2, b2+2+1):
        for k in range(c2-2, c2+2+1):
            
            if 1 <= i <= n and 1 <= j <= n and 1 <= k <= n:
            
                if i < 1:
                    i = n+i 
                elif j < 1: 
                    j = n+j
                elif k < 1:
                    k = n+k
                array2.append((i, j, k))
            
            continue

cnt = 0
for i in array1:
    for j in array2:
        if i == j:
            cnt += 1

print(len(array1) + len(array2) - cnt)