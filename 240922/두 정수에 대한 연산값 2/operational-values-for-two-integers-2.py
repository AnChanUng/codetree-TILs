def modify_numbers(a, b):
    small = min(a, b) + 10
    big = max(a, b) * 2
    return small, big

a, b = map(int, input().split())

result = modify_numbers(a, b)
print(*result)