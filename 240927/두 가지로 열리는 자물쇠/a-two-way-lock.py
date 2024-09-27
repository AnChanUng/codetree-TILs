n = int(input())
a1, b1, c1 = list(map(int, input().split()))
a2, b2, c2 = map(int, input().split())

array1 = set()
for i in range(a1-2, a1+2+1):
    for j in range(b1-2, b1+2+1):
        for k in range(c1-2, c1+2+1):
            
            ni = (i - 1) % n + 1
            nj = (j - 1) % n + 1
            nk = (k - 1) % n + 1
            array1.add((ni, nj, nk))

array2 = set()
for i in range(a2-2, a2+2+1):
    for j in range(b2-2, b2+2+1):
        for k in range(c2-2, c2+2+1):
            ni = (i-1) % n + 1
            nj = (j-1) % n + 1
            nk = (k-1) % n + 1
            
            array2.add((ni, nj, nk))

all_arr = array1 | array2
print(len(all_arr))