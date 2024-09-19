word = input()
dir_num = 3
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
x, y = 0, 0

for i in word:
    if i == 'L':
        dir_num = (dir_num -1 + 4) % 4
    elif i == 'R':
        dir_num = (dir_num + 1) % 4
    else:
        x = x + dx[dir_num]
        y = y + dy[dir_num]

print(x, y)