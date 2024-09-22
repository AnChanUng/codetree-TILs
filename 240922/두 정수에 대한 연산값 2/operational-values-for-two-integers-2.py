a, b = map(int, input().split())

if a < b:
    small = a + 10
    big = b * 2
    print(small, big)
elif a > b:
    small = b + 10
    big = a * 2
    print(small, big)
else:
    break