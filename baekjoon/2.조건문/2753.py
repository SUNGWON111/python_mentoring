y = int(input())
# 윤년은 4배수 or 400 배수
# 4의 배수일 경우
if y % 4 == 0 and y % 100 != 0:
    print('1')
elif y % 400 == 0:
    print('1')
else:
    print('0')