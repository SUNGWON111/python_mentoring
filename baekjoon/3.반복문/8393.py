# https://www.acmicpc.net/problem/8393
# 리스트 요소의 합을 구할 때 변수 하나를  생성에 0을 할당 후 
# 변수에 리스트 요소를 하나씩 더해준다.
l = []
# 변수x에 0을 할당한다
x = 0
n = int(input())
# 1~n까지의 합
# 1+...+n
# 1~n까지 리스트에 저장
for i in range(1, n+1):
    l.append(i)
# 저장된 리스트 요소들을 다 더한다.
for i in l:
    x += i
print(x)