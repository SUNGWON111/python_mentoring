# https://codeup.kr/problem.php?id=6068
n = int(input())
if 90 <= n:
    print('A')
elif 70 <= n <= 89:
    print('B')
elif 40 <= n <= 69:
    print('C')
else:
    print('D')