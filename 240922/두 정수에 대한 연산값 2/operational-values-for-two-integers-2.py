a, b = map(int, input().split())

def solution(a, b):
    small = min(a, b) + 10
    big = max(a, b) * 2
    return small, big

print(*solution(a, b))