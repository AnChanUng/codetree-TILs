import sys
input = sys.stdin.readline

from collections import deque

queue = deque()

n = int(input().strip())
array = deque(sorted(map(int, input().split())))

max_num = 0
while len(array) > 1:
    front = array.popleft()
    end = array.pop()
    max_num = max(front+end, max_num)

print(max_num)