word = list(input())
dir_num = 3
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

x, y = 0, 0
dir_num = (dir_num + 1) % 4
dir_num = (dir_num + 3) % 4

for i in range(len(word)):
    if word[i] == 'L':
        if word[i+1] == 'F':
            nx = x + dx[dir_num]
    elif word[i] == 'R':
        if word[i+1] == 'F':
            ny = y + dy[dir_num]

print(nx, ny)