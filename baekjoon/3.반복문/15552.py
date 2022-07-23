# https://www.acmicpc.net/problem/15552
# 참고) https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
import sys

l = []
t = int(input())
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    l.append(a + b)
for i in l:
    print(i)
 