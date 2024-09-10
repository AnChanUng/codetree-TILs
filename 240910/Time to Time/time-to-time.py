a, b, c, d = map(int, input().split())

# 2시 4분 4시 1분

if d - b >= 0:
    print((c-a) * 60 + (d-b))

else:
    print((c-a-1) * 60 + 60-(b-d))