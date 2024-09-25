a, b = map(int, input().split())

def add(x, y):
    k = min(a, b) + 10
    l = max(a, b) * 2
    print(k, l)

add(a, b)