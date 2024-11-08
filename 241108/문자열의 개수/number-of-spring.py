array = []
while True:
    word = input()
    array.append(word)
    
    if word == '0':
        if len(array) % 2 == 0:
            print(len(array)-1)
        else:
            print(len(array))
            
        for i in range(len(array)):
            if i % 2 == 0:
                print(array[i])
        break