# https://www.acmicpc.net/problem/2741

n = int(input())
l = []
for i in range(1, n+1):
    l.append(i)
for i in l:
    print(i)

# 다른 풀이 https://www.acmicpc.net/source/16145897
# n=int(input())
# print("\n".join(map(str,range(1,n+1))))
# print(구분자, 리스트를 만들고 문자열로 변환해주어야 하므로 map함수 사용)
# join을 이용해 리스트를 문자열로 변형, 줄바꿈을 이용해 하나하나 출력
