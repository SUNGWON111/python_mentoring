# https://www.acmicpc.net/problem/2739

# n이 주어진다
n = int(input())
# n은 1보다 크거나 같고 9보다 작거나 같다.
if 1 <= n <= 9:
    for i in range(9):
        print( n, '*', i + 1, '=', n * (i + 1) )