from collections import deque

queue = deque()

n = int(input())
array = deque(sorted(map(int, input().split())))

max_num = 0
while True:
    front = array.popleft()
    end = array.pop()
    max_num = max(front+end, max_num)

    if len(array) == 0:
        break

print(max_num)