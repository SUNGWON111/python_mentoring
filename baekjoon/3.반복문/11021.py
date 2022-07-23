# https://www.acmicpc.net/problem/11021
# 참고) https://ooyoung.tistory.com/37, https://blockdmask.tistory.com/429
# key) f-string 이용
#     > f"{변수 or 함수}"/ 따옴표 앞에 f만 적고 변수나 함수를 사용할거면 중괄호로 감싸준다.
#  함수를 사용할 때 리턴값이 있어야 한다.
import sys
    
list_ = []
t = int(input())
"""각 테스트 케이스마다  Case #x:를 출력한다.
print(Case "#",x,:)"""
for i in range(t):
    a, b = map(int, sys.stdin.readline().split())
    list_.append(a+b)
for i in range(1, t+1):
    print(f"Case #{i}: {list_[i-1]}")