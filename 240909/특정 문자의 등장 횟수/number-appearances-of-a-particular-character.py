word = input()

ee = 0
eb = 0
for i in range(len(word)-1):
    if word[i:i+2] == 'ee':
        ee += 1
    elif word[i:i+2] == 'eb':
        eb += 1

print(ee, eb)