def weather(y, m, d):
    is_leap = (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)

    days_in_month = {
        1: 31, 2: 29 if is_leap else 28, 3: 31, 4: 30,
        5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    if m not in days_in_month or d < 1 or d > days_in_month[m]:
        print(-1)
        return

    if 3 <= m <= 5:
        print("Spring")
    elif 6 <= m <= 8:
        print("Summer")
    elif 9 <= m <= 11:
        print("Fall")
    else:
        print("Winter")

y, m, d = map(int, input().split())
weather(y, m, d)