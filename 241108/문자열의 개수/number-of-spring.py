array = []
cnt = 0
while True:
    word = input()
    array.append(word)
    
    if array[cnt] == '0':
        break

    cnt += 1

print(cnt)

for i in range(0, cnt, 2):
    print(array[i])