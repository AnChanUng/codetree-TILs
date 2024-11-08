cnt = 0
while True:
    cnt += 1
    word = input()
    
    if cnt % 2 == 1:
        print(word)
    
    if word == 0:
        break