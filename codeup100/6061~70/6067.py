# https://codeup.kr/problem.php?id=6067
a = int(input())
if a < 0:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
if a > 0:
    if a % 2 == 0:
        print('C')
    else:
        print('D')