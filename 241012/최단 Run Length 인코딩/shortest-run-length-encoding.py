word = input()

def encoding(words):
    cnt = 1
    res = ""
    array = []
    for i in range(1, len(words)):
        if words[i-1] == words[i]:
            cnt += 1
            if i == len(words)-1:
                res = words[i-1] + str(cnt)
                array.append(res)
        else:
            res = words[i-1] + str(cnt)
            array.append(res)
            cnt = 1
    if cnt == 1:
        array.append(word[-1] + '1')

    return ''.join(array)

min_total = 1001
for shift in range(1, len(word)+1):
    result = word[shift:] + word[:shift]
    total = encoding(result)
    min_total = min(min_total, len(total))
    
print(min_total)