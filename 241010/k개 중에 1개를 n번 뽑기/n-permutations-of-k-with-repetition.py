k, n = map(int, input().split())

def simple(x, y):
    for i in range(1, k+1):
        for j in range(1, k+1):
            print(i, j, end = " ")
            print()

for _ in range(n-1):
    simple(k, n)