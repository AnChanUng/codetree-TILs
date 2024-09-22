a, b = map(int, input().split())

def solution(a, b):
    if a < b:
        small = a + 10
        big = b * 2
        return small, big
    elif a > b:
        small = b + 10
        big = a * 2
        return small, big