h, m = map(int, input().split())
# 45 <= m =< 59 : m-45
if 45 <= m <= 59:
    print(h, m - 45)
#  m < 45 : h - 1, 60 + m - 45
# elif h == 0 and m < 45:
    # print(h = '11', m + 60 - 45) 오류 ?
elif h == 0 and m < 45:
    print( '23', m + 60 - 45)
else:
    print(h - 1, m + 60 - 45)